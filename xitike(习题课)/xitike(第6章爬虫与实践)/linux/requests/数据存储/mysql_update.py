
import pymysql
# 数据库连接操作
db = pymysql.connect(host="192.168.80.134", user="sczhan", password="Sczhan@1998.", db="ceshi", port=3306)

# 创建游标
cursor = db.cursor()
try:

    # 创建表
    # sql = """create table ceshibiao(
    #     FIRST_NAME CHAR(20) NOT NULL,
    #     LAST_NAME CHAR(20),
    #     AGE INT,
    #     SEX CHAR(1),
    #     INCOME FLOAT)"""

    # 插入数据
    # sql = "insert into ceshibiao(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('liu8', 'dana', 18, 'M', '100000')," \
    #     "('huang', 'dana', 19, 'M', '9999')"
    # cursor.execute(sql)
    # 提交sql执行
    # db.commit()

    # # 查询数据
    # sql = "select * from ceshibiao"
    # cursor.execute(sql)
    # data = cursor.fetchall()
    # print("更新成功" ,data)

    # sql更新数据
    sql = "update ceshibiao set AGE = AGE-1 where FIRST_NAME='%s'"%('huang')
    cursor.execute(sql)
    # 提交sql执行
    db.commit()
    print("更新成功")
except Exception as e:
    # 发生错误请回滚
    db.rollback()
    print("更新失败: " + e)

db.close()


