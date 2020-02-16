#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# master.py for windows

# 在Thread和Process中，应当优选Process，因为Process更稳定，而且，Process可以分布到多台机器上，而Thread最多只能分布到同一台机器的多个CPU上。
# Python的multiprocessing模块不但支持多进程，其中managers子模块还支持把多进程分布到多台机器上。一个服务进程可以作为调度者，将任务分布到其他多个进程中，依靠网络通信。由于managers模块封装很好，不必了解网络通信的细节，就可以很容易地编写分布式多进程程序。
# 分布式很重要 非常重要
# 先启动master.py 在启动worker.py

import time,queue
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support
#任务个数
task_number = 10
#定义收发队列
task_queue = queue.Queue(task_number)
result_queue = queue.Queue(task_number)
def gettask():
    return task_queue
def getresult():
     return result_queue
def test():
    #windows下绑定调用接口不能使用lambda，所以只能先定义函数再绑定
    # 将两个Queue都注册到网络上
    BaseManager.register('get_task',callable = gettask)
    BaseManager.register('get_result',callable = getresult)
    #绑定端口并设置验证码，windows下需要填写ip地址，linux下不填默认为本地
    manager = BaseManager(address = ('127.0.0.1',5002),authkey = b'123')
    #启动
    manager.start()
    try:
        #通过网络获取任务队列和结果队列
        task = manager.get_task()
        result = manager.get_result()
        #添加任务
        for i in range(task_number):
            print('Put task %d...' % i)
            # 将任务内容放到queue中 
            task.put(i)
        #每秒检测一次是否所有任务都被执行完
        while not result.full():
            time.sleep(1)
        for i in range(result.qsize()):
            ans = result.get()
            print('task %d is finish , runtime:%d s' % ans)
    
    except:
        print('Manager error')
    finally:
        #一定要关闭，否则会报管道未关闭的错误
        manager.shutdown()
        
if __name__ == '__main__':
    #windows下多进程可能会炸，添加这句可以缓解
    freeze_support()
    test()