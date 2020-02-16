# function 
# 使用def关键字 定义函数
def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x
# print(my_abs(2))
# print(my_abs(-8))

# 注意： 如果没有return语句，函数其实也会返回结果，只是返回的是None 
# return None 等价于 return

# 有时候可以定义一个空函数  使用pass关键字
def nop():
  pass
# print(nop())

# pass什么都不做 只是为了在还没想好函数体怎么写的时候 让程序先能运行
# pass还可以用在其他东西里面
age = 10 
if age >= 18:
  pass

# return 多个值
import math

def rectangle(x, y):
  c = 2 * (x + y)
  s = x * y
  return c, s
c, s = rectangle(2, 3)
print(c)
print(s)
# 看样子是返回了多个值 但是并不是
print(rectangle(2, 3))
# 函数上返回的多个值实际上就是返回一个 tuple 在语法上 返回一个tuple可以省略小括号， 多个变量可以同时接受一个tuple


# 参数检查
# 1.当参数个数不对的时候 会自动抛出 TypeError
# my_abs(1, 2) 
# 2.但是当参数类型不对的时候 解释器就不会自动检查了
# 看一下 内置函数 abs()和 手动写的my_abs()的区别
# abs('A') 会显示不能输入 str类型的
# my_abs('A') 只会显示 不能让str和int进行比较 即第四行的判断
# 使用内置函数isinstance(n, (dataType1, dataType2..)) 进行数据类型检查
def my_abs1(x):
  if not isinstance(x, (int, float)):
    print('只能输入 int或 float类型的数据')
    return 
  if x >= 0:
    return x
  else:
    return -x
my_abs1('A')
