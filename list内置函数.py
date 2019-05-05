
# sort()排序,从小到大
list12 = [1, 5, 7, 4, 3]
print(list12.sort())
print(list12)
print(list12.sort(reverse=True))
print(list12)
print("*"*20)


# 元组内建函数

# count() 计算某个元素在元组中出现的次数
tuple1 = (3, 5, 7, 9, 3)
print(tuple1.count(3))
print("*"*20)

# index() 获取值在元组中的索引
print(tuple1.index(5))
print(tuple1.index(3, 2, 5))
print("*"*20)


# 字典内建函数

# clear() 清除整个字典
dict1 = {"one": 1, "two": 2}
print(dict1)
dict1.clear()
print(dict1)
print("*"*20)

# copy()复制字典
dict2 = {"1": "one", "two": 2}
dict3 = dict2.copy()
print(dict2)
print("*"*20)

# fromkeys() 按照指定的序列为键创建字典,值都是一样的
list13 = ["a", "b", "c"]
dict4 = dict.fromkeys(list13, 2)
dict5 = {}.fromkeys(list13)
print(dict4)
print(dict5)
print("*"*20)

# get()根据键获取指定的值 找不到的键如果设置默认值则返回默认值,如果没设置默认值,则返回None
dict6 = {"a": 1, "b": 2, "c": 3}
print(dict6.get("a"))
print(dict6.get("d"))
print(dict6.get("d", 4))
print("*"*20)

# items() 将字典变成类似于元组的形式方便遍历
dict6 = {"a": 1, "b": 2, "c": 3}
for k, v in dict6.items():
    print(k, v)
print(dict6.items())
print("*"*20)

# keys() 遍历字典中的键
# values() 遍历字典中的值

# pop 移除字典中指定元素 返回键对应的值,如果键不存在,则返回默认值,如果键找不到,也没设默认值,会报错
dict6 = {"a": 1, "b": 2, "c": 3}
c = dict6.pop("a")
print(c)
print(dict6)
print(dict6.pop("d", 4))
# print(dict6.pop("d"))  报错
print("*"*20)

# popitem() 移除字典的键值对 返回移除的键值对
dict7 = {"k": 5, "h": 7, "j": 9}
print(dict7.popitem())
print(dict7)
print("*"*20)

# setdefault() 在字典中添加元素
dict7 = {"k": 5, "h": 7, "j": 9}
print(dict7.setdefault("o", 10))
print(dict7)
print("*"*20)

# update() 修改字典中的值 返回None
dict7 = {"k": 5, "h": 7, "j": 9}
dict7.update({"k": 15, "h": 18})
print(dict7)
print(dict7.update({"k": 78}))
print(dict7)
print("*"*20)


# 集合内建函数
a = set()
print(a)
print(type(a))
list14 = [1, 5, 7]
a2 = set(list14)
print(a2)
print(type(a2))
print("*"*20)

# add() 向集合中添加元素
set1 = {1, 7, 8}
set1.add(66)
print(set1)
print(set1.add(6))
print(set1)
print("*"*20)

# clear() 清空集合
# copy() 复制集合

# pop() 随机弹出一个元素
a = {1, 5, 7}
print(a.pop())
print(a)
print("*"*20)

# remove() 删除集合中的某个值,如果这个值不在这个集合中会报错
b = {1, 5, 9}
print(b.remove(5))
print(b)
b.remove(9)
print(b)
# b.remove(9)  # 报错
print("*"*20)

# discard() 删除集合中的某个值,如果这个值不在这个集合中什么也不做
c = {1, 5, 9}
print(c.discard(5))
print(c)
c.discard(9)
print(c)
c.discard(9)  # 什么也不做
print(c)
print("*"*20)

# difference() 差集
# difference update() 区别就是difference(),返回一个新的集合  difference updat()把原来的集合覆盖
set2 = {1, 2, 3, 4}
set3 = {4, 5, 6, 7}
print(set2.difference(set3))
print(set2)
print(set3.difference(set2))
print(set3)
print("*"*20)

# 区别
print(set2.difference_update(set3))
set2.difference_update(set3)
print(set2)
set2 = {1, 2, 3, 4}
print(set3.difference_update(set2))
set3.difference_update(set2)
print(set3)