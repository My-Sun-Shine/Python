# 对于Learn74.py的新语法
# 把@asyncio.coroutine替换为async；
# 把yield from替换为await。
import asyncio
import threading

async def Hello():
    '@asyncio.coroutine把一个generator生成器变成coroutine类型'
    print("Hello world!", threading.currentThread())
    # 异步调用asyncio.sleep(1)
    r = await asyncio.sleep(1)
    print("Hello again!", threading.currentThread())

loop = asyncio.get_event_loop()  # 获取一个EventLoop的引用
loop.run_until_complete(Hello())