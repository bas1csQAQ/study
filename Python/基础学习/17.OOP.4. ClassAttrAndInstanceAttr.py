# 实例属性和类属性
# 可以通过实例变量或者self对实例进行绑定属性
class Student(object):
    def __init__(self, name):
        # 通过self 对实例进行绑定属性
        self.name = name
s = Student('lisa')
# 通过实例对象进行绑定属性
s.score = 90

# 可以在类中定义属性 这时候 这个属性就归类所有 称作类属性
class Student1(object):
    name = 'Student'
# 创建实例对象 不给绑定属性值
s1 = Student1()
# 这个时候 由于实例没有name属性 所以会往上查找类的属性 所以打印了Student
print(s1.name) 
# 但是 如果给实例绑定 name属性 再进行打印呢
s1.name = 'Bob'
print(s1.name) 
# 可以发现这个时候 输出的是绑定的属性值
# 这是由于 实例属性的优先级比类属性的优先级高 在访问属性的时候会优先访问实例对象本身
# 但是 类属性并不是给删除掉了
print(Student1.name) # 他依旧存在 只是优先级低 查找不到这里而已
del s1.name # 如果删除实例对象的name属性
print(s1.name) # 可以发现又查找到了类属性

# 所以在设计程序的时候 千万不要将类属性和实例属性的属性名设置成一样的 不然会由于优先级产生冲突


# 设计程序 统计学生人数 给类增加count属性 每创建一个属性就让count自增
class Student2(object):
    count = 0
    def __init__(self, name):
        self.name = name
        Student2.count += 1
if Student2.count != 0:
    print('测试失败!')
else:
    bart = Student2('Bart')
    if Student2.count != 1:
        print('测试失败!')
    else:
        lisa = Student2('Bart')
        if Student2.count != 2:
            print('测试失败!')
        else:
            print('Students:', Student2.count)
            print('测试通过!')
