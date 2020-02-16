# 使用pipe()实现进程之间的通讯
# Pipe()函数返回一对由管道连接的连接对象，默认情况下是双向的
# pipe()连接的两个对象都有send() 和 recv() 方法(两个对象之间相互之间的)
# 要注意的是 如果两个进程同时尝试读取同一端的数据或者向同一端写入数据 那么pipe中的数据可能会造成损坏
# 当然如果是使用管道的不同端的进程就不会损坏数据 指的是连接在一起的两个进程不在同一时间访问同一端
from multiprocessing import Process, Pipe
import os

def f(conn):
    print('%s send message to the end of the pipe.' % os.getpid())
    # 向管道中写入数据
    conn.send([42, None, 'Hello'])

if __name__ == '__main__':
    # 创建pipe的两端
    parent_conn, child_conn = Pipe()
    # 创建进程 将管道的一端 传入方法 并写入数据
    p = Process(target=f, args=(child_conn,))
    # 写入数据的进程开始执行
    p.start()
    # 在管道另一端 获取数据
    print(parent_conn.recv())
    # 等待进程执行完再往下执行其他的程序
    p.join()