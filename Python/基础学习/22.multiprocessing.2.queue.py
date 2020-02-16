# 进程间的通讯
# 使用 queue 实现进程通讯
# 在父进程中创建两个子进程 一个往queue中写入数据(Queue.put()) 一个从queue中读取数据(Queue.get())
# queue线程安全

from multiprocessing import Process, Queue
import os, time, random

# 往queue中写入数据的进程代码
def write(q):
    print('process to write %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('put %s to queue .' % value)
        q.put(value)
        time.sleep(random.random())
# 读数据进程执行的代码
def read(q):
    print('process to read %s' % os.getpid())
    while 1:
        value = q.get()
        print('get %s from queue.' % value)

if __name__ == '__main__':
    # 在父进程创建queue  并且传入给各个子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动pw进程 写入数据
    pw.start()
    # 启动pr进程 读取数据
    pr.start()
    # 等待pw进程结束
    pw.join()
    # 由于pr读取数据的进程是死循环 所以手动结束进程
    pr.terminate()

