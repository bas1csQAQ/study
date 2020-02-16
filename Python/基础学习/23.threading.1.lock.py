# 多线程和多进程最大的区别在于：
# 在多进程中 同一个变量会各自有一份拷贝存在每个进程中 互相不会影响
# 但是在多进程中 所有变量都由所有线程共享， 所以任何一个变量都可以被任何一个线程修改
# 因此 线程之间共享数据的最大危险就是在于多个线程同时修改一个变量 让变量内容很乱
# 比如说：
import time, threading

balance = 0
def change_it(n):
    # 将balance 作用域设置为全局
    global balance
    # balance先加后减 应该还是0
    balance = balance + n
    balance = balance - n

def run_thread(n):
    for x in range(100000):
        change_it(n)
# 创建两个线程
t1 = threading.Thread(target=run_thread, args=(5,))
t2 = threading.Thread(target=run_thread, args=(8,))
# 线程启动
t1.start()
t2.start()
# 让程序等待线程执行结束
t1.join()
t2.join()
# 由于线程的调度是由操作系统决定的 当t1,t2交替执行 如果执行次数足够多了之后 balance的结果就不一定是0了
# 多执行几次 看结果
print(balance)

# 原因是因为 高级语言的一条语句在CPU执行时是若干条语句，即使一个简单的计算
# balance = balance + n 也会分成两步
# 1. 计算balance + n 放入临时变量中 
# 2. 将临时变量的值赋值给balance 
# 这两个操作在操作系统的调度下不断的交替执行 就会造成结果和预期不同

# 要保证结果计算正确 那么当一个线程修改balance的时候 其他线程就一定不能执行 change_it()函数
# 所以要做到上面这个 就要给change_it()上一把锁，当某个线程开始执行change_it()时，我们说，该线程因为获得了锁，因此其他线程不能同时执行change_it() 只有当锁被释放之后 其他线程获取了这个锁才能更改
# 由于锁只有一个，无论多少线程，同一时刻最多只有一个线程持有该锁，所以，不会造成修改的冲突。
# 创建一个锁就是通过threading.Lock()来实现：

balance1 = 0
lock = threading.Lock()

def run_thread1(n):
    for i in range(10000):
        # 获取锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()

# 当多个线程同时执行lock.acquire()时，只有一个线程能成功地获取锁，然后继续执行代码，其他线程就继续等待直到获得锁为止
# 注意 用完之后一定要释放锁 不然其他的线程将永远没办法执行 成为死线程

# 锁的好处就是确保了某一段关键代码只能由一个线程从头到尾的执行完毕
# 坏处当然也有 组织了多线程的并发执行 包含锁的代码实际上只能够以单线程模式执行 效率自然就低了
# 其次由于可以存在多个锁 不同的线程持有不同的锁 并试图获取对方持有的锁的时候 就可能会造成死锁， 导致多个线程挂起 不能执行也不能结束 最后只能靠操作系统强制终止














