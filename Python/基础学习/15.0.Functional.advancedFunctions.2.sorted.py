# 排序算法
# 排序的核心是比较两个元素的大小
# 内置函数  sorted()
# sorted(iterable, *, key=None, reverse=False)
# key 指定带有单个参数的函数，用于从 iterable 的每个元素中提取用于比较的键 (例如 key=str.lower)。 默认值为 None (直接比较元素)。
# reverse 为一个布尔值。 如果设为 True，则每个列表元素将按反向顺序比较进行排序。
l = sorted([36, 5, -12, 9, -21])
print(l)
# 接收一个key函数来实现自定义的排序
# key指定的函数会作用在list中的每一个元素 然后根据key函数返回的结果进行比较
l1 = sorted([36, 5, -12, 9, -21], key = abs)
print(l1)

# 对于字符串
# 默认情况下是按照ascii比较的
l2 = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(l2)
# 现在传入key函数  比如说传入lower()函数 用于忽略大小写
l3 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(l3)

# 如果想要实现反向排序 需要设置第三个参数
l4 = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(l4)


# 有一个tuple 要求实现按照名字进行排序
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
  return t[0]
def by_score(t):
  return t[1]
l5 = sorted(L, key=by_name)
l6 = sorted(L, key=by_score)
print(l5)
print(l6)

l7 = sorted(L, key=lambda x: x[0])
l8 = sorted(L, key=lambda x: x[1])
print(l7)
print(l8)