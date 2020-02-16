# 装饰器

def now():
  print('2019-08-04')

# 现在假设 想要增强now()函数的功能， 比如在使用函数的前后自动打印日志，但是又不想要改变函数原先的定义。
# 这种在函数运行期间动态增加功能的方式 就是装饰器
# 在本质上 装饰器是一个返回函数的高阶函数
# 所以 这里定义一个函数
def log(func):
  def wrapper(*args, **kw):
    print('log : call %s()' % func.__name__) ## __name__是每个函数都有的属性 可以拿到函数的名字
    return func(*args, **kw)
  return wrapper
# 装饰器接受一个函数作为参数 然后返回一个函数 
# 使用@语法将 装饰器放在函数的定义位置
@log
def now1():
  print('2019-08-04')
# 执行函数 发现不仅仅是运行了now1()函数本身 而且还在执行函数之前打印了日志
now1()
# 这是因为 将@log放到now1()函数的定义处 相当于执行了 now = log(now)

# 如果说装饰器本身需要传入参数， 那么就需要多谢一个返回装饰器的高阶函数
# 比如说要自定义日志文字
def log1(text):
  def decorator(func):
    def wrapper(*args, **kw):
      print('log: %s %s()' % (text, func.__name__))
      return func(*args, **kw)
    return wrapper
  return decorator

@log1('execute')
def now2():
  print('2019-08-04')

now2()
# 三层嵌套相当于 now2 = log1('execute')(now2)

# 但是 当我们查看被装饰器装饰的函数的__name__的时候
print(now2.__name__)
# 发现变成了wrapper 
# 只是因为当装饰器函数返回的时候 返回的函数名就是wrapper 所以就把wrapper()函数的属性都复制过来了
# 那么怎么纠正回来呢
# 使用 functools中的wraps来解决这个问题
import functools

# 使用functools.wraps解决__name__被修改的问题
# 只需要在wrapper()函数上增加@functools.wraps(func)就行了
def log2(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    print('call %s():' % func.__name__)
    return func(*args, **kw)
  return wrapper

@log2
def now3():
  print('2019-08-04')

now3()
print(now3.__name__)

# 设计装饰器 要求 可以做用于任何函数上 并且打印该函数的执行时间
import time
def metric(func):
  @functools.wraps(func)
  def wrapper(*args, **kw):
    localtime = time.asctime( time.localtime(time.time()))
    print('execute %s() at %s' % (func.__name__, localtime))
    return func(*args, **kw)
  return wrapper

@metric
def now4():
  print('now4()')

now4()