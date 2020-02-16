#!/usr/bin/env python3
# -*- coding : utf-8 -*-
# task.py for windows
import time, sys, queue, random
from multiprocessing.managers import BaseManager
# 由于是从网络上获取 queue 所以注册时只提供名字就好了
BaseManager.register('get_task')
BaseManager.register('get_result')
# 创建连接 要注意的是地址和验证码要和task_master.py中一致
conn = BaseManager(address = ('127.0.0.1',5002), authkey = b'123')
try:
    # 连接
    conn.connect()
except:
    print('连接失败')
    sys.exit()
# 从网络上获取queue的对象
task = conn.get_task()
result = conn.get_result()
while not task.empty():
    n = task.get(timeout = 1)
    print('run task %d' % n)
    sleeptime = random.randint(0,3)
    time.sleep(sleeptime)
    rt = (n, sleeptime)
    result.put(rt)
if __name__ == '__main__':
    pass