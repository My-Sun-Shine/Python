# 访问限制 私有属性
class Student(object):
    def __init__(self, name, score):
        # 相当于C#中的类的构造函数，注意第一个参数一定是self，这个参数不需要传递
        # 在python中，实例的变量如果以__开头，表示这就是一个私有变量
        self.__name = name  # 在属性前面加上两个下划线__
        self.__score = score

    def get_name(self):  # 这应该就是C#的get访问
        return self.__name

    def set_name(self, name):  # 这应该就是C#的set访问
        self.__name = name

    def print_Student(self):
        # 定义一个方法，第一个参数是self，这个参数不需要传递
        print("%s %.2f" % (self.__name, self.__score))


stu = Student("AAA", 65)  # 类的实例化
stu.print_Student()
print(stu.get_name())  # 取值
stu.set_name("CCC")  # 赋值
print(stu.get_name())

# 但是但是，虽然不能直接通过__name访问，主要是因为python解释器把__name转换成了_Student__name(版本不同的解释器，转换的结果不同)了，
# 所以通过访问_Student__name，又能访问，但是但是这种方法不建议使用
print(stu._Student__name)

# 在Learn19中有一个可以直接给实例绑定属性的情况
stu.__name = 8#但是，这只是给这个实例添加一个动态属性，并不能访问类中的__name属性，因为该属性在实例上已经变成了_Student__name
print(stu.__name)
