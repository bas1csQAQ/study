# 虽然可以是用class来封装数据 隐藏了内部的逻辑原理 但是却依旧可以通过外部修改一个实例的内部属性
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s, %s' % (self.name, self.score))
Jack = Student('Jack', 56)
Jack.print_score()
# 在这里修改name属性
Jack.name = 'lisa'
Jack.print_score()
# 可以发现name的值确实是被改变了 
# 那么怎么才能让一个属性不被外部修改呢？
# 在属性名前面加上__  在python中 如果一个变量以__开头，那么这就是一个私有变量 在外部是无法访问的
class Student1(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def print_score(self):
        print('%s, %s' % (self.__name, self.__score))
John = Student1('John', 56)
John.print_score()
# print(John.__name)  可以发现外部已经没办法访问属性了
# 这样就可以保证了外部代码无法随意更改对象内部的属性状态 通过访问限制保护实例对象

# 但是 如果外部代码想要获取name和score属性呢？
# 可以在类中加上get方法
class Student2(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_name(self):
        print(self.__name)
    def get_score(self):
        print(self.__score)

# 如果又要允许外部修改score呢
class Student3(object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def set_score(self, score):
        self.score = score
    # 在set方法中 还可以加上对参数的检查 保证参数的正确性
    def set_score1(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')


# 在python中 不同格式的变量名 具有不同的意义
# __xxx__ 这种格式的表示特殊变量 可以直接访问
# __xxx 这种格式的是私有变量
# _xxx 这种格式的是可以被直接访问的 但是会约定俗成的要求视为私有变量 而不访问

# 那么 双下划线开头的实例变量 真的就不能够从外部访问吗？
# 不能够直接访问是因为 python的解释器将变量名改为了 _Student1__name  通过这个就可以访问变量了
print(John._Student1__name) # 24行的John变量
# 但是 不建议使用  因为不同的解释器会把变量改成不同格式的属性名





