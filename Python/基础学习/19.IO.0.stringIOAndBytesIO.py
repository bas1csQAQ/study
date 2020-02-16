# StringIo
# 很多时候 数据的读写不仅仅是文件 也可以在内存中读写
# StringIO是在内存中读写str
# 引入stringIO
from io import StringIO
# 创建stringIO 
f = StringIO()
# 然后像操作文件一样写入文件就好了
f.write('hello')
f.write('world')
# getvalue()用于获取写入后的str
print(f.getvalue())
f.close()
# 读取stringIO
# 使用str初始化stringIO
f = StringIO('hello world !!! \nGood bye!')
# 像操作文件一样读取
while 1:
    s = f.readline()
    if s == '':
        break
    print(s.strip())

# BytesIO
# 使用BytesIO操作二进制数据
# 引入 BytesIO
from io import BytesIO
# 创建bytesIO
f = BytesIO()
# 写入数据
# 注意是写入经过utf-8编码过的二进制数据
f.write('中文'.encode('utf-8'))
# 使用getvalue()获取写入后的内容
print(f.getvalue())
f.close()

# 读取二进制内容
# 使用一个二进制数据初始化bytesIO
f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
f.read()
f.close()