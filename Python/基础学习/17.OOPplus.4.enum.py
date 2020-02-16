# 枚举类型
# 当需要定义常量的时候，一个常用的办法是使用大写变量通过整数来定义，比如月份
JAN = 1
FEB = 2
MAR = 3
# ...
NOV = 11
DEC = 12
# 好处是简单 缺点是类型是int而且依旧只是变量
# 还有一个更好的办法就是通过枚举类型来定义class类型 每一个常量都是class的唯一实例
from enum import Enum
Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))
# 这样就得到了 Month类型的枚举类 可以直接通过 Month.Jan来引用一个常量 或者可以直接枚举所有成员
for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)
    # value值是自动赋值给成员的int常量 默认是从1开始的

# 如果想要更加精确的控制枚举类型 则需要使用Enum派生出自定义类
from enum import Enum, unique
@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6
# 其中 @unique装饰器用来检查并保证不存在重复值
# 访问枚举类型的话 有很多方法
day = Weekday.Mon
print(day)
print(Weekday.Tue)
print(Weekday['Tue'])
print(Weekday.Tue.value)
print(day == Weekday.Mon)
print(day == Weekday.Tue)
print(Weekday(1))
print(day == Weekday(1))
# 可以使用成员名称引用枚举常量 也可以直接通过value值来获取枚举常量


# 设计student类 然后gender使用枚举类型 
class Gender(Enum):
    Male = 0
    Female = 1

class Student(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
