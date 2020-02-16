# 获取对象信息
# 当拿到一个对象的引用的时候 怎么判断这个对象是什么类型的 有哪些方法？
# 1.使用type()方法
# 基本类型都可以使用type()方法进行判断
print(type(123))
print(type('abc'))
print(type(None))
# 如果说一个变量指向一个函数或者类 那么type()方法也可以进行判断
print(type(abs))

# type()方法返回是对应的class类型  那么如果想要进行判断怎么办
print(type(123) == type(456))
print(type(123) == int)
print(type('abc') == type('456'))
print(type('abc') == str)
print(type(123) == type('abc'))
# 可以发现 对于基本数据类型 可以直接使用 int，str等进行判断
# 但是 如果想要判断一个对象是否是函数呢？
# 使用 types 模块
import types
def fn():
    pass
print(type(fn) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# 对于class的继承关系来说 type()方法就差强人意了 所以要判断class类型 要使用 isinstance()方法
# isinstance() 方法判断的是对象是否是该类型本身 或者该类型是否在类型的父继承链上
class Animal(object):
    pass
class Dog(Animal):
    pass
class Husky(Dog):
    pass
a = Animal()
d = Dog()
h = Husky()
print(isinstance(h, Husky)) # true 因为h确实属于Husky类型
print(isinstance(h, Dog)) # true 因为h属于的Husky类型确实是由dog继承来的
print(isinstance(h, Animal)) # 所以 可以确信h也属于animal
print(isinstance(d, Animal)) # 同样的 也可以确定d属于animal类型
# 要注意的是
print(isinstance(d, Husky))
# 一个对象只能是属于对应的类型或者对应类型的父继承链上的类型 而不能是属于子类型
# 就好比说 一个人长得像他爸爸 而不能说他爸爸长得像他儿子

# 对于基本数据类型来说 也可以使用isinstance()方法
print(isinstance('a', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

# 甚至说 还可以判断一个变量是否属于某些类型中的一个
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))

# 所以 在进行判断的时候 总要优先使用isinstance()判断类型

# 使用dir()方法获取一个对象中的所有方法和属性 
print(dir('abc'))
# 可以发现返回的方法中 很多都是类似__xxx__的 这种类型的方法和属性在python中都是由特殊用途的
# 比如说__len__返回长度  如果使用len()方法来获取长度的时候 实际上在内部是调用的__len__()方法
# 所以说 
print(len('abc'))
# 和
print('abc'.__len__())
# 是等价的

# 如果对于自己写的类 想要使用 len(myObj)的话 就要自己写一个 __len__()方法
class MyDog(object):
    def __len__(self):
        return 100
dog = MyDog()
print(len(dog))

# 除了类似__xxx__类型的属性和方法之外 其他的都是普通方法或属性 比如
print('abc'.upper()) # 返回大写的字符串


# 但是更多时候 只是把方法和属性列出来是不够的 
# 需要配合 getattr() setattr() hasattr()来对一个对象进行操作
class MyObject(object):
    def __init__(self):
        self.x = 11
    def power(self):
        return self.x * self.x
obj = MyObject()
# 使用 hasattr()方法判断是否有某个属性 
print(hasattr(obj, 'x'))
print(hasattr(obj, 'y'))
# 使用 setattr()方法对对象设置属性 y
setattr(obj, 'y', 20)
print(hasattr(obj, 'y'))
# 使用getattr()方法获取属性y
print(getattr(obj, 'y'))
# 等同于直接通过对象点属性名获取属性
print(obj.y)
# 但是 对于getattr()方法来说 如果获取了不存在的属性就会报错 但是可以给定第三个参数给默认值 如果属性不存在就返回默认值
print(getattr(obj, 'z', 30))

# 当然以上三个方法 对于方法也适用
print(hasattr(obj, 'power')) 
print(getattr(obj, 'power'))
fn  = getattr(obj, 'power') # 可以直接获取到属性power 并赋值给fn
print(fn())



# 要注意的是，只有在不知道对象信息的时候，我们才会去获取对象信息
# 如果可以写
# obj.x + obj.y
# 就绝对不要写
# getattr(obj, 'x') + getattr(obj, 'y')




