# 偏函数
# 对于函数而言 通过设定函数的默认值 可以降低函数调用时的难度， 偏函数就是解决这个问题的
# 比如 int()函数可以将传入的字符串转换成证书 默认是默认以十进制转换的 
# 但是如果想要将一个字符串按照二进制来转换的话 就需要加上base属性
print(int('12345'))
print(int('12345', base=8))
print(int('12345', 16))  # 可以省略base=
# 但是 如果当要执行大量的转换的时候 每次都要多传递一个参数就会很麻烦
# 所以： 以二进制为例
def int2(x, base = 2):
  return int(x, base)
# 这个时候 调用int2()函数就可以很方便的进行进制转换了
print(int2('100000'))

# python的functools.partial 用来帮助创建偏函数
import functools
# 可以直接使用函数来直接创建一个新的函数
int8 = functools.partial(int, base=8)
print(int8('67'))

# functools.partial()函数的作用就是将函数的某些参数给固定住（也就是设置默认值），返回一个新的函数，调用这个新函数会更简单


# 会将5加到max函数的参数中 相当于添加了一个比较的数在max函数中
max1 = functools.partial(max, 5)
print(max1(3,4))
