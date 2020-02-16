# 整数
# 可以处理任意大小的整数，包括负整数 1、100、-80...  有时候也使用方便的十六进制表示
num = 1
print(num)
# 浮点数
# 写法1： 数学写法：1.2、2.3、3.14...
# 写法2： 科学计数法 1.23x109就是1.23e9，或者12.3e8，0.000012可以写成1.2e-5
flo = 1.2
print(flo)
flo1 = 1.2e3
flo2 = 1.2e-4
print(flo1)
print(flo2)
# 注意： 整数运算是准确的(包括整数的除法！！)， 但是浮点数计算可能是不准确的 会有四舍五入之类的误差
# python 中 整数，浮点数没有大小限制  但是浮点数超过一定范围就会显示 inf(无限大)

# 字符串
# 字符串是以单引号'或双引号"括起来的任意文本，
name = 'xiaopangshou'
print(name)
# python 中 同样拥有转义字符 \
print('I\'m ok.')
# 注意： python 中 定义了 r'' 写在单引号中的字符 默认为不转义
print('\\\t\\')
print(r'\\\t\\')
# 注意： 若是有很多行 python 定义了 '''...''' 的形式 表示多行字符
print('''line1
line2
line3
	''')

# 布尔类型
# 真： True
# 假： False

# 布尔值的运算
# and : 与运算 只有运算符两边都是 True  运算结果才是 True
print('and 运算符')
print(True and True)
print(True and False)
print(False and False)
print(5>3 and 3>1)
# or : 或运算 运算符两边有一个 True 运算结果就是 True
print('or 运算符')
print(True or True)
print(True or False)
print(False or False)
print(5>3 or 3>1)
# not ： 是非运算符 是单目运算符 作用是将 True 变为 False 将 False 变为 True
print('not 运算符')
print(not True)
print(not False)

# 布尔类型通常用在if判断的地方
#age = int(input('please input a age:\n'))
#if age >=18:
#	print('adult')
#else:
#	print('teenager')

# 空类型 none
# 注意： none 不等于 0  这是两个不同的值  0 有意义 而 none只是一个空值


# 除此之外 还有 列表 字典等数据类型
# 还可以自定义数据类型
