# 计算机之所以能够实现自动化 是因为可以做条件判断
age = 20
if age>=18:
  # print('your age is %d' % age)
  print('your age is', age)
  print('adult')
# 按照python的缩进规则 如果条件表达式的值为True 就会执行 缩进两个空格的语句执行

# elif 是 else if 的缩写
age = 3
if age >= 18:
  print('adult')
elif age >= 6:
  print('teenager')
else:
  print('kid')