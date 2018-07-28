from threading import Thread
import time
from colorama import Fore


class CountdownTask(object):

    def __init__(self, name, color):
        self._running = True
        self.name = name
        self.color = color

    def terminate(self):
        self._running = False

    def run(self, n):

        while self._running and n > 0:
            print(self.color + self.name + 'T-minus: ' + str(n))
            n -= 1
            time.sleep(5)


if __name__ == "__main__":
    """
    Python 解释器会等待所有线程（除了守护进程）结束，才会停止运行，
    守护线程在后台一直运行，在主线程结束时停止运行
    """
    c = CountdownTask('t1', color=Fore.GREEN)
    c2 = CountdownTask('t2', color=Fore.RED)
    t1 = Thread(target=c.run, args=(5,), daemon=True)
    t2 = Thread(target=c2.run, args=(4,))
    t1.start()
    t2.start()
