# 数据类型中 字符串很特殊 有一个特别的问题 编码问题
# 由于计算机只能够处理数字 所以需要处理文本的时候，就必须将文本转换成数字 这就是字符编码
# 最先开始是美国人的 ascii码 但是只能够表示127个字符  ascii码 使用一个字节来表示字符
# 但是一个字节表示的字符有限 所以各国就开始有了自己的字符编码
# 类似 中国的 国家标准 gb2313 日本的 shift_jis
# 当多种语言的文本混合出现的时候 就会显示乱码
# 所以 unicode 出现了  unicode把所有的国家语言都编码到一起了
# unicode 通常使用两个字节来表示一个字符  遇到偏僻的字符也会使用四个字符来表示

# unicode 和 ascii 的区别
# 1. ascii 通常是一个字节 而 unicode 通常是两个字节
# 2. 在 unicode 中 对应的ascii的字符编码 通常是将 对应的ascii前面补一个字节的0
# 比如 A:  ascii:01000001  =>  unicode: 00000000 01000001

# 但是好好的凭啥要让英文字符多占一个字节  多占据了一个字节 就表示 传输和存储上要吃亏
# 所以 utf-8 出现了 可变长编码
# utf-8 将每一个unicode字符按照不同的字节 编码成1-6个字节， 
# 1. 常用的英文字母被编码成1个字节
# 2. 汉字通常为3个字节
# 3. 很生僻的字符才会被编译成4-6个字节

# ascii 可以被堪称是 utf-8 的一部分 所以之前使用了ascii的编码可以使用utf-8继续使用

# 所以 明白了编码问题  那么计算机是怎么使用编码的呢？
# 1. 在计算机内存中 统一使用 unicode 编码， 当需要保存到硬盘或者需要传输的时候，就转为utf-8
# 2. 使用编辑器、记事本编辑的时候，从文件读取的 utf-8字符被转为unicode字符到内存中， 当编辑完成之后，再将unicode字符转换成 utf-8保存到文件中
# 3. 浏览网页的时候，服务器把生成的unicode内容转换成utf-8再传输到浏览器中

# 在python3 中 字符串是以 unicode 编码的 即python字符串支持多语言
print('包含中文的字符串')
print('english string')
print('Deutsche Saite')

# 对于单个字符的编码， 
# ord()方法获得字符的整数表示
# chr()方法将对应编码转换成字符
print(ord('a'))
print(ord('中'))
print(chr(98))
print(chr(25991))
# 可以使用 unicode 编码获取对应字符  和直接写字符是等价的
print('\u4e2d\u6587')

# python 中字符串类型是 str 内存中以unicode表示 ，这就表示 一个字符串就要对应很多个字节。
# 那么如果要在网上进行传输或者保存到磁盘上，就必须要把str转变成 以字节为单位的bytes
# 对bytes类型的数据要使用以b前缀的单引号或双引号表示
print(b'abc')
print(b"ABC")

# 需要注意的是，'abc'和b'abc'  前者是str，后者虽然内容显示和前者一样 但是 bytes的每一个字符只占用一个字节
# 使用encode()方法 可以编码为指定的bytes
print('abc'.encode('ascii'))
print('中文'.encode('utf-8'))

# 注意: 纯英文的str 可以使用 ascii编码为bytes 内容是一样的
# 含有中文的可以使用 Utf-8 编码为bytes。 含有中文的不能够使用ascii

# 在bytes中 无法显示的ascii字符的字节 均用 \x## 显示

# 如果从网络或者磁盘中读取了字节流， 那么读到的数据就是 bytes 想要将bytes转换成str 就要使用 decode()方法
print(b'abc'.decode('ascii'))
print(b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8'))
# 注意： 如果遇到了无法解析的字节 decode()会报错 但是可以在decoede()方法中添加 errors='ignore' 来忽略错误的字节
print(b'\xe4\xb8\xad\xff\x96\x87'.decode('utf-8', errors='ignore'))

# 计算str中含有多少个字符 可以使用 len()方法
print(len('abc'))
# 如果对bytes使用len()方法 则会计算所占字节数
print(len('中文'.encode('utf-8')))


# 处理字符串时 经常需要将str和bytes相互转换。 为了避免乱码问题 应该用 utf-8

# 通常会在python源文件的头部加上:
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 第一行是为了告诉 linux/mac 这是一个python可执行程序 windows会忽略掉
# 第二行是为了告诉 python解释器 按照utf-8编码来读取源代码


# 字符串格式化问题  
# 1.和c相同的格式化控制
print('hello,%s' % 'world')
print('you have $%d' % 100)
print('hello, %s. you have $%d' % ('john', 100))
# %d 整数 
# %f 浮点数
# %s 字符串
# %x 十六进制整数...

# 如果不确定应该用什么格式控制符 %s 永远能用
print('age: %s, gener: %s' % (19, True))

# 2. format()方法 类似插值表达式 使用 {0},{1}... 后面跟上类型  使用方法要比格式控制符麻烦得多
print('你好 {0}, 你的成绩提高了 {1:.1f}%'.format('张三', 11.2))


# print('你好,%s,成绩提高了%.5s %%' % ('里斯',(85-72)/72*100))