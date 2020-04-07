from mongodb.MysqlAPI2 import MysqlDemo

mysql = MysqlDemo("192.168.80.136", 'root', 'Zhan@1998.', "ceshi")
print(mysql)
# for i in range(1, 10):
#     data = {
#         "FIRST_NAME": "name" + str(i),
#         "LAST_NAME": "Xueyuan",
#         "AGE": "18",
#         "SEX": "M",
#         "INCOME": "10000",
#     }
#     mysql.insert("ceshibiao", data)

# sql = 'select * from ceshibiao where FIRST_NAME ="name2"'
# res = mysql.get_one(sql)
# print(res)
#
# res = mysql.get_all("select * from ceshibiao")
# for item in res:
#     print(item)

data = {
    "FIRST_NAME": "name10",
}
mysql.insert("ceshibiao", data)