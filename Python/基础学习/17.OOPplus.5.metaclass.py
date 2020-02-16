# 动态语言和静态语言的最大的区别 就是在函数和类的定义 不是编译时定义的而是运行时动态创建的
from hello import Hello # 导入hello模块
# 当python解释器载入hello模块的时候 就会执行这个模块中所有的语句 执行结果就是创建出了一个Hello的class
h = Hello()
print(type(Hello))
print(type(h))
# 是用type()函数可以查看一个类型或者变量的类型， Hello是一个class，它的类型就是type，而h是一个实例，它的类型就是class Hello

# type()函数既可以返回一个对象的类型，又可以创建出新的类型，比如，我们可以通过type()函数创建出Hello类，而无需通过class Hello(object)...的定义
def fn(self, name='world'): # 先定义函数
    print('hello %s' % name)
Hello1 = type('Hello1', (object,), dict(hello = fn)) # 创建 Hello1对象
h1 = Hello1()
print(h1.hello())
print(type(Hello1))
print(type(h1))
# 使用type()函数创建class对象需要传入三个参数
# 1.class的名称
# 2.继承的父类集合，是一个tuple类型 
# 3.class的方法名称和函数绑定

# 使用type()函数创建类和直接写类定义是完全一样的， python解释器在遇到class的时候只是扫描一下class的语法 然后在内部使用type()函数创建出class


# 另一种创建clss的方法是使用metaclass
# 对于metaclass简单的说就是：
# 有了类 就可以创建实例
# 那么 如果想要创建类 就要用到metaclass
# 也就是说 先定义metaclass  然后通过metaclass创建class  再通过class创建实例
# 类可以看成是metaclass的实例
# 通常来说 metaclass是不会用到的 所以我没看懂就不写下来误导你了



