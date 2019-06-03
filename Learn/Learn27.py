# 枚举类
from enum import Enum, unique
Month = Enum("Month", ("Jan", "Feb", "Mar", "Apr", "May",
                       "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"))
for name, member in Month.__members__.items():
    print(name, "=>", member, ",", member.value)

print("-"*20)

for date in Month:
    print(date.name, "=>", date, ",", date.value)

print("-"*20)

@unique  # 保证没有重复的value
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Web = 3
    Thu = 4
    Fri = 5
    Sat = 6


day1 = Weekday.Mon
print(day1)
print(Weekday["Mon"])  # 通过成员名称访问
print(Weekday(1))  # 通过value访问
print(day1.value)
for name, member in Weekday.__members__.items():
    print(name, "=>", member, ",", member.value)

print("-"*20)

for date in Weekday:
    print(date.name, "=>", date, ",", date.value)

print("-"*20)
