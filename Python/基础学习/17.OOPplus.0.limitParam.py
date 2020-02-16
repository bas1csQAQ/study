# 动态语言的灵活性表现在 在创建一个实例之后 可以给实例绑定任何属性和方法
class Student(object):
    pass
s = Student()
# 给实例绑定属性
s.name = 'lisa'
print(s.name)

def set_age(self, age):
    self.age = age

from types import MethodType
# 给实例绑定方法
s.set_age = MethodType(set_age, s)
s.set_age(20)
print(s.age)

# 但是 给实例绑定的方法 对于其他的实例是不起作用的
s1 = Student()
# s1.set_age(10) 会报错 是因为set_age方法在实例s上 s1上没有

# 当然 可以将方法绑定在类上 那么 通过类定义的实例都可以使用
def set_score(self, score):
    self.score = score
Student.set_score = set_score
s.set_score(90)
s1.set_score(89)
print(s.score)
print(s1.score)


# 通过使用 __slots__ 限制实例属性
# 比如 只允许给Student实例添加name和age属性
class Student1(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称
s2 = Student1()
s2.name = 'John'
s2.age = 20
# s2.score = 99 # 会报错 因为没有规定可以绑定score属性
# 要注意的是 __slots__ 只对当前类实例起作用 对继承的子类是不起作用的
class GraduateStudent(Student):
    pass
g = GraduateStudent()
g.score = 99

