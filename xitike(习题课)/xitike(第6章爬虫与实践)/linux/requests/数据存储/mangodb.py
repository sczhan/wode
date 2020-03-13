"""
mongoDB: 非关系型数据库
mongoDB属于更加适合爬虫的数据库
MongoDB是一个基于分布式文件存储的数据库, 由c++编写
主要为web应用提供可扩展的高性能数据存储解决方案


概要说明
SQL:                  MongoDB:                          说明:
database              database                          数据库
table                 collection                        表/集合
row                   document                          行/文档
colume                filed                             字段/区域
index                 index                              索引
primary               primary                            主键/_id为主键

安装mongoDB
    自行百度
    sudoapt-get install mongodb

如何python操作mongodb
    pip install pymongo
"""

# 导入需要的包pymongo

import pymongo

# 链接mongodb数据库
# client = pymongo.MongoClient()
# client = pymongo.MongoClient("192.168.80.136", 27017)
client = pymongo.MongoClient("mongodb://192.168.80.134:27017")

# 获取到数据库, 连接数据库
db = client.test

# 获取集合
std = db.posts

# 获取数据
datas = std.find()
print(datas)
for data in datas:
    print(data["name"])
# 获取集合中的字段属性


# # 插入文档
# import pymongo
#
# client = pymongo.MongoClient("192.168.80.134", 27017)
# db = client.test
# print(db)
# post = {
#     "name": "liudana",
#     "sex": "m",
#     'age': 18,
#     "class": ['database', "python", "java", "math", "数据分析", "linux"],
#     "income": "10000000"
# }
#
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print("post id is: ", post_id)
