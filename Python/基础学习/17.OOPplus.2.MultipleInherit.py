# 多继承
# 比如说动物界中 有的动物可以跑 有的动物可以飞 有的动物是哺乳动物 有的动物属于鸟类
class Animal(object):
    pass
class Mammal(Animal):
    pass
class Bird(Animal):
    pass
class Runnable(object):
    def run(self):
        print('Running...')
class Flyable(object):
    def fly(self):
        print('Flying...')

# 这就可以分为四种类型的  但是有的动物可以属于其中的两种甚至更多的
# 比如说狗 又是可以跑的 又是哺乳动物 
class Dog(Mammal, Runnable):
    pass
# 比如说蝙蝠 又是可以飞的 又是哺乳动物
class Bat(Mammal, Flyable):
    pass
# 这就是多继承 通过多继承可以让一个子类同时拥有很多个父类的功能

# 在python中允许使用多继承 MixIn就是一种
# 在设计继承的时候 通常都是单一继承下来的 但是如果需要混合一些额外的功能 就要使用多继承来实现了
# 这种多继承的设计通常称作MixIn