# Base64是一种用64个字符来表示任意二进制数据的方法。 任意二进制到文本字符串的编码方法 
# Base64永远是4的倍数 不够的话要在最后加上=来把Base64字符串的长度变为4的倍数  才可以正常解码
# 将需要解码的字符串转换为 bytes 类型，在末尾添加 = 号使其为4的倍数
# 在进行编码的时候 很多Base64会把后面的=删除  
import base64



# 编码
print(base64.b64encode(b'binary\x00string'))
# 解码
base64.b64decode(b'YmluYXJ5AHN0cmluZw==')


# 由于标准的Base64编码后可能出现字符+和/，在URL中就不能直接作为参数，所以又有一种"url safe"的base64编码，其实就是把字符+和/分别变成-和_
print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode('abcd--__'))



# 写一个能处理去掉=的base64解码函数

def safe_base64_decode(s):
    if len(s) % 4 != 0:
        s = s + b'=' * (4 - len(s) % 4)
    return base64.b64decode(s)
# print(safe_base64_decode(b'YWJjZA=='))