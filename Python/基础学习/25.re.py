# 正则表达式 很重要 非常重要
# 正则表达式是一种用来匹配字符串的强有力的武器。它的设计思想是用一种描述性的语言来给字符串定义一个规则，凡是符合规则的字符串，我们就认为它“匹配”了，否则，该字符串就是不合法的。

# 在正则表达式中 
# 1. 如果直接给出字符 就是精确匹配
# 2. 使用\d 可以匹配一个数字
# 3. 使用\w 可以匹配一个字母或者数字
# 4. 使用. 可以匹配任意字符
# 5. 对于变长的字符 
    # 1. 使用* 表示任意个字符 
    # 2. + 表示至少一个字符 
    # 3. ?表示0或者1个字符 
    # 4. {n} 表示n个字符
    # {n, m} 表示n-m个字符
# 6. 使用[] 表示匹配范围
    # 1. [0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线
    # 2. [0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串
    # 3. [a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串
    # 4. [a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符
# 7. A|B 表示 匹配A或者B
# 8. ^表示行的开头，^\d表示必须以数字开头
# 9. $表示行的结束，\d$表示必须以数字结束

# 所需要注意的是 由于python中的正则表达式是由字符串实现的 但是字符串中有一个转义的问题
# 所以需要使用python的r前缀
# r = r'abc\-001'
# 这样就不用考虑转义的问题了

# 使用re模块判断正则表达式是否匹配
import re
r = r'^\d{3}-\d{3,8}$'
result = re.match(r, '010-12345')
print(result)
result1 = re.match(r, '010 12345')
print(result1)
# 使用match()方法判断是否匹配 如果匹配成功 就会返回一个match对象 不然就会返回None

# 使用正则表达式切分字符串 会比正常的办法更加灵活
print('a b   c'.split(' '))
# 可以发现使用 split()方法分割s字符串的时候 没办法判断连续的空格
# 使用正则表达式切分字符串
# \s是空格
split = re.split(r'\s+', 'a b   c')
print(split)
# 多加一个逗号试试
split1 = re.split(r'[\s|,]+', 'a,b, c  d')
print(split1)
# 再多加一个分号
split2 = re.split(r'[\s|,|;]+', 'a,b;; c  d')
print(split2)
# 可以发现使用正则表达式会更加的方便 简单

# 在正则表达式中使用()来实现分组功能 提取子字符串

result2 = re.match(r'^(\d{3})-(\d{3,8})$', '010-123456')
print(result2)
# 如果在正则表达式中定义了组 那么就可以在返回的match对象中使用group()方法提取出子字符串
# group(0) 永远是原始字符串
print(result2.group(0))
# group(1) 表示第一个子字符串
print(result2.group(1))
# group(2) 表示第二个子字符串
print(result2.group(2))

# 提取字符串很有用 

# 贪婪匹配
# 正则表达式中 默认是贪婪匹配 也就是尽可能多的匹配字符 
# 比如说
result3 = re.match(r'^(\d+)(0*)$', '102300').groups()
print(result3)
# 可以发现 数字全部被\d匹配完了  0*什么都没匹配到 所以返回了一个空字符串
# 所以要想让0*匹配到字符 就必须让\d+进行非贪婪匹配
# 所以加上一个? 就让\d进行了非贪婪匹配
result4 = re.match(r'^(\d+?)(0*)$', '102300').groups()
print(result4)


# 当在python中使用 正则表达式的时候 re模块会在内部做两件事
# 1.编译正则表达式 如果正则表达式写的不合法 就会报错
# 2.使用编译后的正则表达式去匹配字符串

# 所以如果一个正则表达式要使用很多次的时候 出于效率的考虑 可以先预编译这个正则表达式 然后等用的时候拿来直接用就好了
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
result5 = re_telephone.match('010-12345').groups()
print(result5)

# 写一个email的地址验证表达式 
# 判断 xxx@xxx.com 或者 xxx.xxx@xxx.com 格式的email
emailReg = re.compile(r'^([a-z]+)(\.[a-z]+|[a-z]+)@([a-z]+)\.com$')

def is_valid_email(addr):
    if emailReg.match(addr):
        print('true')
    else:
        print('false')
    

is_valid_email('someone@gmail.com')
is_valid_email('bill.gates@microsoft.com')
is_valid_email('bob#example.com')
is_valid_email('mr-bob@example.com')


# 写一个email 把用户名取出来
# <Tom Paris> tom@voyager.org => Tom Paris
# bob@example.com => bob
emailReg1 = re.compile(r'^(.*?)([a-zA-Z\s]+)(.*)$')
def name_of_email(addr):
    res = emailReg1.match(addr)
    if res:
        print(res.group(2))
    else:
        print('false')
name_of_email('<Tom Paris> tom@voyager.org')
name_of_email('tom@voyager.org')
