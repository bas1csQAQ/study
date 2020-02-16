# 高级函数：就是参数可以是函数的函数
# map()：map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
# 比如说 有一个函数
def f(x):
  return x * x
# 需要将这个函数作用在一个list中
l = [1, 2, 3, 4, 5]
r = map(f, l)
print(list(r))

# reduce():reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
# 效果类似于reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
# 比如说 有一个函数
from functools import reduce
def add(a, b):
  return a + b
r1 = reduce(add, l)
print(r1)
# 显然这个效果使用内置函数sum()也可以实现
# 但是如果 将[1, 2, 3, 4, 5] 变成12345呢
def f1(x, y):
  return x * 10 + y
r2 = reduce(f1, l)
print(r2)

# 考虑到str也是序列 所以总结一下就可以写出一个 str转为int
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
  def fn(x, y):
        return x * 10 + y
  def char2num(s):
      return DIGITS[s]
  return reduce(fn, map(char2num, s))

print(str2int('1234'))

# 编写函数 使用map()将英文名的首字母大写
l1 = ['ADAM', 'LISA', 'barT']
def normalize(name):
  # str.capitalize()函数返回一个可利用的字符串 通常是首字母大写其他字母小写
  # str.title()函数返回一个标题案例的字符串 通常是首字母大写 其他字母小写
  return name.title()

print(list(map(normalize, l1)))


# 编写函数 使用reduce()函数求list中所有元素的乘积
l2 = [2, 3, 4, 5]
def prod(a, b):
  return a * b
print(reduce(prod, l2))


# 编写函数 使用 map()和reduce()实现 '123.456' -> 123.456
def str2float(s):
  i, f = s.split('.')
  # i: [1,2,3]
  # f: [3,4,5]
  def strTran(a, b):
    return a * 10 + b
  def char2num(s):
    return DIGITS[s]
  return reduce(strTran, map(char2num, i)) + reduce(strTran, map(char2num, f)) * pow(10, -len(f))
print(str2float('123.456'))
    

