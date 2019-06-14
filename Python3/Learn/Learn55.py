# psutil模块获取系统信息
import psutil
print("CPU逻辑数量:", psutil.cpu_count())
print("CPU物理核心:", psutil.cpu_count(logical=False))
print("CPU频率:",psutil.cpu_freq())
print("CPU当前系统利用率:",psutil.cpu_percent())
print("CPU统计数据:",psutil.cpu_stats())
print("系统范围内的CPU时间:",psutil.cpu_times())
print("对于每个特定的CPU时间提供利用率:",psutil.cpu_times_percent())
print("从1970年以来以秒表示的系统启动时间:",psutil.boot_time())
print("当前连接在系统上的用户列表:",psutil.users())
print("CPU的用户/系统/空闲时间:")
print(psutil.cpu_times())

print("模拟ps命令，获取所有正在运行的进程信息")
# psutil.test()

# 类似top命令的CPU使用率，每秒刷新一次，累计10次
# for x in range(10):
#     psutil.cpu_percent(interval=1,percpu=True)

# 内存信息
print("获取物理内存信息")
print(psutil.virtual_memory())
print("获取交换内存信息")
print(psutil.swap_memory())

# 磁盘信息
print("获取磁盘分区信息")
print(psutil.disk_partitions())
print("获取磁盘使用情况")
print(psutil.disk_usage("/"))
print("获取磁盘IO")
print(psutil.disk_io_counters())

# 网络信息
print("获取网络读写字节/包的个数")
print(psutil.net_io_counters())
print("获取网络接口信息")
# print(psutil.net_if_addrs())
print("获取网络接口状态")
print(psutil.net_if_stats())

# 获取当前网络连接信息
print("获取当前网络连接信息")
# print(psutil.net_connections())

# 进程信息
print("获取所有进程ID")
pids_list = psutil.pids()
print(pids_list)
pid = input("输入需要获取信息的进程ID>>>")
# isdigit判断字符串是否都是数字
while pid.isdigit() and int(pid) in pids_list:
    p = psutil.Process(int(pid))  # 获取某个进程
    try:
        print("进程名称", p.name())
        print("进程exe路径", p.exe())
        print("进程的工作目录", p.cwd())
        print("进程启动的命令行", p.cmdline())
        print("父进程ID", p.ppid())
        print("父进程", p.parent())
        print("子进程列表", p.children())
        print("进程状态", p.status())
        print("进程用户名", p.username())
        print("进程创建时间", p.create_time())
        print("进程终端", p.terminal())
        print("进程使用CPU时间", p.cpu_times())
        print("进程使用的内存", p.memory_info())
        print("进程打开的文件", p.open_files())
        print("进程相关网络连接", p.connections())
        print("进程的线程数量", p.num_threads())
        print("所有线程信息", p.threads())
        print("进程环境变量", p.environ())
    except:
        pass
    # p.terminate()  # 结束进程
    print(pids_list)
    pid = input("输入需要获取信息的进程ID>>>")
print("end")


