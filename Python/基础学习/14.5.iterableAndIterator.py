# 可迭代类型和迭代器
# 注意： 可迭代类型和迭代器并不是一个东西

# 只要能够使用for循环的都是可迭代类型
# 一类是 稽核数据类型 ： list tuple dict str set等
# 一类是generator: 包括生成器和带有yield的generator function
# 可以使用 collections模块中的 iterable来判断是否是可迭代类型
from collections.abc import Iterable
print(isinstance([], Iterable)) # list
print(isinstance({}, Iterable)) # dict
print(isinstance('abc', Iterable)) # str
print(isinstance((x for x in range(10)), Iterable)) # generator
print(isinstance(100, Iterable)) # int  int不是迭代类型

# 而迭代器指的是，可以被next()方法调用 并且不断返回下一个值的对象叫做迭代器 iterator
# 可以使用collections模块中的 iterator来判断是否是迭代器
from collections.abc import Iterator
print(isinstance([], Iterator)) # list false
print(isinstance({}, Iterator)) # dict false
print(isinstance('abc', Iterator)) # str false
# list dict str 都不是迭代器 但是如果想要把可迭代类型转换成迭代器 可以使用iter()函数
print(isinstance(iter([]), Iterator)) # list true
print(isinstance(iter({}), Iterator)) # dict true
print(isinstance(iter('abc'), Iterator)) # str true

# 那么 为什么list dict str 这些可迭代类型为什么不是迭代器呢？
# 因为 迭代器在python中表示的是数据流，可以使用next()方法不断地调出下一个值 知道没有数据的时候抛出异常，但是永远不可知这个序列有多长 只能不断的通过next()方法取出下一个值
# 迭代器是惰性的 只有在返回下一个数据的时候才会进行计算

# python中的for实际上本质上是不断地调用next()方法实现的
for x in [1, 2, 3, 4, 5]:
  pass
# 等价于：

# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
  try:
      # 获得下一个值:
      x = next(it)
  except StopIteration:
      # 遇到StopIteration就退出循环
      break