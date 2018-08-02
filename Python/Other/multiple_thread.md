# Python 并发编程

## 多进程

### 1. 基础知识

获取进程号：`os.getpid()`   `Process.pid`

获取进程名：`Process.name`

获取当前进程对象： `multiprocessing.current_process()`

启动进程：`Process.start()`

阻塞住主进程，等待子进程运行完毕：`Process.join()`

终止进程：`Process.terminate()`

创建守护进程， 守护进程不能被终止， 主进程结束，守护进程随之结束：

`p = Process(target=func, daemon=True)`



### 2. 使用 multiprocessing 模块创建多进程 

multiprocessing 模块提供了一个Process类来描述一个进程对象。创建子进程时，只要传入一
个执行函数和函数的参数，即可完成一个Process实例的创建， 用start()方法启动进程，用
join()方法实现进程间的同步

```python
import os
from multiprocessing import Process

def run_proc(name):
    print("Child process {} ({}) Running...".format(name, os.getpid()))

print('Parent process ', os.getpid())
for p in [Process(target=run_proc, args=(str(i),)) for i in range(5)]:
    print("Process will start.")
    p.start()
```

### 3. multiprocessing 模块提供了一个Pool 类来代表进程池对象

Pool 可以提供指定数量的进程供用户调用， 默认大小是CPU的核数。当有新的请求提交到Pool 时， 如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定的最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来处理它

```python
from multiprocessing import Pool
import os, time, random
"""
程序创建了容量为4（4核心CPU）的进程池， 依次向进程池中添加了10个任务。
从运行结果中可以看到虽然添加了10个任务， 但是一开始只运行了4个，而且每次最多运行
3个进程。当一个任务结束了， 新的任务依次添加进来，任务执行使用的进程依然是原来的
进程， 通过进程的 pid 就可以看出来

Pool 对象调用 join() 方法会使主进程等待所有子进程执行完毕， 调用join()之前
必须先调用close(), 调用close()之后就不能继续添加新的Process了。
"""

def run_task(name):
    print("Task {} (pid = {}) is running...".format(name, os.getpid()))
    time.sleep(random.random() * 3)
    print("Task {} end.".format(name))


if __name__ == '__main__':
    print('Current process {}.'.format(os.getpid()))
    p = Pool()
    for i in range(10):
        p.apply_async(run_task, args=(str(i),))

    print("Waiting for all subprocess done...")
    p.close()
    p.join()
    print('All subprocess done')
```

### 4. 使用面向对象的方式创建进程

```python
import multiprocessing

# 继承 multiprocessing.Process
class My_Process(multiprocessing.Process):
    
    # override __init__()
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.args = args
        self.kwargs = kwargs
        
    # override run()
    def run(self):
        print(multiprocessing.current_process())
        print(self.args)
        print(self.kwargs)
        
if __name__ == "__main__":
    p = My_Process(1,2,3, a=1, b=2, c=3)
    p.start()
```

### 5. 进程间通信

Python提供了多种进程间通信的方式， 例如Queue, Pipe, Value+Array等。 Queue 用来在多个进程间实现通信，Pipe 常用来在两个进程间通信。

#### Queue通信

Queue是多进程安全的队列，可以使用Queue实现多进程之间的数据传递。有两个方法：Put和Get可以进行Queue操作：

1. Put 方法用以插入数据到队列中， 它还有两个可选参数：blocked 和 timeout。如果blocked为True（默认值），并且 timeout 为正值， 该方法会阻塞timeout 指定的时间， 直到该队列有剩余的空间。如果超时，会抛出 Queue.Full 异常。如果blocked 为 False, 但该 Queue 已满， 会立即抛出 Queue.Full 异常。
2. Get 方法可以从队列读取并且删除一个元素。同样，Get 方法有两个可选参数：blocked 和timeout。 如果blocked 为True （默认值）， 并且timeout 为正值， 那么在等待时间内没有取到任何元素，会抛出Queue.Empty 异常。 如果 blocked 为False，分两种情况：如果 Queue 有一个值可用， 则立即返回该值； 否则， 如果队列为空， 则立即抛出Queue.Empty 异常。

```python
from multiprocessing import Process, Queue
import multiprocessing
import os, time, random

"""
在父进程中创建三个子进程，
两个子进程往Queue中写入数据
一个子进程从Queue中读取数据
"""


def proc_write(q, urls):
    print('Process {} is writing...'.format(multiprocessing.current_process().pid))
    for url in urls:
        q.put(url)
        print('Put {} to Queue'.format(url))
        time.sleep(random.random())


def proc_read(q):
    print('Process {} is reading...'.format(os.getpid()))
    while True:
        url = q.get(True)
        print("Get {} from Queue".format(url))


def main():
    q = Queue()
    proc_writer1 = Process(target=proc_write, args=(q, ['url1', 'url2', 'url3']))
    proc_writer2 = Process(target=proc_write, args=(q, ['url4', 'url5', 'url6']))
    proc_reader = Process(target=proc_read, args=(q,))

    # 开始写
    proc_writer1.start()
    proc_writer2.start()

    # 开始读
    proc_reader.start()

    # 等待写入进程 finished，然后close 读进程
    proc_writer1.join()
    proc_writer2.join()

    proc_reader.terminate()


if __name__ == '__main__':
    main()

```

#### Pipe 通信

Pipe 常用来在两个进程间进行通信， 两个进程分别位于管道的两端。

Pipe 方法返回（conn1, conn2）代表一个管道的两个端。Pipe 方法有duplex 参数， 如果duplex 参数为 True(默认值)， 那么这个管道是全双工模式， 也就是说 conn1 和 conn2 均可收发，若 duplex 为 False, conn1 只负责接收消息， conn2 只负责发送消息。send 和 recv 方法分别是发送和接收消息的方法。 例如， 在全双工模式下， 可以调用conn1.send发送消息， conn1.recv 接收消息。 如果没有消息可接收， recv方法会一直阻塞。如果管道已经被关闭，那么recv 方法会抛出 EOFError。

```python
import multiprocessing
import random
import time
import os

"""
创建两个进程， 一个子进程通过 Pipe发送数据，
一个子进程通过Pipe接收数据
"""


def proc_send(pipe, urls):
    for url in urls:
        print('Process {} send: {}'.format(os.getpid(), url))
        pipe.send(url)
        time.sleep(random.random())


def proc_recv(pipe):
    while True:
        print('Process {} recv: {}'.format(os.getpid(), pipe.recv()))
        time.sleep(random.random())


def main():
    # conn1 = send port; conn2 = recv port
    conn1, conn2 = multiprocessing.Pipe()
    p_send = multiprocessing.Process(
        target=proc_send, args=(conn1, ['url' + str(i) for i in range(10)]))
    p_recv = multiprocessing.Process(target=proc_recv, args=(conn2,))
    p_send.start()
    p_recv.start()


if __name__ == '__main__':
    main()
```



## 多线程

### 1. 用 threading 模块创建多线程

`threading` 模块一般通过两种方式创建多线程：第一种方式是把一个函数传入并创建Thread实例， 然后调用 start() 方法开始执行； 第二种方式是直接从 `threading.Thread` 继承并创建线程类， 然后重写 `__init__()` 和 `run()` 

```python
# 第一种方式

import random
import time
import threading

"""
获取当前线程对象 - threading.current_thread() 
获取线程的名字 - Thread.name
"""

def thread_run(urls):
    print('Current {} is running'.format(threading.current_thread().name))
    for url in urls:
        print('{}---->>>{}'.format(threading.current_thread().name, url))
        time.sleep(random.random())
    print("{} ended.".format(threading.current_thread().name))


def main():
    print('Current {} is running'.format(threading.current_thread().name))
    t1 = threading.Thread(target=thread_run, args=(['url1', 'url2', 'url3'],))
    t2 = threading.Thread(target=thread_run, args=(['url4', 'url5', 'url6'],))

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('Current {} ended'.format(threading.current_thread().name))


if __name__ == '__main__':
    main()
```

```python
# 第二种方式
import random
import time
import threading


class MyThread(threading.Thread):
    def __init__(self, urls):
        super().__init__()
        self.urls = urls

    def run(self):
        print('Current {} is running'.format(self.name))
        for url in self.urls:
            print('{}---->>>{}'.format(self.name, url))
            time.sleep(random.random())
        print("{} ended.".format(self.name))


def main():
    print('Current {} is running'.format(threading.current_thread().name))
    t1 = MyThread(urls=['url1', 'url2', 'url3'])
    t2 = MyThread(urls=['url4', 'url5', 'url6'])

    t1.start()
    t2.start()
    t1.join()
    t2.join()

    print('Current {} ended'.format(threading.current_thread().name))


if __name__ == '__main__':
    main()
```

### 2. 线程同步

如果多个线程共同对某个数据修改， 则可能出现不可预料的结果，为了保证数据的正确性，需要对多个线程进行同步。使用 Thread 对象的 Lock 和 RLock 可以实现简单的线程同步，这两个对象都有 acquire 方法和 release 方法， 对于那些每次只允许一个线程操作的数据，可以将其操作放到 acquire 和 release 方法之间。

对于 Lock 对象而言， 如果一个线程连续两次进行 acquire 操作， 那么由于第一次 acquire 之后没有 release，第二次 acquire 将挂起线程。 这会导致 Lock 对象永远不会 release，使得线程死锁。RLock 对象允许一个线程多次对其进行 acquire 操作， 因为在其内部通过一个 counter 变量维护着线程 acquire 的次数。 而且每一次的acquire 操作必须有一个 release 操作与之对应，在所有的 release 操作完成之后，别的线程才能申请该 RLock 对象。

```python
import threading

my_lock = threading.RLock()
num = 0


class MyThread(threading.Thread):

    def __init(self):
        super().__init__()

    def run(self):
        global num
        while True:
            my_lock.acquire()
            if num >= 4:
                my_lock.release()
                print('{} released, Number: {}'.format(self.name, num))
                break
            num += 1
            print('{} locked, Number: {}'.format(self.name, num))
            my_lock.release()


def main():
    t1 = MyThread()
    t2 = MyThread()
    t1.start()
    t2.start()


if __name__ == '__main__':
    main()
```

### 3. 全局解释器锁(GIL)

在 Python 的原始解释器 CPython 中 存在着 GIL (Global Interpreter Lock), 因此在解释执行Python代码时，会产生互斥锁来限制线程对共享资源的访问，直到解释器遇到 I/O 操作或者操作次数达到一定数目时才会释放 GIL。由于全局解释器锁的存在，在进行多线程操作的时候，不能调用多个CPU内核，只能利用一个内核，所以在进行 CPU 密集型操作的时候， 不推荐使用多线程， 更加倾向于多进程。对于IO密集型操作，多线程可以明显提高效率，例如 Python 爬虫的开发， 绝大多数时间爬虫是在等待 socket 返回数据，网络 IO 的操作延时比 CPU 大得多。