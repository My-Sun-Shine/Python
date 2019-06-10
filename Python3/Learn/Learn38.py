# 多线程
import time
import threading


def loop():
    print("thread %s is running..." % threading.current_thread().name)
    n = 0
    while n < 5:
        n += 1
        print("thread %s >>> %s" % (threading.current_thread().name, n))
        time.sleep(1)
    print("thread %s ended." % threading.current_thread().name)


# threading.current_thread() 获取当前线程的实例 .name获取名称
# 主线程的名称为MainThread
print("Thread %s is running.." % threading.current_thread().name)
t = threading.Thread(target=loop, name="LoopThread")  # 给子线程命名
t.start()
t.join()
print("thread %s ended." % threading.current_thread().name)

# 线程锁 Lock ######################################################################################################################################


def change_it(n):
    global balance
    balance = balance+n
    balance = balance-n


def run_thread(n):
    for i in range(1000000):
        change_it(n)


def run_thread_lock(n):
    for i in range(1000000):
        lock.acquire()  # 先要获取锁
        try:
            change_it(n)
        finally:
            lock.release()  # 释放锁


balance = 0
# 两个线程交替对balance进行修改，会导致balance!=0,所以需要加一个lock
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
print("-"*20)
balance = 0
lock = threading.Lock()
t1_lock = threading.Thread(target=run_thread_lock, args=(5,))
t2_lock = threading.Thread(target=run_thread_lock, args=(8,))
t1_lock.start()
t2_lock.start()
t1_lock.join()
t2_lock.join()
print(balance)
