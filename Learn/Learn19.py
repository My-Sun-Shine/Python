# 类class和类的实例
class Student(object):
    count = 0  # 这应该算是C#的静态变量，属于这个类，不属于某个实例

    def __init__(self, name, score):
        # 相当于C#中的类的构造函数，注意第一个参数一定是self，这个参数不需要传递
        # 该函数前后都有两个下划线__
        self.name = name  # 这是在self的变量 属于实例变量
        self.score = score
        Student.count += 1  # 每实例化一次 就加1

    def print_Student(self):
        # 定义一个方法，第一个参数是self，这个参数不需要传递
        print("%s %.2f" % (self.name, self.score))


stu = Student("AAA", 65)  # 类的实例化
print(Student)  # <class '__main__.Student'>
print(stu)  # <__main__.Student object at 0x000000545321D438>
print(stu.name, stu.score)
stu.print_Student()

stu.age = 8  # 可以对该实例对象进行动态绑定属性数据，并可以访问
print(stu.age)
# 注意这只是针对这一个实例对象，再实例化一个对象，则绑定的属性数据不可以使用
stu1 = Student("AAA", 65)
# stu1.age  # 报错没有该属性

# 目前已经实例化2次
print(Student.count)
