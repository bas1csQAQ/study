# list 列表类型  有序的集合 可以随时增加删除其中的元素
classmate = ['Bob', 'Tracy', 'John']
print(classmate)
# 对list类型的元素使用len()方法可以获得list的元素个数
print(len(classmate))
# 同样的 使用索引值来访问每一个位置的元素  索引值从0开始  要注意索引越界问题
print(classmate[0])
print(classmate[1])
print(classmate[2])
# 如果要获取倒数第几个元素 可以：
print(classmate[-1])
print(classmate[-2])
print(classmate[-3])
# 使用append() 方法向list中追加元素 追加的元素在list末尾
classmate.append('adam')
print(classmate)
# 使用insert()方法将元素插入到list的指定的位置
classmate.insert(1, 'Jack')
print(classmate)
# 使用pop()方法删除list末尾的元素
classmate.pop()
print(classmate)
# 在pop()方法中添加索引值参数 删除对应索引位置的元素
classmate.pop(1)
print(classmate)
# 替换list中的元素内容
# 直接向对应索引位置赋值
classmate[0] = 'Sarah'
print(classmate)


# 注意：list中的元素的数据类型可以不相同
l = ['apple', 11, True]
# list元素也可以是另一个list
l1 = ['python', 'java', ['php', 'asp'], 'scheme']
print(len(l1))
print(l1[2][0])

# 注意： 如果一个list中没有任何元素， 那么这就是一个空list  长度是0
l2 = []
print(len(l2))


# tuple
# 也是一种有序列表 和list很像 不同的是 tuple 一旦初始化就不能够修改了
classmate1 = ('Bob', 'Tracy', 'John')
print(classmate1)
# 同样的 可以使用 索引值获得对应位置的元素 但是不能够赋值了
# 由于tuple不可变了 所以就安全了 所以在能够使用tuple的地方 尽量使用 tuple 而不是list

# 注意： 
# 1.tuple在定义的时候 就必须要初始化
t = (1, 2)
# 2.定义一个空的tuple 
t1 = ()
# 3.定义只有一个元素的tuple 必须要加一个逗号 ，
# 这是因为小括号同时也是数学公式中的计算 ， 在这种情况不明的时候 python会将小括号识别为数学计算
# 如果不加逗号的话 就会定义一个整型的变量 而不是一个tuple
t2 = (1,)

# 注意： tuple说的不变说的是 tuple中每个元素的指向不变 
t3 = ('a', 'b', ['A', 'B'])
print(t3)
# 例如这个 t3[2]指向的是一个数组 那么就不能够再指向其他的东西了 但是指向的数组还是可变的
t3[2][0] = 'X'
t3[2][1] = 'Y'
print(t3)




