# 多任务可以由多进程完成 也可以由一个进程中的多线程完成
# 进程是由若干个线程组成的 一个进程至少由一个线程
# 由于线程是操作系统直接支持的执行单元 所以很多高级语言都内置了多线程的支持
# python中的线程不是模拟出来的线程  而是真正的线程
# python提供了 _thread和 threading两个模块
# 其中_thread是低级模块 threading是高级模块 对_thread进行了封装 
# 线程使用方法和进程大体相同 都是将一个函数传入并创建thread实例 然后调用start()函数开始执行
import time, threading

# 新线程需要执行的代码
def loop():
    # threading.current_thread()会返回当前线程
    print('thread %s is running.' % threading.current_thread().name)
    n = 1
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' % (threading.current_thread().name, n))
        time.sleep(1)
    print('thread %s is ended' % threading.current_thread().name)


# 任何进程默认都会有一个线程 这个线程叫做主线程 主线程又可以启动新的线程
print('thread %s is running' % threading.current_thread().name)
# 在创建线程的时候 给函数和子线程的名字
# 名字没有任何意义 只有打印的时候用来显示 如果不给命名的话 就会默认命名为Thread-1，Thread-2……
t = threading.Thread(target=loop, name='loopThread')
# 启动线程
t.start()
# 等待线程执行结束再执行下面的
t.join()
print('thread %s is ended' % threading.current_thread().name)



