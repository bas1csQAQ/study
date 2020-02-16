# 使用进程池的方式批量创建子进程
from multiprocessing import Pool
import os, time, random

def long_time_task(name):
    print('run task %s (%s)' % (name, os.getpid()))
    # 进程开始时间记录
    start = time.time()
    # 时间sleep 给程序一个假的执行时间
    time.sleep(random.random() * 3)
    # 进程结束时间记录
    end = time.time()
    print('task %s run %.2f seconds' % (name, (end - start)))

if __name__ == '__main__':
    print('parent process %s' % os.getpid())
    # 创建一个
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('wating for all subprocesses done.')
    # 调用close()方法 关闭进程池 表示不再添加新的进程
    p.close()
    # 调用join()方法表示会等进程池中的所有子进程执行完毕之后 才会往后执行
    p.join()
    print('all subprocesses done')

# 在执行结果可以发现 进程0 1 2 3是同时执行的 但是进程4却不是 4是在等前面有一个执行结束之后 再加入执行队列的
# 这是因为设置进程池的时候 设置的是4 也就是说同时可以跑4个进程 这是由于pool的设置而造成的限制 而并不是操作系统的显示
# 如果将 进程池设置的部分 改为 p = Pool(5) 就不会出现这种情况了





