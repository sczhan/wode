
"""
利用map（）函数，把用户输入的不规范的英文，变成首字母大写，其他小写的规范的名字：
比如说["ADMAm"，"LISA"，"JACK"]["Admam"，"Lisa，"Jack]
"""

def standards(s):
    t = s.lower()
    t = t.capitalize()
    print(t)
    return t

name = list(map(standards, ["ADMAm","LISA","JACK"]))
print(name)


"""
打印回数 例如12321 888,999请利用filter()函数
"""
def equal(a,b):
    return a == b

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)-1):
        if equal(s[i], s[len(s)-i-1]):
            continue

        else:
            return False
    return True
output = filter(is_palindrome, range(1, 10000))
print(list(output))


"""
用元组表示学生的姓名和成绩 l = [("bo",75)("bol",75)("aok",85)]
用sorted() 对名字进行排序
"""
l = [("bo",75),("sol",75),("aok",85)]

def by_name(t):
    t = sorted(t[0], key=str.lower)
    return t

l2 = sorted(l, key=by_name)
print(l2)


l = [("bo",75),("sol",95),("aok",85)]

def by_score(t):
    t = sorted(range(t[1]),key=abs)
    return t

l2 = sorted(l, key=by_score,reverse=False)
print(l2)