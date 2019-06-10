# 使用@property把一个getter方法变成属性进行访问，而它本身又创建一个@score.setter，负责把一个setter变成属性
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError("应该是int")
        if value < 0 or value > 100:
            raise ValueError("应该在0到100之间")
        self._score = value

    @property
    def grade(self):
        # 只读属性
        if self._score == 100:
            return "A"
        elif self._score >= 90:
            return "B"
        elif self._score >= 60:
            return "C"
        else:
            return "D"


s = Student()
s.score = 60
print(s.score)
# s.score = 9000
print(s.grade)


class Screen(object):
    # 有width和height两个可读可写的属性，以及一个只读属性resolution
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width*self._height


sc = Screen()
sc.height = 768
sc.width = 1024
print(sc.resolution)
