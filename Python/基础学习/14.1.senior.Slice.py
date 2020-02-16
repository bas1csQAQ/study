# 切片
# 想要取出一个tuple或者list的部分元素是很常见的操作
L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
# 现在有一个list 需要取出前3个元素
print([L[0], L[1], L[2]])
# 这样虽然是完成了上述任务 但是没有任何扩展 如果要取前4个元素 就只能重新写了
# 所以稍微扩展一下 取出索引为0-N-1的元素
r = []
n = 3
for i in range(n):
  r.append(L[i])
print(r)
# 这样就只用修改n的值就可以适应这种大部分的操作了
# 但是 我们可能要经常这么做 所以使用循环写的未免也太麻烦了

# python提供切片 slice操作符 可以大大的简化这种操作
# L[0:2]表示从索引为0的元素开始 到索引为2的为止不包括索引为2的元素
print(L[0:2])
# 如果第一个索引为0的话 还可以省略0
print(L[:4])
# 可以从任何list中有的索引开始
print(L[1:3])

# python支持倒数取元素
# 同样的 python也支持倒数切片  
# 注意 倒数第一个元素的索引值是 -1
print(L[-1:])
# 和正数切片一样的 L[-3:-1]表示的是从倒数第3个元素开始 截取到倒数第1个元素  不包括倒数第1个元素
print(L[-3:-1])

# 切片很有用
# 这是一个0-99的list
L1 = list(range(100))
print(L1)

# 取出前10个元素
print(L1[:10])
# 取出后10个元素
print(L1[-10:])
# 取出11-20的元素  第11个元素的下标是10  所以从10开始截取 一直截取到20之前
print(L1[10:20])

# 同样的 slice中还有步长功能
# L1[:10:2]表示前10个元素 每两个取一个
print(L1[:10:2])
# L1[::5] 所有元素 每五个取一个
print(L1[::5])

# 只有一个冒号 可以原样复制一个list
print(L1[:])

# tuple也可以进行slice操作  只不过返回值依旧是一个tuple
t = tuple((range(10)))
print(t[:5])

# 字符串也可以看作是list 其中每一个字符就是一个元素
s = 'ABCDEFG'
print(s[:3])


# 编写一个函数 实现取出字符串头尾的空格
# 例如 'hello   '  ->  'hello'
#      '   hello'  ->  'hello'
#      '  hello  ' ->  'hello'

def trim(s):
  while s[:1] == ' ':
    s = s[1:]
  while s[-1:] == ' ':
    s = s[:-1]
  return s

if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
