# 单元测试unittest
# 单元测试类
import unittest


class Dict(dict):
    # 被测试类
    # 继承dict，实现d=Dict(a=1,b=2) 调用d['a'] 得到1
    # 也可以调用d.a 得到1
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


class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        if self.score < 0 or self.score > 100:
            raise ValueError("the score must between 0 and 100")
        if self.score >= 80:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"


class TestDict(unittest.TestCase):
    # 继承单元测试类
    def test_init(self):
        d = Dict(a=1, b="test")
        self.assertEqual(d.a, 1)  # 断言是否相等
        self.assertEqual(d.b, "test")
        self.assertTrue(isinstance(d, dict))

    def test_key(self):
        d = Dict()
        d["key"] = "value"
        self.assertEqual(d.key, "value")

    def test_attr(self):
        d = Dict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")

    def test_keyerror(self):
        d = Dict()
        # with语句上下文管理器 多用于打开文件
        with self.assertRaises(KeyError):
            # 当key不存在是报错
            value = d["empty"]

    def test_attrerror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty

    def setUp(self):
        # 每个测试方法调用之前
        print("setUp....")

    def tearDown(self):
        # 每个测试方法调用之后
        print("tearDown....")


class TestStudent(unittest.TestCase):
    def test_80_to_100(self):
        s1 = Student("AA", 80)
        s2 = Student("CC", 100)
        self.assertEqual(s1.get_grade(), "A")
        self.assertEqual(s2.get_grade(), "A")

    def test_60_to_79(self):
        s1 = Student("AA", 60)
        s2 = Student("CC", 79)
        self.assertEqual(s1.get_grade(), "B")
        self.assertEqual(s2.get_grade(), "B")

    def test_0_to_59(self):
        s1 = Student("AA", 0)
        s2 = Student("CC", 59)
        self.assertEqual(s1.get_grade(), "C")
        self.assertEqual(s2.get_grade(), "C")

    def test_invalid(self):
        s1 = Student("AA", -1)
        s2 = Student("BB", 101)
        with self.assertRaises(ValueError):
            s1.get_grade()
        with self.assertRaises(ValueError):
            s2.get_grade()


# 调用测试
unittest.main()
