# 继承和多态
# 在OOP中 当定义一个class的时候 可以从一个现有的类来继承 
# 比如
class Animal(object):
    def run(self):
        print('Animal is running!')

class Dog(Animal):
    pass
class Cat(Animal):
    pass
dog = Dog()
dog.run()
cat = Cat()
cat.run()
# 可以发现 dog和cat类并没有写任何东西 但是却拥有animal的run方法
# 继承最大的好处就是 子类可以获得父类的全部功能
# 当然也可以在子类中增加或者修改一些东西
class Dog1(Animal):
    def run(self):
        print('dog is running!')
    def eat(self):
        print('dog is eatting!')
class Cat1(Animal):
    def run(self):
        print('cat is running!')
    def eat(self):
        print('cat is eatting!')
dog1 = Dog1()
dog1.run()
cat1 = Cat1()
cat1.run()
# 这个时候可以发现 dog和cat执行的就是自己本身的run()方法

# 这就引出了多态的概念
# 这里有一个方法 接收一个animal类型的对象 然后执行run()方法
def run_twice(animal):
    animal.run()
    animal.run()
run_twice(Animal())
run_twice(Dog1())
run_twice(Cat1())
# 可以发现 传入的不管是animal类还是dog，cat类最终都完整的执行出了run()方法
# 就是 无论是哪个子类的实例(dog, cat) 他们都是属于一个父类的(animal)  所以只用按照父类(animal)的类型进行操作就行 只要传入的是父类(animal)或者子类(dog, cat)类型的变量 都会调用实际上对应的方法(dog类型的就执行dog中的run()方法 cat的就执行cat中的run()方法  如果子类中没有 就执行父类(animal)中的run()方法)
# 简单地说就是 只需要知道一个变量是属于某个父类数据类型的变量 然后不用管到底属于哪个子类 只管调用实际方法就行了  具体执行的方法是父类中的还是子类中的 由对象的确切类型来决定  这就是多态真正厉害的地方 调用方只管调用不用管细节


# 静态类型和动态类型
# 对于静态类型语言来讲 例如java  如果需要传入animal类型的参数 那么传入的对象必须是animal类型的或者子类对象的  不然就没办法执行run()方法
# 但是对于动态语言来说 就不一定要传入animal类型 所要做的只是保证传入的对象有一个run()方法就可以了
class Timer(object):
    def run(self):
        print('start..')
run_twice(Timer())
# 可以发现 将timer对象传入 run_twice()方法之后 依旧是完整的执行下来了
# 这就是动态语言中的 鸭子类型 
# 并不要求又严格的继承体系 只要是 看起来像鸭子(和animal类型一样有run()方法) 走路像鸭子(run()方法可以正确执行)  那么它就是鸭子 就可以按照鸭子(animal类型)来使用

