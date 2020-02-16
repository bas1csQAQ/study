# 一个任务就是一个进程 progress
# 一个进程中可能不只做一件事 比如说word 可以同时进行打字 拼写检查 等事情 这些进程中的子任务 就叫做线程
# 如果想要同时执行多个任务要怎么办
# 1. 一种是启动多个进程，每个进程虽然只有一个线程，但多个进程可以一块执行多个任务。
# 2.一种方法是启动一个进程，在一个进程内启动多个线程，这样，多个线程也可以一块执行多个任务。
# 3.第三种方法，就是启动多个进程，每个进程再启动多个线程，这样同时执行的任务就更多了，当然这种模型更复杂，实际很少采用

# 使用multiprocessing模块实现多平台的多进程支持(由于操作系统的不同而造成的 unix/linux可以直接调用os模块中的fork()函数创建进程 但是windows不行)
from multiprocessing import Process
import os

# 子进程需要执行的代码
def run_proc(name):
    # pid 相当于子进程的id
    print('run child process %s (%s)' % (name, os.getpid()))

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    # 创建一个process实例 只需要传入要执行的函数和函数的参数
    p = Process(target=run_proc, args=('test',))
    print('child process will start')
    # 使用start()函数启动进程
    p.start()
    # join()用于等待子进程执行结束之后在继续往下运行 通常用于进程之间的同步
    p.join()
    print('child process end')

