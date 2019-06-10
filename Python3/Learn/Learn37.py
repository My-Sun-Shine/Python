# 多进程
import subprocess
from multiprocessing import Process, Pool, Queue
import os
import time
import random


def run_proc(name):
    # getpid() 获取当前进程的ID
    print("Run child process %s (%s)..." % (name, os.getpid()))


if __name__ == "__main__":
    print("——"*30)
    print("Parent process %s." % os.getpid())
    # 获取一个Process对象，代表一个进程对象
    p = Process(target=run_proc, args=("test",))
    print("Child process will start.")
    p.start()  # 启动
    print("Child process......")
    p.join()  # 等待子进程结束
    print("Child process end.")

# 启动大量的子进程，使用进程池Pool##################################################################################################################################


def long_time_task(name):
    print("run task %s (%s)..." % (name, os.getpid))
    start = time.time()
    time.sleep(random.random()*3)
    end = time.time()
    print("task %s runs %0.2f seconds." % (name, (end-start)))


if __name__ == "__main__":
    print("——"*30)
    print("Parent process %s." % os.getpid())
    n = 1
    p = Pool(n)  # Pool有个默认值 为电脑CPU的核数
    for i in range(n+1):
        # 添加进程
        p.apply_async(long_time_task, args=(i,))
    print("等待所有子进程结束....")
    p.close()  # 调用之后就不能再添加新的进程了
    p.join()  # 等待所有的子进程结束，在使用join之前必须先调用close方法
    print("所有子进程结束")

# 子进程的输入和输出 subprocess模块 ###################################################################################################################################################
if __name__ == "__main__":
    print("——"*30)
    print("$ nslookup www.python.org")
    r = subprocess.call(["nslookup", "www.python.org"])
    print("Exit code:", r)
    print("——"*30)
    print("$ nslookup")
    p = subprocess.Popen(["nslookup"], stdin=subprocess.PIPE,
                         stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b"set q=mx\npython.org\nexit\n")
    print(output.decode("gbk"))
    print("Exit code:", p.returncode)

# 进程之间进行通信 #############################################################################################################################


def write(q):
    # 写入数据的进程代码
    print("Process to write: %s" % os.getpid())
    for value in ["A", "B", "C"]:
        print("Put %s to Queue..." % value)
        q.put(value)
        time.sleep(random.random())


def read(q):
    # 读取数据的进程代码
    print("Process to read: %s" % os.getpid())
    while True:
        value = q.get(True)
        print("Get %s from Queue." % value)


if __name__ == "__main__":
    print("——"*30)
    q = Queue()  # 父进程创建队列，并传给各个子进程
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    pw.start()  # 启动写入进程
    pr.start()  # 启动读取进程
    pw.join()  # 等待写入进程结束
    pr.terminate()  # 读取进程是死循环，无法等待结束，只能强行终止
