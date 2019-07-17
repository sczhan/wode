
import json

# 此时student 是一个dict格式内容, 不是json
Student = {
    "name": "wwww0",
    "age": 15,
    "mobile": "152325"
}

print(type(Student))

stu_json = json.dumps(Student)
print(type(stu_json))
print("JSON对象{0}".format(stu_json))

stu_dict = json.loads(stu_json)
print(type(stu_dict))
print(stu_dict)