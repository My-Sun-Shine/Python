# 协程，生产者生产消息后，直接通过yield跳转到消费者开始执行，待消费者执行完毕后
# 切换回生产者继续生产，效率极高


def consumer():
    '消费者  生成器'
    r = ''
    while True:
        n = yield r  # 返回结果
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    '生产者'
    c.send(None)  # 启动生成器
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


c = consumer()
produce(c)
