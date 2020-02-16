# 参数是函数中很重要的组成部分
# 设计一个函数 给一个数字 求这个数字的平方
def power(x):
  return x * x
print(power(5))

# 那么 如果要求一个数的3次方 4次方呢？ 总不能每一个都写一个函数 
# 所以这个时候想到了 新增一个参数 作为要求的次方数
def power1(x, n):
  s = 1
  while n > 0:
    n = n - 1
    s *= x
  return s
print(power1(2, 3))

# 那么这个时候我们就发现一个问题 因为调用函数的时候就必须要传递两个参数 不然就会报错
# 然而一般都是求平方的 所以有了默认参数
def power2(x, n = 2):
  s = 1
  while n > 0:
    n = n - 1
    s *= x
  return s
print(power2(3))
# 需要注意的是 默认参数必须要写在最后  而且默认参数必须要是不变对象
# 那么如果传递的是可变参数又会怎么样呢？
def add_end(l = []):
  l.append('end')
  return l
print(add_end())
print(add_end())
# 可以发现会如果一直执行方法的话 会一直往list中增加
# 那么怎么将上面的改为只增加一次end呢？
def add_end1(l = None):
  if l is None:
    l = []
  l.append('end')
  return l
print(add_end1())
print(add_end1())
# 这样就无论执行多少次 都只会增加一次end

# 可变参数
# 可以传入若干个参数进入函数
# 如果说 编写一个函数 求 1-5的所有数字平方和 那么可能会想到传入一个list 然后再循环计算
def calc(numbers):
  sum = 0
  for n in numbers:
    sum += n * n
  return sum  
print(calc([1, 2, 3, 4, 5])) 
# 但是这么调用的时候 总要先定义一个list来  那么有没有什么办法可以不用list呢？
# 可变参数就是为了解决这种问题而出现的  在参数前面加了一个* 这样在函数内部就会相当于接收到一个tuple 
# 调用的时候就相当方便了
def calc1(*numbers):
  sum = 0
  for n in numbers:
    sum += n * n
  return sum 
print(calc1(1, 2, 3))
# 那么 如果已经有了一个list或者tuple了  需要使用list中的元素进行计算 要怎么办呢？
nums = [1, 2, 3, 4]
print(calc1(nums[0], nums[1], nums[2]))
# 这样固然可以 但是看起来也太麻烦了
# python允许在list或者tuple前面增加一个* 表示把list中所有的元素作为可变参数传入函数中
print(calc1(*nums))

# 关键字参数
# 关键字参数允许传入0个或者多个含有参数名的参数， 这些参数会在函数内部被封装成一个dict
def person(name, age, **kw):
  print('name:', name, 'age:', age, 'others:', kw)
person('Michael', 20)
person('Michael', 20, gener='M', job='Engineer')
# 同样的 如果事先有了一个dict 也可以直接使用dict中的数据
d = {'city': 'BeiJing', 'job': 'Engineer'}
person('Jack', 20, city=d['city'], job=d['job'])
# 或者
person('John', 17, **d)
# 这样表示将现有的dict中所有的key-value用关键字参数的形式传入函数中 
# 注意 这样相当于是将数据的副本传入了函数 在函数中更改内容不会改变外部的dict内容
# 关键字参数可以用于注册页面 只有一些参数是必须的时候， 可以将可选项利用关键字参数的形式定义函数

# 命名关键字参数
# 如果说 想要限制关键字参数的参数名 例如只接收city和job作为关键字参数
# 需要在位置参数和关键字参数中间加一个*作为分隔
def person1(name, age, *, city, job):
  print('name:', name, 'age:', age, 'city:', city, 'job', job)
person1('Jack', 20, city='BeiJing', job='Engineer')
# 如果是函数的定义中已经有了一个可变参数 那么在后面跟着的关键字参数就不用*作为分隔了
def person2(name, age, *args, city, job):
  pass
# 需要注意的是 关键字参数在传入的时候 如果没有参数名 会报错 即关键字参数在传参的时候 必须有参数名

# 怎么判断关键字参数有没有传递到函数内部呢？
# 使用 in对关键字参数进行检查
def person3(name, age, **kw):
  if 'city' in kw:
    # 关键字参数中有 city
    pass
  if 'job' in kw:
    # 关键字参数中有 job
    pass
  print('name:', name, 'age:', age, 'others:', kw)


# 多种不同参数的使用
# 多种参数一同使用的时候 参数顺序必须是：
# 必选参数、默认参数、可变参数、命名关键字参数、关键字参数

def f1(a, b, c=0, *args, **kw):
  print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
  print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

# 常规调用
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

# 有趣的是 可以使用 tuple和dict来调用上述函数
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)

# 对于任何函数 都可以通过 类似 func(*args, **kw)的形式调用  无论这个函数是怎么定义的


# 设计函数 使其可接收一个或多个数并计算乘积
def multiplication(x, *y):
  mul = x
  for n in y:
    mul *= n
  return mul
# print(multiplication(1, 2, 3))