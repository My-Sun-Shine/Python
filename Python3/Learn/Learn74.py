# asyncio的编程模型是一个消息循环,从asyncio模块直接获取一个EventLoop的引用
# 然后把需要执行的协程放到EventLoop中
import asyncio
import threading


@asyncio.coroutine
def Hello():
    '@asyncio.coroutine把一个generator生成器变成coroutine类型'
    print("Hello world!", threading.currentThread())
    # 异步调用asyncio.sleep(1)
    r = yield from asyncio.sleep(1)
    print("Hello again!", threading.currentThread())


@asyncio.coroutine
def wget(host):
    print('wget %s...' % host)
    connect = asyncio.open_connection(host, 80)
    reader, writer = yield from connect
    header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
    writer.write(header.encode('utf-8'))
    yield from writer.drain()
    while True:
        line = yield from reader.readline()
        if line == b'\r\n':
            break
        print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
    # Ignore the body, close the socket
    writer.close()


loop = asyncio.get_event_loop()  # 获取一个EventLoop的引用
loop.run_until_complete(Hello())
print("--"*50)
# 使用任务Task封装两个coroutine
tasks = [Hello(), Hello()]
loop.run_until_complete(asyncio.wait(tasks))
print("--"*50)
# IO操作
tasks = [wget(host)
         for host in ['www.sina.com.cn', 'www.sohu.com', 'www.163.com']]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
