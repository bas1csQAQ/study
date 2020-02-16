# 调试程序的方法

# 1.将有可能出错的变量打印出来
def foo(s):
    n = int(s)
    print('>>> n = %d' % n)
    return 10 / n

def main():
    foo('0')

# main()
# 但是这么做会导致运行结果中有很多垃圾信息 而且在最后还要将print()全部删掉

# 断言
# 在所有使用print()的地方使用assert代替
def foo1(s):
    n = int(s)
    assert n != 0, 'n is zero!'
    return 10 / n

def main1():
    foo1('0')
# main1()
# assert的意思是，表达式n != 0应该是True，否则，根据程序运行的逻辑，后面的代码肯定会出错
# 如果断言失败 则assert语句本身就会抛出异常
# 但是如果到处都是断言 那么运行结果和print()相比也不会好到哪里  
# 可以在启动python解释器的时候 增加 -O参数来关闭assert  (英语大写字母o)  python -O 18.debug.py

print('----------------------------------------------------')
# logging
# 将所有使用print()的地方替换成 logging 和断言相比 logging不会排除错误 而且还可以输出到文件
import logging
# 设置日志基本配置 
# filename表示日志输出文件位置 也可以不设置 不设置日志输出文件位置的时候 默认会在控制台输出
# level 设置日志输出信息类别 分为debug，info，warning，error等几个级别 当指定了类别之后其他的都没用了 这样就可以控制输出不同级别的信息 
logging.basicConfig(filename='example.log', level=logging.INFO)
s = '2'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)

# python调试器pdb  让程序以单步方式运行 可以随时查看运行状态
# 以参数-m pdb启动后(python -m pdb 文件名)，pdb将定位到下一步要执行的代码。
# 输入命令l来查看代码
# 输入命令n可以单步执行代码
# 任何时候都可以输入命令p 变量名来查看变量
# 输入命令q结束调试，退出程序

# 这么做理论上是万能的 但是如果代码很多 这个就不适用了 所以还有另一种断点方法
# 引入 pdb模块
import pdb
# 之后在任何可能出错的地方 放上一个 pdb.set_trace() 就可以设置一个断点
# 这样在程序执行的时候 会在断点处停止执行 并进入pdb调试环境 可以使用p命令查看变量 c命令继续运行
# 这个方法比直接启动pdb但不调试效率高不少
s = '0'
n = int(s)
pdb.set_trace() # 运行到这里会自动暂停
print(10 / n)
