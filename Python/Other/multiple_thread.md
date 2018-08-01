# Python 并发编程

## 多进程

1. **使用 multiprocessing 模块创建多进程** 

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

2. **multiprocessing** 模块提供了一个Pool 类来代表进程池对象

Pool 可以提供指定数量的进程供用户调用， 默认大小是CPU的核数。当有新的请求提交到Pool中

时， 如果池还没有满，那么就会创建一个新的进程用来执行该请求；但如果池中的进程数已经达到规定的最大值，那么该请求就会等待，直到池中有进程结束，才会创建新的进程来处理它

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

