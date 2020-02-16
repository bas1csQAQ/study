# 函数作为返回值
# 在高阶函数中  函数不仅可以作为参数传入函数 也可以作为返回值返回出去
# 比如
# 这样可以实现一个可变参数的求和
def calc_sum(*args):
  sum = 0
  for n in args:
    sum += n
  return sum
# 但是 如果要求不立即求和 而在后续还需要进行计算呢？
def lazy_sum(*args):
  def sum():
    ax = 0
    for n in args:
      ax = ax + n
    return ax
  return sum
f = lazy_sum(1, 2, 3, 4)
print(f)
# 可以看到打印的是一个函数对象  也就是说当调用lazy_sum()时，返回的并不是求和结果，而是求和函数
# 当调用f()的时候 才是真的计算求和
print(f())

# 一般来说 函数执行完毕之后 相应的内存也会删除  但是像这种将内部函数返回 并且还能够访问之前的一些参数和变量的存在 称作闭包 
# 被返回的函数不会立即执行  知道被调用f()为止
# 闭包
def count():
  fs = []
  for i in range(1, 4):
    def f():
      return i * i
    fs.append(f)
  return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
# 可以发现上述输出都是9
# 这是因为 闭包不会立即执行 他们函数中引用的都是i 但是当for in结束的时候 i的值已经变成了3 所以i*i自然都是3*3

# 为了解决这个问题 所以需要将引用改变
def count1():
  # def f(j):
  #   def g():
  #     return j*j
  #   return g
  # 以上f函数可以使用lambda来简化代码
  def f(i):
    return lambda : i*i
  fs = []
  for i in range(1, 4):
    fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
  return fs
f4, f5, f6 = count1()
print(f4())
print(f5())
print(f6())


# 使用闭包 返回一个计数器函数 每次调用的时候递增
def createCounter():
  n = 0
  def counter():
    nonlocal n # 使用nonlocal关键字改变n的作用域
    n += 1
    return n
  return counter
c = createCounter()
print(c())
print(c())
print(c())
