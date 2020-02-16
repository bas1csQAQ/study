# 基本输入
# 使用 input([str]) 可以给变量中输入数据 而不是仅仅的手动赋静态变量了
name = input()
print('name =', name)

# input([str]) 小括号中可以输入提示语句
number = input('please input a number:\n')
print(number)

# 注意： 在python3 中 input([str])方法接收到的值 默认为字符串
# 可以通过数据类型转换来解决类型问题
number1 = int(input('please input a number:\n'))
print(number1)
