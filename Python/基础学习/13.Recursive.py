# 递归函数
# 在函数内部，可以调用其他函数。如果一个函数在内部调用自身本身，这个函数就是递归函数。
# 如果说 设计函数 求n的阶乘
def fun(n):
  if n == 1:
    return 1
  return n * fun(n-1)
print(fun(5))
# 理论上 所有的递归都可以写成循环的形式，只不过循环看着不清晰

# 注意： 使用递归需要注意防止栈溢出
# 计算机中 函数调用是通过栈来实现的  每一层调用都会增加一个栈 每当函数返回都会减少一个栈
# 由于 栈的大小不是无限的 所以当递归次数过多时 就会造成栈溢出
# 比如：
# print(fun(1000)) 

# 那么怎么才能解决栈溢出的问题呢？
# 使用尾递归进行优化
# 尾递归：在函数返回的时候 调用自己 并且 return 不能含有表达式  
# 这样的话编译器或者解释器在运行的时候就会进行优化 使不管递归调用几次 都只会占据一个栈 就不可能出现栈溢出的问题了
# 上述 fun 方法 由于 return中n * fun(n-1) 有乘法表达式 所以不是尾递归
def fun1(n):
  return fun2(n, 1)

def fun2(n, product):
  if n == 1:
    return product
  return fun2(n - 1, n * product)
# 将上述代码改为以上形式 就是尾递归了 思路是将每一步的阶乘 传递到函数中
# fun2函数中的 return n-1 和 n*product 都是在递归调用之前就执行的 所以是尾递归 不会有栈溢出的问题
print(fun1(100))


# 编写递归函数 实现汉诺塔
def move(n, a, b, c):
  if n == 1:
    print(a, '-->', c)
  else:
    move(n - 1, a, c, b)
    print(a, '-->', c)
    move(n - 1, b, a, c)
move(3, 'a', 'b', 'c')
