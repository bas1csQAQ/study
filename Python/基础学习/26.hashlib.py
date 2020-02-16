# 摘要算法
# 摘要算法又称哈希算法、散列算法。它通过一个函数，把任意长度的数据转换为一个长度固定的数据串（通常用16进制的字符串表示）
# 摘要算法就是通过摘要函数f()对任意长度的数据data计算出固定长度的摘要digest

import hashlib
# 其中最常见的就是 MD5
md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

# 如果数据量大 也可以分块多次调用update()方法 结果是一样的
md5_1 = hashlib.md5()
md5_1.update('how to use md5 in '.encode('utf-8'))
md5_1.update('python hashlib?'.encode('utf-8'))
print(md5_1.hexdigest())

# md5是最常见的摘要算法 速度很快，生成结果是固定的128 bit字节，通常用一个32位的16进制字符串表示
# 另一种常见的摘要算法是 sha1
sha1 = hashlib.sha1()
sha1.update('how to use sha1 in '.encode('utf-8'))
sha1.update('python hashlib?'.encode('utf-8'))
print(sha1.hexdigest())
# SHA1的结果是160 bit字节，通常用一个40位的16进制字符串表示
# 比SHA1更安全的算法是SHA256和SHA512，不过越安全的算法不仅越慢，而且摘要长度更长

# 设计一个验证用户登录的函数 根据用户输入的口令是否正确 返回true或者false
db = {
    'michael': 'e10adc3949ba59abbe56e057f20f883e',
    'bob': '878ef96e86145580c38c87f0410ad153',
    'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if db[user] == md5.hexdigest():
        print('true')
    else:
        print('false')
login('michael', '123456')
login('bob', 'abc999')
login('alice', 'alice2008')
login('michael', '1234567')


# 那么是否采用了md5加密密码之后 就一定安全了呢?
# 当然不是 很多用户还是喜欢用 123456 这种简单口令作为密码 所以只要拿同样的摘要算法算出密码之后 就可以找到这些简单密码的账号了
# 所以 在使用md5的时候 会采用 加盐 的办法来
# 这一方法通过对原始口令加一个复杂字符串来实现
# 这样 只要盐不被黑客知道 那么即使是简单的密码 也很难通过md5反推明文口令
import random
# 返回md5密文函数
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

class User(object):
    def __init__(self, username, password):
        self.username = username
        # 使用随机数把盐设置出来
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        # 使用加盐的办法来加密密码明文口令
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}

# 修改login函数 根据修改后的md5算法实现用户登录验证
def login1(username, password):
    user = db[username]
    print(user.salt, user.password)
    if user.password == get_md5(password + user.salt):
        print('true')
    else:
        print('false')

login1('michael', '123456')




