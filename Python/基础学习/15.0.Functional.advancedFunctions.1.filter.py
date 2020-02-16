# filter()函数用于过滤序列。
# filter()函数和map()类似 不同的是会根据返回值的 true或者false决定保留该元素还是丢弃
# 比如
def odd(n):
  return n % 2 == 1
l1 = [1, 2, 3, 4]
lr = filter(odd, l1)
print(list(lr))

#  比如：去除字符串中的空字符串
# str.strip([char]) 作用是去除字符串中的所有空格 \t之类的字符 
# 如果写了参数 那就是去除所有空格\t之类的字符 并且还去除字符串中所有和参数相同的字符
def not_empty(s):
  return s and s.strip()
print(list(filter(not_empty, '123   45')))


# 使用埃及筛法求素数  ??? 
# 构建一个从3开始的数列
def _odd_iter():
  n = 1
  while True:
    n = n + 2
    yield n
# 构建一个判断素数的方法
def _not_divisible(n):
  return lambda x: x % n > 0
# 求素数
def primes():
  yield 2
  it = _odd_iter() # 初始序列
  while True:
    n = next(it) # 返回序列的第一个数
    yield n
    it = filter(_not_divisible(n), it) # 使用filter过滤数列 凡是满足
# 打印20以内的素数:
for n in primes():
  if n < 5:
    print(n)
  else:
    break


# 使用filter()判断回文数
def is_palindrome(n):
  return str(n) == str(n)[::-1]
# 将传递进来的数字强转成str  然后使用切片将字符串翻转  如果翻转过后的和之前的一样 那么就是回文数
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101, 111, 121, 131, 141, 151, 161, 171, 181, 191]:
  print('测试成功!')
else:
  print('测试失败!')