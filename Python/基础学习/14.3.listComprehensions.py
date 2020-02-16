# 列表生成式List Comprehensions 是一种简单但强大的list生成式
# 比如说 想要生成一个 1-10的list
# 可以这样
l = list(range(1, 11))
print(l)
# 但是如果要生成 1*1, 2*2, 3*3...10*10呢？
# 当然可以使用循环实现
l1 = []
for x in range(1, 11):
  l1.append(x * x)
print(l1)
# 但是使用循环 无疑是繁琐的
# 列表生成式就是为了解决这个问题：
# 其中 将要生成的元素写在最前面 后面跟上for循环 就可以把list创建出来
# 要注意的是 for循环中的变量必须要和前面生成的元素使用的变量相同  即 x*x 要和 for x in range(1, 11) 
l2 = [x * x for x in range(1, 11)]
print(l2)
# for循环后面还可以加上if判断
l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)
# 还可以多层循环
l4 = [m + n for m in 'ABC' for n in 'XYZ']
print(l4)


# 小的应用  引入os模块
import os
# 使用os模块中的 listdir 列出当前列表的文件和目录
l5 = [d for d in os.listdir('.')] 
print(l5)

# 就像for循环可以使用两个变量一样
d = {'x': 'A', 'y': 'B', 'z': 'C' }
l6 = [k + '=' + v for k, v in d.items()]
print(l6)

# 可以使用lower()方法将字符串改为小写  upper()方法大写  
# 注意 lower()和upper()只对字符串起作用
L = ['Hello', 'World', 'IBM', 'Apple']
l7 = [s.upper() for s in L]
l8 = [s.lower() for s in L]
print(l7)
print(l8)

# 编写函数 使含有字符串和整数的list 中的字符串全部传为小写
# 可以使用 内置函数 isinstance(obj, type)判断是否是字符串
L1 = ['Hello', 'World', 18, 'Apple', None]
l9 = [s.lower() for s in L1 if isinstance(s, str)]
print(l9)
