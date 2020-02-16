# 在程序运行中 如果发生了错误 可以实现约定返回一个错误代码 这样就知道是否出错 以及出错的原因
# 这种返回错误代码的操作很常见  例如打开文件的open()函数 成功时返回的是文件描述符(一个整数) 出错时返回的是-1
# 但是 使用错误代码来表示是否出错很不方便 使用错误代码就会造成使用大量的代码来进行判断
# 所以在高级语言中 一般都会内置try-except-finally一类的错误处理机制
# 比如说
try:
    print('try...')
    r = 10 / 0
    print('result:', r)
except ZeroDivisionError as e:
    print('except:', e)
finally:
    print('finally...')
print('END')
# 很明显这个程序是错的
# 发现print('result:', r)没有执行 这是因为在上一行发现出错 然后所以捕捉到错误执行了except中的代码 再之后执行了必须要执行的finally
# 如果说没有错误发生就不会执行except中的内容

# 当然 错误可以有很多种类 自然也该有多种不同的错误捕捉语句块来处理
try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')

# 如果没有错误发生 可以在except语句块后加一个else 表示当try中没有发生错误的时候 执行的语句
try:
    print('try...')
    r = 10 / int('2')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
else:
    print('no error!')
finally:
    print('finally...')
print('END')

# 要注意的是 python中的错误其实也是class 所有的错误类型全部都继承自baseException 所以在使用except的时候，不仅仅捕捉的是该类型的错误 还会把子类型全部捕获
try:
    pass
except ValueError as e:
    print('ValueError')
except UnicodeError as e:
    print('UnicodeError')
# 在这个例子中 第二个异常永远不可能捕获到 因为UnicodeError是ValueError的子类 就算报错 也会被第一个except捕获到

# 使用try-except还有一个巨大的好处  可以跨越多层调用，比如下面这个例子 在main()函数中调用bar()函数 异常捕获在main()中 无论是哪个调用的函数出错了 都会被捕捉到
def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except Exception as e:
        print('Error:', e)
    finally:
        print('finally...')
main()
# 也就是说 不需要再每一个可能出错的位置捕获异常 只需要在合适的地方进行捕获就好了 这样也减少了大量写try...except...finally的麻烦

print('--------------------------------------')
# 不捕获异常 打开注释 观察报错 学会看报错
# bar('0')

# 如果不捕获异常 虽然说可以让解释器打印出错误栈 但是程序执行也就结束了
# 可以使用内置的logging模块来记录错误信息
import logging

def main1():
    try:
        bar('0')
    except Exception as e:
        logging.exception(e)
main1()
# 可以发现 程序依旧是打印了错误信息 但是程序还是执行下去了 并且正常退出 

# 使用raise 抛出异常 有的时候，可以根据自己的需要手动创建一个错误class  当在需要的时候手动抛出错误
# raise如果不带参数 就会把当前错误重复抛出
# 选择好继承关系
class FooError(ValueError):
    pass

def foo1(s):
    n = int(s)
    if n==0:
        raise FooError('invalid value: %s' % s)
    return 10 / n

foo1('0')
# 当执行的时候 可以追踪到自己定义的错误
# 当然 只有特殊情况下需要定义错误类型的时候才会手动写一个错误类型  大多时候还是尽量要使用内置的错误类型

# 可以将except和raise一起用 但是必须是合理的转换  
# 比如说不能将IOError转换成毫不相关的ValueError
try:
    10 / 0
except ZeroDivisionError:
    raise ValueError('input error!')



