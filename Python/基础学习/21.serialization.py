# 变量从内存中变成可存储或传输内容的过程 叫做序列化
# python提供的pickle模块用来实现序列化
import pickle
d = dict(name='Bob', age=18, score=89)
print(pickle.dumps(d))
# pickle.dumps()方法把任意对象序列化成一个bytes 然后就可以将这个内容存到文件中
# 或者使用 pickle.dump(obj, file) 将obj序列化之后直接存到file中
f = open('serialization.txt', 'wb')
pickle.dump(d, f)
f.close()

# 如果要将对象从磁盘中读取到内存时 可以使用pickle.loads()方法反序列化出对象
f = open('serialization.txt', 'rb')
d = pickle.load(f)
f.close()
print(d)

# json 是序列化的标准格式
# json类型表示出来就是一个字符串 可以被所有语言读取 也可以很方便的通过网络传输或者存储到磁盘
# 对应类型：
# JSON类型	    Python类型
# {}	        dict
# []	        list
# "string"	    str
# 1234.56	    int或float
# true/false	True/False
# null	        None
# 使用python内置的json模块实现python对象和json格式的转换
import json
d = dict(name='John', age=20, score=88)
# dumps()函数返回有一个str 内容是标准的json格式
# dump()函数将json写入一个文件中
print(json.dumps(d))
# 使用loads()函数 将json字符串反序列化 load()函数从文件中读取字符串并反序列化
json_str = '{"age": 20, "score": 88, "name": "Lisa"}'
print(json.loads(json_str))
# 由于json标准中规定编码为utf-8 python也是 所以这两个总是可以正确的进行转换



# 很多时候 使用class表示对象 
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

# 实例化student对象
s = Student('Bob', 20, 88)
# 将实例对象 序列化
# print(json.dumps(s))
# 会给一个错误 一个实例对象都没办法序列化 这肯定是不合理的
# 这是因为 在默认情况下 dumps()方法不知道该怎么将一个实例对象转换成json对象
# 可以在dumps()函数中增加default参数 参数值是一个转换函数
def student2dict(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }
print(json.dumps(s, default=student2dict))
# 同样的 如果要将一个json反序列化一个student对象 ：传入object_hook参数 参数值是转换函数
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])
print(json.loads(json_str, object_hook=dict2student))

# 但是这么做虽然解决了当前的问题 遇到了另一个实例对象就没办法了 每一个class都要写这么两个转换方法显然是很麻烦的
# 在class实例中通常都有一个 __dict__属性 是用来存储实例变量的 值就是一个dict
# 所以上述序列化可以简写成  要注意的是 有少数是不可以这么写的 比如定义了 __slots__的class
print(json.dumps(s, default=lambda obj: obj.__dict__))



