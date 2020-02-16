# dict ： dictionary 其他语言中也叫做 map 使用 Key-value进行存储 具有极快的查找速度
# 使用list实现dict
names = ['Michael', 'Bob', 'Tracy']
scores = [95, 75, 85]
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 可以根据key值添加新的值
d['Adam'] = 67
print(d['Adam'])

# 一个Key值只能对应一个value  如果对已有的key值进行赋值 则会覆盖掉之前的值
d['Jack'] = 90
print(d['Jack'])
d['Jack'] = 60
print(d['Jack'])

# 只能够对存在的key值进行赋值 不然会报错

# 避免key值不存在有两种办法
# 1.使用in判断
print('Thomas' in d)
# 2.使用dict提供的get(key, [return])方法 如果不存在key值 会返回None  或者自定义返回的值
print(d.get('Thomas'))
print(d.get('Thomas', -1))
# 注意 返回 None的时候 python的交互环境不会显示结果

print(d)
# 使用pop(key)方法删除对应的key-value值
d.pop('Bob')
print(d)

# dict的特点
# 1. 查找和插入速度快 不会随着key的增加而变慢
# 2. 需要占用大量内存， 内存浪费多

# list的特点
# 1. 查找和插入的速度随着元素的增加而增加
# 2. 占用空间少 浪费内存少

# 即 dict 使用空间换取时间的方法


# set
# set和dict类似 是一组key的集合 但是不会存储value  set中没有重复的值  set是无序的
# 使用list创建list
s = set([1, 2, 3])
print(s)
# 使用set过滤重复元素
s = set([1, 1, 2, 3, 3, 4])
print(s)
# 使用add(key)方法给set中添加元素
s.add(5)
print(s)
# 使用remove(key)方法删除元素
s.remove(5)
print(s)

# 注意： set是一个无序 无重复元素的集合！

# 使用set实现并集 交集
s1 = set([1, 2, 3])
s2 = set([2, 3, 4])
print(s1 & s2)
print(s1 | s2)


# 注意： dict和set的key值只能是不可变的对象
# 整型和字符串都是不可变对象 可以作为key值
# list是可变 所以不可以作为key值

# 那么可变对象和不可变对象具体区别在哪里呢？
# list是可变对象 对于可变对象进行的任何操作都会最终在可变对象本身显示
l = ['c', 'b', 'a']
print(l)
l.sort()
print(l)
# 但是对于不可变元素
a = 'abc'
print(a.replace('a', 'A'))
print(a)
# 可以看到80返回的字符串同样是改变了的 但是 实际上a的值还是不变 这是为什么呢？
# 要明白的是 a是变量 'abc'才是字符串对象 不变的是a的指向 而不是字符串对象本身
# 对于不可变对象本身进行的任何更改操作 会产生新的对象返回出来 而不是更改自身
b = a.replace('a', 'A')
print(b)
# 这样 就保证了不可变对象永远是不可变的


# t = (1, 2, 3)
# t2 = (1, 2, [1, 2])
# s3 = set(t)
# s4 = set(t2)
# print(s3)
# print(s4)