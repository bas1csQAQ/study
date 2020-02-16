# 使用os模块 可以操作目录和文件
import os
# 操作系统类型
# nt 说明系统是windows
# posix 说明系统是Linux、Unix或Mac OS X
print(os.name)

# 如果要获取更详细的系统信息 可以使用 uname()函数 windows上没有这个函数
# 也就是说 os中有些函数是跟操作系统相关的

# 使用environ变量显示环境变量
print(os.environ)
# 使用os.environ.get(key) 可以获取对应key值的环境变量
print(os.environ.get('PATH'))

# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中 一部分放在os.path模块中
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 将两个路径拼接的时候 需要使用 os.path.join()函数  这样的话可以正确处理不同操作系统的路径分隔符
# Linux/Unix/Mac下，os.path.join()返回 part-1/part-2
# Windows下会返回 part-1\part-2
print(os.path.join('E:\\workSpace\\python', 'testdir'))
# 使用mkdir()函数创建目录
os.mkdir('E:\\workSpace\\python\\testdir')
# 使用rmdir()函数删除一个目录
os.rmdir('E:\\workSpace\\python\\testdir')

# 使用os.path.split()函数拆分路径 会将路径拆分为两部分 后一部分总是最后级别的目录或者文件名
print(os.path.split('E:\\workSpace\\python\\testdir'))
# 使用os.path.splitext()函数可以直接得到文件扩展名
print(os.path.splitext('E:\\workSpace\\python\\testdir\\hello.txt'))
# 要注意的是 以上这些合并 拆分路径的函数并不要求目录和文件真实存在 只是对字符串的操作罢了

# 使用 os.rename(filename1, filename2) 来对文件进行重命名 表示将filename1 改为 filename2
# os.rename('testOS.txt', 'testOS.py')
# 使用 os.remove(filename) 删除文件
# os.remove('testOS.py')

# 但是 os模块中居然没有 复制文件的函数
# 所幸在shutil模块中中有copyfile(src, dst)的函数  src和dst都是以字符串形式给出的路径名 dst必须是完整的目标文件名而且必须给出 如果路径文件已经存在 就会将原来的文件覆盖掉
# 在shutil模块中还有很多使用的函数 

# 使用python特性过滤文件 比如要列出当前目录下的所有目录
# print(os.listdir('.'))
# for x in os.listdir('.'):
#     if os.path.isdir(x):
#         print(x)
dirlist = [x for x in os.listdir() if os.path.isdir(x)]
print(dirlist)
# 列出所有的.py文件
pyfilelist = [x for x in os.listdir() if os.path.isfile(x) and os.path.splitext(x)[1] == '.py']
print(pyfilelist)
