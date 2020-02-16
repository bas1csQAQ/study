# 在多线程环境下，每个线程都有自己的数据。一个线程使用自己的局部变量比使用全局变量好，因为局部变量只有线程自己能看见，不会影响其他线程，而全局变量的修改必须加锁。
# 但是局部变量也有问题，就是在函数调用的时候，传递起来很麻烦：
# 比如说：
class Student(object):
    pass

def do_subtask_1(std):
    pass

def do_subtask_2(std):
    pass

# 如果使用参数传递呢  这是最容易想到的办法了
def process_student(name):
    std = Student(name)
    # std是局部变量，但是每个函数都要用它，因此必须传进去：
    do_task_1(std)
    do_task_2(std)

def do_task_1(std):
    do_subtask_1(std)
    do_subtask_2(std)

def do_task_2(std):
    do_subtask_2(std)
    do_subtask_2(std)
# 但是函数一层一层的调用会很麻烦  如果使用全局变量也不行 因为每个线程处理的实例对象不同

# 那么 如果使用一个全局的dict存放所有的实例对象 然后用thread作为key获取线程对应的实例对象呢？
global_dict = {}

def std_thread_1(name):
    std = Student(name)
    # 把std放到全局变量global_dict中：
    global_dict[threading.current_thread()] = std
    do_task_1_1()
    do_task_2_1()

def do_task_1_1():
    # 不传入std，而是根据当前线程查找：
    std = global_dict[threading.current_thread()]

def do_task_2_1():
    # 任何函数都可以查找出当前线程的std变量：
    std = global_dict[threading.current_thread()]

# 理论上这么做是可以的 最大的优点是消除了实例对象在每层函数中的传递问题 但是这么取值也太丑了把

# threadLocal就是为了解决这个问题而出现的
import threading
# 创建全局ThreadLocal对象:
local_school = threading.local()


def process_student1():
    # 获取当前线程关联的student:
    std = local_school.student
    print('Hello, %s (in %s)' % (std, threading.current_thread().name))

def process_thread(name):
    # 绑定ThreadLocal的student:
    local_school.student = name
    process_student1()

t1 = threading.Thread(target= process_thread, args=('Alice',), name='Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name='Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()



# 全局变量local_school是一个 ThreadLocal对象 每一个thread都可以对它读写 student属性 但是互不影响
# ThreadLocal解决了参数在一个线程中各个函数之间相互传递的问题



