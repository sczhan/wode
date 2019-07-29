
class Student(object):
    def __init__(self, name, age, scores):
        self.name = name
        self.age = age
        self.scores = scores

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_scores(self):
        return max(self.scores)


stu1 = Student("wang", 18, [100, 99, 80])
print(stu1.get_name())
print(stu1.get_age())
print(stu1.get_scores())
print("*"*20)


class DictClass(object):
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        # 判断key 是否在字典里
        if key not in self.dict.keys():
            return "key不在字典里"
        else:
            self.dict.pop(key)
            return "删除成功"

    def get_dcit(self, key):
        if key not in self.dict.keys():
            return "not found"
        else:
            return self.dict[key]

    def get_key(self):
        x = []
        for key in self.dict.keys():
            x.append(key)
        return x

    def uodate_dict(self, dict2):
        y = []
        self.dict = dict(self.dict, **dict2)
        for value in self.dict.values():
            y.append(value)
        return y


dict1 = DictClass({"one": 1, "two": 2})
print(dict1.del_dict("on"))
print(dict1.get_dcit("tw"))
print(dict1.get_key())
print(dict1.uodate_dict({"three": 3}))
print("*"*20)


class ListInfo(object):
    def __init__(self, list_val):
        self.list_val = list_val

    def add_key(self, key_name):
        #
        if isinstance(key_name, (str, int)):
            self.list_val.append(key_name)
            print(self.list_val)
            return "OK"
        return "字符串和数字"

    def get_key(self, index):
        # 判断传入的索引是否超过了列表
        if 0 <= index < len(self.list_val):
            return self.list_val[index]
        return "输入太大了"

    def update_list(self, list_val2):
        self.list_val.extend(list_val2)
        return self.list_val

    def del_key(self):
        # 首先要判断列表中是否还有元素
        if len(self.list_val) >= 0:
            return self.list_val.pop(-1)
        return "列表为空"


list2 = ListInfo([1, 2, 3])
print(list2.add_key(6))
print(list2.get_key(2))
print(list2.update_list([7, 8, 9]))
print(list2.del_key())
print(list2.add_key([12]))
print("*"*20)


class SetInfo(object):
    def __init__(self, my_set):
        self.my_set = my_set

    def add_setinfo(self, keyname):
        if isinstance(keyname, (str, int)):
            self.my_set.add(keyname)
            return self.my_set
        return "输入字符或整数"

    def get_intersection(self, new_set):
        if isinstance(new_set, set):
            return new_set & self.my_set
        return "不是set"

    def get_union(self, new_set1):
        if isinstance(new_set1, set):
            return  self.my_set | new_set1
        return "不是set"

    def del_difference(self, new_set2):
        if  isinstance(new_set2, set):
            return  self.my_set - new_set2
        return "不是set"


my = SetInfo({1, 5, 9})
print(my.add_setinfo(6))
print(my.get_intersection((5, 6, 7)))
print(my.get_union({7, 5, 3}))
print(my.del_difference({1, 8}))