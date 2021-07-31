import threading
import time


class threadingA(threading.Thread):
    def __init__(self):
        # 初始化线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容：
        for i in range(10):
            print("我是线程A" +  str(i))
            time.sleep(1)


class threadingB(threading.Thread):
    def __init__(self):
        # 初始化线程
        threading.Thread.__init__(self)

    def run(self):
        # 该线程要执行的程序内容：
        for i in range(10):
            print("我是线程B" + str(i))
            time.sleep(1)


if __name__ == '__main__':
    t1 = threadingA()
    t1.start()
    t2 = threadingB()
    t2.start()
