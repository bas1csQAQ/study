# 定制类
# 在python的类中有很多特殊用途的函数(例如__len__  __slots__) 可以帮助定义类
class Student(object):
    def __init__(self, name):
        self.name = name
# 打印一个实例
print(Student('Michael'))
# 可以发现 除了打印的类型 其他的信息什么也看不到 
class Student1(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student1 object (name: %s)' % self.name
    # def __repr__(self):
    #     return 'Student1 object (name: %s)' % self.name
    __repr__ = __str__
print(Student1('Lisa')) 
# __str__()方法用于定义在打印实例的时候输出的字符串
s1 = Student1('Lisa')
print(s1)
# 两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串
# 但是3.7版本中 这两个方法好像给设计为相等了 也就是说 无论设置了哪一个方法 另一个方法都会变得相同
# 在3.5版本的时候还是两个方法  可能是考虑到这两个方法大多时候都是一个内容吧

# 使用 __iter__()方法实现迭代
# 该方法返回一个迭代对象 
class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，所以返回自己

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100: # 退出循环的条件
            raise StopIteration()
        return self.a # 返回下一个值
# 当使用的时候 for就会不断的调用__next__()方法
for n in Fib():
    print(n)
    
# 虽然说这个迭代实例看起来像list 但是确实不能够当作list来使用
# 比如取第五个值  是不能够这么用的  
# print(Fib()[5])
# 但是可以使用__getitem__()方法表现成list那样按照下标取值 
class Fib1(object):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a
f = Fib1()
print(f[0])
print(f[3])
print(f[5])
# 这样就可以实现使用下标取值了

# 使用__getattr__()方法，在取不存在的属性的时候 动态返回一个属性
class Student2(object):  
    def __init__(self):
        self.name = 'Michael'
s2 = Student2()
print(s2.name) # 调用已经存在的属性 没有问题
# print(s2.score) # 调用不存在的属性 就会报错
class Student3(object):  
    def __init__(self):
        self.name = 'Michael'
    def __getattr__(self, attr):
        if attr == 'score':
            return 99
s3 = Student3()
print(s3.name)
print(s3.score) 
# 调用不存在的属性时，比如score，Python解释器会试图调用__getattr__(self, 'score')来尝试获得属性，就有机会返回score的值
# 当然 这个也可以返回函数
class Student4(object):
    def __getattr__(self, attr):
        if attr == 'age':
            return lambda: 25
s4 = Student4()
print(s4.age())
# 不过要注意的是 返回函数 在调用的时候就要加上小括号

# 每一个类都可以有自己的方法和属性 创建实例之后可以使用方法
# 同时 任何类，只需要定义一个__call__()方法，就可以直接对实例进行调用
class Student5(object):
    def __init__(self, name):
        self.name = name
    def __call__(self):
        print('My name is %s.' % self.name)
s5 = Student5('John')
s5()

# 使用callable()方法判断一个变量是对象还是函数
print(callable(s5))
print(callable(max))
print(callable([1, 2, 3]))
print(callable('str'))
