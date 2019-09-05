
"""
利用map（）函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：
比如说["ADMAm"，"LISA"，"JACK"]["Admam"，"Lisa，"Jack]
利用lamdba函数
"""

ls = ["ADMAm","LISA","JACK"]
new_ls = map(lambda x: x.lower().capitalize(), ls)
print(list(new_ls))



"""
打印回数 例如12321 888,999请利用lamdba
"""
# 打印出1-1000的回数
ls = range(1000)
new_ls = filter(lambda x: str(x)[0] == str(x)[len(str(x))-1],ls)
print(list(new_ls))



"""
用元组表示学生的姓名和成绩 l = [("bo",75)("bol",75)("aok",85)]
用sorted() 对名字进行排序
"""
l = [("bo",75, "wo", 712),("sol",75,"wo", 727),("aok",85,"wo", 772)]

new_l = sorted(l, key=lambda x: x[3], reverse=True)
print(list(new_l))

l = [("bo",75),("sol",75),("aok",85)]

new_l = sorted(l, key=lambda x: x[1], reverse=True)
print(list(new_l))


