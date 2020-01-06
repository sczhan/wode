
import math
# print(math)
# ceil() 向上取整操作
print(math.ceil(5.05))
print(math.ceil(9.9))
print("*"*20)

# floor() 向下取整操作
print(math.floor(5.01))
print(math.floor(5.9))
print("*"*20)


#  查看系统保留关键字,是不可以用来当做变量命名
import keyword
print(keyword.kwlist)  # 打印系统关键字
print("*"*20)

# round() 四舍五入操作,不是数字模块,是python内置函数
print(round(5.05))
print(round(5.5))
print(round(5.9))
print("*"*20)

# sqrt() 开平方,返回浮点数
print(math.sqrt(4))
print(math.sin(0.5))
print("*"*20)

# pow() 与幂运算差不多,计算一个数的几次方,返回浮点数(两个参数,第一个参数是底数,第二个是指数)
print(math.pow(4, 3))   # 4的3次方
# 幂运算 函数返回浮点型,幂运算返回整型
print(4**3)
print("*"*20)

# fabs() 对一个数值获取它的绝对值,返回浮点数
print(math.fabs(-1))
print(math.fabs(3))
print(math.fabs(0))
print("*"*20)

# abs() 获取绝对值操作,不是数字模块,是python内置函数. 返回值由本身类型而定
print(abs(-1))
print(abs(-2.5))
print(abs(0))
print(abs(4.0))
print("*"*20)

# fsum() 对整个序列求和 返回浮点数
print(math.fsum([1, 7, 8]))
print(math.fsum([1, 7.5, 8]))
print("*"*20)

# sum() python内置求和  返回值由本身类型而定
print(sum([1, 7, 8]))
print(sum([1, 7.5, 8]))
print("*"*20)


# math.modf()  讲一个浮点数拆分为整数部分和小数部分组成元组   小数在前,整数部分在后
print(math.modf(5))
print(math.modf(4.5))
print(math.modf(0))
print(type(math.modf(0)))
print("*"*20)

# copysign() 将第二个数的符号(正负号)传给第一个数    返回第一个数值的浮点数
print(math.copysign(1, -2))
print(math.copysign(-1, 2))
print("*"*20)


# 打印自然是对数e 和 π的值
print(math.e)
print(math.pi)
print("*"*20)


import random
# random() 获取0-1之间的随机小数 包含0不包含1  不可迭代
for i in range(1,11):
    # print(random.random())
    # 随机指定开始和结束之间的值
    print(random.randint(1,9))

print("*"*20)

# random.randrange() 获取指定开始和结束之间的值,可以指定间隔值  不可迭代 range可迭代
for i in range(1,11):
    # print(random.random())
    # 随机指定开始和结束之间的整数值
    print(random.randrange(1, 10, 1))

print("*"*20)


# uniform() 随机获取指定范围内的值(包括小数)
print(random.uniform(1, 9))
print("*"*20)


# choice() 随机获取列表中的值 (元组也可以)
list1 = [1, 2, 3, 5]
tuple1 = (1, 5, 7, 9)
print(random.choice(list1))
print(random.choice([77, 888]))
print(random.choice(tuple1))
print(random.choice((99, 88)))
print("*"*20)


# shuffle() 随机打乱序列, 返回值为空
print(list1)
print(random.shuffle(list1))
print(list1)
print("*"*20)


