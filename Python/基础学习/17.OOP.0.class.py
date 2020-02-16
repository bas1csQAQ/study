# OOP 是面向对象编程 是一种编程思想 将对象作为程序的基本单元 一个对象包含了数据和操作数据的函数
# 面向过程的程序设计把计算机程序视为一系列的命令集合，即一组函数的顺序执行。为了简化程序设计，面向过程把函数继续切分为子函数，即把大块函数通过切割成小块函数来降低系统的复杂度。
# 而面向对象的程序设计把计算机程序视为一组对象的集合，而每个对象都可以接收其他对象发过来的消息，并处理这些消息，计算机程序的执行就是一系列消息在各个对象之间传递。

# 比如说  现在要处理学生的成绩
# 使用面向过程
stu1 = {'name': 'Michael', 'score': 95}
def print_score(stu):
    print('name: %s, score: %s' % (stu['name'], stu['score']))
print_score(stu1)

# 使用面向对象
# 先创建一个学生对象 通过这个对象将成绩信息打印出来
class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s, %s' % (self.name, self.score))

lisa = Student('Lisa', 93)
lisa.print_score()

# 要明确类和实例的概念  
# 比如说人是一个类 然后类里面是人共同的属性 名字 性别 身高 等等  把属性抽出来当作一个类
# 每一个人实际上就是把属性给定 有了确定的各个属性值
# 大概这个意思


# 在python中使用class关键字定义类
# class关键字后面是类名 (object)表示这个类是从哪里继承的  如果不知道该写什么继承类 或者没有合适的 就写object 这是所有类最终都会继承的
class Person(object):
    pass
# 将类实例化 就是通过类名()来实现的  这样就实例出了一个person对象
person = Person()

# 在类中通过__init__()方法对实例进行赋值
class Person1(object):
    # __init__()方法的第一个参数永远是self 代表实例对象本身  在实例化的时候 self不需要传值
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
bart = Person1('bart', 'M')
print(bart.name, bart.gender)

# 这些被注入的数据是实例对象本身拥有的 所以没必要使用外部函数来调用数据 
# 而是在类的内部定义访问数据的函数， 这样就将数据封装了起来
class Person2(object):
    # __init__()方法的第一个参数永远是self 代表实例对象本身  在实例化的时候 self不需要传值
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
    def print_gender(self):
        print(self.gender)

blue = Person2('blue', 'M')
blue.print_gender()

# 将数据封装起来之后 在调用类方法的时候就会很简单 而且外部并不知道内部的逻辑的实现细节
# 类是实例对象的模板 


