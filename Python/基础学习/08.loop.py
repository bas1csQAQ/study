# 循环
# 1. for in 用于将list或者tuple中的每个元素遍历出来
names = ['Michael', 'Bob', 'Tracy']
for name in names:
  print(name)

# range()方法用于返回一个整数数列 然后在转为list类型就可以得到一个0到参数范围的整数list了
print(list(range(5)))

#计算0-100的和
sum = 0
for x in range(101):
  sum += x
print(sum)

# 2.while 循环。当条件满足的时候 就一直循环 不满足时就退出
# 计算100以内奇数和
sum = 0
n = 99
while n > 0:
  sum += n
  n -= 2
print(sum)

# break 用于提前退出循环
# 输出 1-5
n = 1
while n <= 5:
  print(n)
  n += 1
print('end')
# 使用break提前结束循环
n = 1
while n <= 5:
  if n > 3:
    break
  print(n)
  n += 1
print('end')

# continue 使用continue跳出本次循环
# 输出打印0-5
n = 0
while n < 5:
  n += 1
  print(n)
print('end')
# 只输出能够被2整除的
n = 0
while n < 5:
  n += 1
  if n % 2 != 0:
    continue
  print(n)
print('end')


# 注意： continue 和break 虽然好用 但是会造成逻辑分叉过多 而造成不必要的错误 
# 更改逻辑判断就可以解决的问题 尽量修改逻辑判断