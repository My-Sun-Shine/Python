# 文档测试doctest
import doctest

#在测试异常时，可以使用...表示中间一大段的输出
class Dict(dict):
    '''
    >>> d1 = Dict()
    >>> d1['x'] = 100
    >>> d1.x
    100
    >>> d1.y = 200
    >>> d1['y']
    200
    >>> d2 = Dict(a=1, b=2, c='3')
    >>> d2.c
    '3'
    >>> d2['empty']
    Traceback (most recent call last):
    ...
    KeyError:'empty'
    >>> d2.empty
    Traceback (most recent call last):
    ...
    AttributeError:'Dict' obejct has no attribute 'empty'
    '''

    def __init__(self, **kw):
        super().__init__(**kw)

    # 正常情况下 调用类中不存在的方法或属性，就会报错
    # 使用该方法可以动态返回一个属性或者方法
    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value


doctest.testmod()
