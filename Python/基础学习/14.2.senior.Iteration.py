# 迭代就是使用for循环进行遍历
# python中的foe不仅可以作用在list和tuple中 只要是可迭代对象都可以使用

# 对 dict进行遍历
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
  print(key)
# 由于 dict不是按照list那样按顺序存储的  所以可能会出现 acb这种迭代顺序
# 默认情况下 dict迭代的是key值
# 可以使用 for value in d.values(): 来遍历value值
for value in d.values():
  print(value)
# 也可以使用 for k, v in d.items(): 来同时遍历key, value值
for k, v in d.items():
  print(k,v)

# 字符串也是可迭代对象 
for ch in 'ABC':
  print(ch)

# 只要使用for就可以对可迭代对象进行迭代 但是怎么才能确定这是一个可迭代对象呢？
# 使用collections模块中的 iterable类型进行判断
# 引入collections 中的Iterable
from collections.abc import Iterable
# 使用isinstance判断一个元素是否可以被迭代
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))


# 如果说想要实现对list像java那样的下标循环怎么办
# 使用内置函数 enumerate 
for i, value in enumerate(['A', 'B', 'C']):
  print(i, value)

# 像上述的同时引用两个变量的方式 很常用
for x, y in [(1, 2), (2, 4), (3, 9)]:
  print(x, y)


# 编写函数 求一个list中的最大值和最小值
# 正常想法
def findMinAndMax(l):
  if len(l) == 0:
    return (None, None)
  max = l[0]
  min = l[0]
  for n in l:
    if n > max:
      max = n
    if n < min:
      min = n
  return (max, min)

# python思想写法
def findMinAndMax1(l):
  if len(l) == 0:
    return (None, None)
  return (min(l), max(l))

l = [1,2,3,4,12,3,4354,65,543,423,4]
print(findMinAndMax1(l))
print(findMinAndMax(l))

print(findMinAndMax1([]))
print(findMinAndMax([]))
