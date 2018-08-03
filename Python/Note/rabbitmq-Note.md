# RabbitMQ

消息（Message）是指在应用间传送的数据。消息可以非常简单，比如只包含文本字符串，也可以更复杂，可能包含嵌入对象。

消息队列（Message Queue）是一种应用间的通信方式，消息发送后可以立即返回，由消息系统来确保消息的可靠传递。消息发布者只管把消息发布到 MQ 中而不用管谁来取，消息使用者只管从 MQ 中取消息而不管是谁发布的。这样发布者和使用者都不用知道对方的存在。

 RabbitMQ 是一个由 Erlang 语言开发的 AMQP 的开源实现。

AMQP ：Advanced Message Queue，高级消息队列协议。它是应用层协议的一个开放标准，为面向消息的中间件设计，基于此协议的客户端与消息中间件可传递消息，并不受产品、开发语言等条件的限制。



## RabbitMQ 安装

一般来说安装 RabbitMQ 之前要安装 Erlang ，可以去[Erlang官网](https://link.jianshu.com/?t=http://www.erlang.org/downloads)下载。接着去[RabbitMQ官网](https://link.jianshu.com/?t=https://www.rabbitmq.com/download.html)下载安装包，之后解压缩即可。根据操作系统不同官网提供了相应的安装说明：[Windows](https://link.jianshu.com/?t=http://www.rabbitmq.com/install-windows.html)、[Debian / Ubuntu](https://link.jianshu.com/?t=http://www.rabbitmq.com/install-debian.html)、[RPM-based Linux](https://link.jianshu.com/?t=http://www.rabbitmq.com/install-rpm.html)、[Mac](https://link.jianshu.com/?t=http://www.rabbitmq.com/install-standalone-mac.html)

 

## RabbitMQ 运行和管理

```shell
# MAC /usr/local/Cellar/rabbitmq/3.7.4/sbin 执行命令所在目录
./rabbitmq-server # 启动
./rabbitmq-server -detached # 后台启动
./rabbitmqctl status # 查询服务器状态
./rabbitmqctl stop # 关闭整个RabbitMQ节点
./rabbitmqctl -n rabbit@server.example.com stop # 关闭指定的节点
./rabbitmqctl reset # 重置 RabbitMQ 节点， 该命令将清除所有的队列
./rabbitmqctl list_queues # 查看已声明的队列
./rabbitmqctl list_exchanges # 查看交换器
./rabbitmqctl list_bindings # 查看绑定
```

## 核心理念

- 发布者（producer）是发布消息的应用程序。
- 队列（queue）用于消息存储的缓冲。
- 消费者（consumer）是接收消息的应用程序。

 

## 使用Python 操作 RabbitMQ

`pip install pika` 

 

1. **简单的收发消息**

```python
# send.py
import pika
"""
发送一个消息到队列中
"""
# 建立到 RabbitMQ 的连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()
# 创建一个名为 hello 的队列
channel.queue_declare(queue='hello')

# 将消息发送到 Exchange 中 默认交换机用空字符串标识

channel.basic_publish(exchange='', routing_key='hello', body='Hello, World!')
print("[x] Sent 'Hello, World!' ")
connection.close()
```

```python
# receive.py
import pika

"""
从队列中获取消息，并打印消息
"""

# 建立到 RabbitMQ 的连接
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 重复声明创建一个名为 hello 的队列， 避免队列不存在
channel.queue_declare(queue='hello')


# 定义回调函数， 当我们获取到消息的时候，Pika 库就会调用此回调函数。
# 这个回调函数会将接收到的消息内容输出到屏幕上
def callback(ch, method, properties, body):
    print("[x] Received {}".format(body.decode()))


# ack = acknowledgement character 确认信号
channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
# 我们输入一个用来等待消息数据并且在需要的时候运行回调函数的无限循环
channel.start_consuming()
```

2. **创建一个工作队列**

工作队列（又称：任务队列——Task Queues）是为了避免等待一些占用大量资源、时间的操作。当我们把任务（Task）当作消息发送到队列中，一个运行在后台的工作者（worker）进程就会取出任务然后处理。当你运行多个工作者（workers），任务就会在它们之间共享。

 ```python
# new_task.py
import pika

"""
发送任务到工作队列中
"""

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()
channel.queue_declare('hello')
message = input("> ")

channel.basic_publish(exchange='', routing_key='hello', body=message)
print("[x] Sent '{}' ".format(message))
connection.close()
 ```

```python
# worker.py
import pika
import time

"""
它需要为消息体中每一个点号（.）模拟1秒钟的操作。它会从队列中获取消息并执行
"""

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))

channel = connection.channel()

channel.queue_declare('hello')


def callback(ch, method, properties, body):
    print(" [x] Received {}".format(body))

    time.sleep(body.decode().count('.'))
    print(" [x] Done")


channel.basic_consume(callback, queue='hello', no_ack=True)
print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
```

3. **消息确认**

当处理一个比较耗时得任务的时候，你也许想知道消费者（consumers）是否运行到一半就挂掉。当前的代码中，当消息被 RabbitMQ 发送给消费者（consumers）之后，马上就会在内存中移除。这种情况，你只要把一个工作者（worker）停止，正在处理的消息就会丢失。同时，所有发送到这个工作者的还没有处理的消息都会丢失。

我们不想丢失任何任务消息。如果一个工作者（worker）挂掉了，我们希望任务会重新发送给其他的工作者（worker）。

为了防止消息丢失，RabbitMQ 提供了消息响应（acknowledgments）。消费者会通过一个 ack（响应），告诉 RabbitMQ 已经收到并处理了某条消息，然后RabbitMQ 就会释放并删除这条消息。

如果消费者（consumer）挂掉了，没有发送响应，RabbitMQ 就会认为消息没有被完全处理，然后重新发送给其他消费者（consumer）。这样，及时工作者（workers）偶尔的挂掉，也不会丢失消息。

消息是没有超时这个概念的；当工作者与它断开连的时候，RabbitMQ 会重新发送消息。这样在处理一个耗时非常长的消息任务的时候就不会出问题了。

消息响应默认是开启的。之前的例子中我们可以使用 no_ack=True 标识把它关闭。是时候移除这个标识了，当工作者（worker）完成了任务，就发送一个响应。

 ```python
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.') )
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_consume(callback,
                      queue='hello') 
 ```

4. **消息持久化**

如果你没有特意告诉 RabbitMQ，那么在它退出或者崩溃的时候，将会丢失所有队列和消息。为了确保信息不会丢失，有两个事情是需要注意的：我们必须把“队列”和“消息”设为持久化。

首先，为了不让队列消失，需要把队列声明为持久化（durable）：

```python
channel.queue_declare(queue='hello', durable=True)
```

尽管这行代码本身是正确的，但是仍然不会正确运行。因为我们已经定义过一个叫hello 的非持久化队列。RabbitMq 不允许你使用不同的参数重新定义一个队列，它会返回一个错误。但我们现在使用一个快捷的解决方法——用不同的名字，例如task_queue。

```python
channel.queue_declare(queue='task_queue', durable=True)
```

这时候，我们就可以确保在 RabbitMq 重启之后 queue_declare 队列不会丢失。另外，我们需要把我们的消息也要设为持久化——将 delivery_mode 的属性设为2。

```python
channel.basic_publish(exchange='',
                      routing_key="task_queue",
                      body=message,
                      properties=pika.BasicProperties(
                         delivery_mode = 2, # make message persistent
                      ))
```

5. **公平调度**

你应该已经发现，它仍旧没有按照我们期望的那样进行分发。比如有两个工作者（workers），处理奇数消息的比较繁忙，处理偶数消息的比较轻松。然而RabbitMQ 并不知道这些，它仍然一如既往的派发消息。

这时因为 RabbitMQ 只管分发进入队列的消息，不会关心有多少消费者（consumer）没有作出响应。它盲目的把第 n-th 条消息发给第 n-th 个消费者。

我们可以使用 basic.qos 方法，并设置 prefetch_count=1。这样是告诉RabbitMQ，在同一时刻，不要发送超过1条消息给一个工作者（worker），直到它已经处理了上一条消息并且作出了响应。这样，RabbitMQ 就会把消息分发给下一个空闲的工作者（worker）。

```python
channel.basic_qos(prefetch_count=1)
```

如果所有的工作者都处理繁忙状态，你的队列就会被填满。你需要留意这个问题，要么添加更多的工作者（workers），要么使用其他策略。

6. **发布/订阅**

分发一个消息给多个消费者（consumers）。这种模式被称为“发布／订阅”。

 RabbitMQ 消息模型的核心理念是：**发布者（producer）不会直接发送任何消息给队列**。事实上，发布者（producer）甚至不知道消息是否已经被投递到队列。

发布者（producer）只需要把消息发送给一个交换机（exchange）。交换机非常简单，它一边从发布者方接收消息，一边把消息推送到队列。交换机必须知道如何处理它接收到的消息，是应该推送到指定的队列还是是多个队列，或者是直接忽略消息。这些规则是通过交换机类型（exchange type）来定义的。

有几个可供选择的交换机类型：**直连交换机（direct）**, **主题交换机（topic）**, （头交换机）headers和 **扇型交换机（fanout）**。我们在这里主要说明最后一个 —— 扇型交换机（fanout）。先创建一个 fanout 类型的交换机，命名为 logs：

```python
channel.exchange_declare(exchanges='logs', exchange_type='fanout')
```

**临时队列**

你还记得之前我们使用的队列名吗（ hello 和 task_queue）？给一个队列命名是很重要的——我们需要把工作者（workers）指向正确的队列。如果你打算在发布者（producers）和消费者（consumers）之间共享同队列的话，给队列命名是十分重要的。

但是这并不适用于我们的日志系统。我们打算接收所有的日志消息，而不仅仅是一小部分。我们关心的是最新的消息而不是旧的。为了解决这个问题，我们需要做两件事情。

首先，当我们连接上 RabbitMQ 的时候，我们需要一个全新的、空的队列。我们可以手动创建一个随机的队列名，或者让服务器为我们选择一个随机的队列名（推荐）。我们只需要在调用 queue_declare 方法的时候，不提供 queue 参数就可以了：

```python
result = channel.queue.declare()
```

这时候我们可以通过 `result.method.queue` 获得已经生成的随机队列名。它可能是这样子的：amq.gen-U0srCoW8TsaXjNh73pnVAw==。

第二步，当与消费者（consumer）断开连接的时候，这个队列应当被立即删除。exclusive 标识符即可达到此目的。

```python
result = channel.queue_declare(exclusive=True) 
```

**绑定**

我们已经创建了一个扇型交换机（fanout）和一个队列。现在我们需要告诉交换机如何发送消息给我们的队列。交换器和队列之间的联系我们称之为绑定（binding）

```python
channel.queue_bind(exchange='logs', queue=result.method.queue)
```

```python
# log_send.py

"""
实时转发消息给所有消费者， 如果没有消费者，则消息就会被忽略
"""
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# 创建 fanout 类型的交换机， 交换机的名字是logs
channel.exchange_declare(exchange='logs', exchange_type='fanout')
# 如果没有绑定队列到交换器，消息将会丢失。
# 但这个没有所谓，如果没有消费者监听，那么消息就会被忽略
message = "Hello, World!"
channel.basic_publish(exchange='logs', routing_key='', body=message)
print(" [x] Sent {}".format(message))

connection.close()
```

```python
# log_receive.py
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# 创建 fanout 类型的交换机， 交换机的名字是logs
channel.exchange_declare(exchange='logs', exchange_type='fanout')

# 创建临时队列，当消费者断开连接时，这个队列立即被删除
result = channel.queue_declare(exclusive=True)
# 获取队列的名字
queue_name = result.method.queue

# 绑定队列
channel.queue_bind(exchange='logs',
                   queue=queue_name)

print(' [*] Waiting for logs. To exit press CTRL+C')


def callback(ch, method, properties, body):
    print(" [x] %r" % (body,))


channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

channel.start_consuming()
```

