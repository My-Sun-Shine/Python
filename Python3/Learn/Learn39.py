# 在多线程环境中，每个线程都有自己的数据
# 一个线程使用自己的局部变量比使用全局变量好的多，局部变量只有线程自己访问到，不会影响其他线程
# 但是全局变量所有线程都会访问，所以要加锁
# ThreadLocal类型对象，是一个全局变量，但是每个线程都只能读写自己线程的独立副本，互不影响
# 解决了参数在一个线程多个函数直接互相传递的问题
import threading

# 创建全局变量
local_school = threading.local()


def proess_student():
    # 获取当前线程关联的student
    std = local_school.student
    print("Hello, %s (in %s)" % (std, threading.current_thread().name))


def proess_thread(name):
    # 绑定ThreadLocal的student
    local_school.student = name
    proess_student()


t1 = threading.Thread(target=proess_thread, args=("AAA",), name="Thread_A")
t2 = threading.Thread(target=proess_thread, args=("BBB",), name="Thread_B")
t1.start()
t2.start()
t1.join()
t2.join()
