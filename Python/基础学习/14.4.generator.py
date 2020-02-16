# 使用列表生成式 可以直接创建一个list 但是由于内存大小有限 所以list的数量肯定是有限的
# 而且一旦是创建了大量元素的list 然后又只是访问一些或者几个元素的时候 这难免会造成大量的内存浪费
# generator就是为了解决这个问题出现的
# generator不会将list完全创建出来 而是在循环的过程中不断的推算出后续的元素
# 创建generator的方法
# 1.将列表生成式的中括号换成小括号
l = [x * x for x in range(10)]
print(l)
g = (x * x for x in range(10))
print(g)
# 使用generator的next()方法 就可以调用下一个值
print(next(g))
# 但是一直使用next()方法未免太麻烦了 所以还是要使用for
for n in g:
  print(n)


# 斐波拉契数列 使用列表生成式写不出来 但是使用函数就好写了
def fib(max):
  n, a, b = 0, 0, 1
  while n < max:
    print(b)
    a, b = b, a + b
    n += 1
  return 'done'
fib(3)

# 看这个覅波拉契数列的函数 很明显的是根据前面的数字来推算后面的数字  
# 那么这个思路是不是跟generator是一样的呢？
# 那么 是不是可以把fib()函数修改成generator
def fib1(max):
  n, a, b = 0, 0, 1
  while n < max:
    yield b
    a, b = b, a + b
    n += 1
  return 'done'
# 将print(b)改为yield b
# 这是定义generator的另一种方式  如果一个函数中有yield 那么这个函数就是一个generator函数
# yield的作用是 当generator函数每次执行next()方法的时候，都会执行到yield然后返回 等待下次调用next()方法
# 比如说
def odd():
  print('step 1')
  yield 1
  print('step 2')
  yield 2
  print('step 3')
  yield 3

o = odd()
next(o)
next(o)
next(o)
# 可以看到的是 每次执行next()方法 都会执行到最近的yield的地方 然后等待下次执行next()方法 然后接着往下执行

# 所以对于fib()函数
for n in fib1(5):
  print(n)
# 但是使用for调用generator的时候 是不会得到generator的return值的 因为返回值保存在StopIteration错误的value


