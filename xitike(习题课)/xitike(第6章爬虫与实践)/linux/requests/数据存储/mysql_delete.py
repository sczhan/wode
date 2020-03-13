import pymysql

db = pymysql.connect("192.168.80.134", "sczhan", "Sczhan@1998.", "ceshi", 3306)
cursor = db.cursor()

# 创建删除语句
sql = "delete from ceshibiao where INCOME > '%f'"%(9999)
try:
    cursor.execute(sql)
    db.commit()
    print("执行成功")
except Exception as e:
    db.rollback()
    print("执行失败:" + e)
db.close()