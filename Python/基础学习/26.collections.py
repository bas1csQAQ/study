# 内置模块
# collections是Python内建的一个集合模块，提供了许多有用的集合类

# 1.namedtuple
# namedtuple是一个函数，它用来创建一个自定义的tuple对象，并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。
# 这样一来，用namedtuple可以很方便地定义一种数据类型，它具备tuple的不变性，又可以根据属性来引用，使用十分方便。
# 比如一个点
p = (1, 2)
# 不说明的前提下 很难看出这个是一个坐标点 但是使用一个class又小题大做了 
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x, p.y)

# 比如使用坐标和半径表示一个圆
Circle = namedtuple('Circle', ['x', 'y', 'r'])


# deque
# 使用list存储数据时，按索引访问元素很快，但是插入和删除元素就很慢了，因为list是线性存储，数据量大的时候，插入和删除效率很低
# deque是为了高效实现插入和删除操作的双向列表，适合用于队列和栈
from collections import deque
q = deque(['a', 'b', 'c'])
# 在后面追加元素
q.append('x')
# 在头部追加元素
q.appendleft('y')
print(q)
# 删除末尾的元素
q.pop()
# 删除头部元素
q.popleft()
print(q)


# defaultdict
# 在使用dict中 如果key不存在 就返回默认值
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['key2'])
# 要注意 默认是是调用函数时给的 函数是在创建defaultdict对象是传入的
# 除了在key不在时返回默认值 其他的和dict是一样的


# orderedDict
# 使用dict时 key是无序的 所以在对dict进行迭代的时候 无法确定key的顺序
# 如果要让key又顺序 可以使用orderdict
from collections import OrderedDict
od = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(od)
# orderedDict的key会按照插入的顺序排列 不是按照key本身的排序
od1 = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(list(od1.keys()))

# 使用 orderdict实现一个fifo(先进先出)的dict  当容量超过限制 先删除最早添加的key
class LastUpdatedOrderedDict(OrderedDict):

    def __init__(self, capacity):
        # 是对继承自父类的属性进行初始化。而且是用父类的初始化方法来初始化继承的属性。
        super(LastUpdatedOrderedDict, self).__init__()
        # 在父类orderDict的__init__方法基础上 给LastUpdatedOrderedDict添加了一个_capacity的属性
        self._capacity = capacity

    def __setitem__(self, key, value):
        # 判断这个key有没有在dict中存在 如果存在就是1 执行修改操作  不存在就执行增加操作
        containsKey = 1 if key in self else 0

        if len(self) - containsKey >= self._capacity:
            # popitem()移除键值对并返回 last=true的时候 按照LIFO顺序返回 last=false的时候 按照FIFO顺序返回
            last = self.popitem(last=False)
            print('remove:', last)
        # 如果key值已经存在 就执行修改
        if containsKey:
            del self[key]
            print('set:', (key, value))
        # 不存在就执行增加操作
        else:
            print('add:', (key, value))
        # 调用父类的__setitem__方法写入键值对
        OrderedDict.__setitem__(self, key, value)
m_od = LastUpdatedOrderedDict(2)
m_od['a'] = 1
m_od['b'] = 2
m_od['c'] = 3
print(m_od)


# Counter
# Counter是一个简单的计数器 
# 比如统计字符出现的次数
from collections import Counter
c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)



