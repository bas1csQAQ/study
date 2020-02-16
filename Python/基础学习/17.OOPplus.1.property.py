# 在给实例绑定属性的时候 虽然直接使用属性写起来简单 但是这也造成了 属性值可以被随意更改的问题
class Student(object):
    pass
s = Student()
s.score = 999
# 这显然不符合逻辑 所以为了能够对属性值进行判断 或者说进行限制 可以通过方法来实现赋值和取值
class Student1(object):
    def get_score(self):
        return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise 'score must be integer'
        if value < 0 or value > 100:
            raise 'score must between 0 ~ 100'
        self._score = value
# 现在对任意的实例对象进行操作都可以不用担心被随意设置属性值了
s1 = Student1()
s1.set_score(20)
print(s1.get_score())

# 但是这又延伸了一个新的问题 使用方法来设置和调用又显得复杂 没有使用属性方便
# 所以为了偷懒设计了 @property 
# 这是一个内置的装饰器 作用是将一个方法作为属性调用
class Student2(object):
    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
# 将一个getter方法变成属性调用 就加@property就够了 在同时还会生成一个装饰器 @score.setter 作用是将一个setter方法变成属性赋值
s2 = Student2()
s2.score = 90
print(s2.score)
# 这样就得到了一个 可控的属性操作

# 如果值设置 getter方法 而不设置 setter方法 那么这个属性就是只读属性
class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth
# 例如 age就是只读属性 而birth就是可读写属性

# @property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。

# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution
class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self, value):
        self._width = value
    @property
    def height(self):
        return self._height
    @height.setter
    def height(self, value):
        self._height = value
    @property
    def resolution(self):
        return self._width * self._height
