"""
数据存储之mysql
Ubuntu环境安装mysql
    sudo apt-get update
    sudo apt-get install mysql-server
    sudo apt-get install mysql-client
    sudo apt-get install libmysqlclient-dev

登录数据库:
    sudp mysql -u root -p



rhel7 环境安装mysql数据库
    https://www.cnblogs.com/guozhiping/p/7684134.html

mysql数据库远程连通:
    1. 修改/etc/mysql/my.conf
        找到bind-address = 127.0.0.1 这一行, 将这一行注释
        或者: 将这一行改为bing-address= 0.0.0.0

    2. 让root用户支持连接mysql数据库
        mysql -u root -p
        grant all privileges on *.* to root@'%' identified by "yourpassword" with grant option

    3. 让rhel7中防火墙允许mysql服务通过
        firewall-cmd --permanent --add -service=mysql
        firewall -cmd --reload


Python3操作mysql(pymysql)
    pip install pymysql
"""
import pymysql


# try:
#     # 获取一个数据库连接, 注意是utf8类型, 需要定制数据库
#     # 打开数据库连接
#     """
#     host="192.168.80.133",  数据库服务地址
#     user="sczhan",          登录数据库用户
#     password="Sczhan@1998.",  用户密码
#     db='ceshi',           所连接的数据库名
#     port=3306              数据库端口号, mysql默认3306
#     """
#     db = pymysql.connect(host="192.168.80.133", user="sczhan", password="Sczhan@1998.", db='ceshi', port=3306)
#     print(db)
#     # 创建游标, 对数据库进行操作, 使用cursor()方法
#     cursor = db.cursor()
#     # 使用execute() 执行sql语句
#     cursor.execute("DROP TABLES IF EXISTS ceshibiao")
#     # 使用预处理语句创建表
#     sql =''' create table ceshibiao(
#     FIRST_NAME CHAR(20) NOT NULL,
#     LAST_NAME CHAR(20),
#     AGE INT,
#     SEX CHAR(1),
#     INCOME FLOAT)'''
#     cursor.execute(sql)
#     db.close()
#
# except:
#     print("创建失败")


# 数据库插入操作
# db = pymysql.connect("192.168.80.133", "sczhan", "Sczhan@1998.", "ceshi")
#
# # 利用cursor()创建游标
# cursor = db.cursor()
#
# # # sql语句
# # sql = "insert into ceshibiao(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME) VALUES ('liu8', 'dana', 18, 'M', '100000')," \
# #     "('huang', 'dana', 19, 'M', '9999')"
#
# # 为了防止sql 注入
# sql = "INSERT INTO ceshibiao(FIRST_NAME, LAST_NAME, AGE, SEX, INCOME)" \
#       "VALUES ('%s','%s','%d','%c','%s')" % ('liu1', 'dana', 18, 'M', '100000')
#
# try:
#     # 执行sql语句
#     cursor.execute(sql)
#     # 提交执行
#     db.commit()
#     print("执行成功")
# except:
#     # 发生意外
#     db.rollback()
#     print("执行失败")
#
# db.close()

# 数据库查询操作
try:
    db = pymysql.connect("192.168.80.133", "sczhan", "Sczhan@1998.", "ceshi")
    cursor = db.cursor()
    cursor.execute("select * from ceshibiao")
    # datas = cursor.fetchone()
    # row = cursor.rowcount
    # print(datas, row)
    datas = cursor.fetchall()
    # print(datas)
    for data in datas:
        print(data)
    cursor.close()  # 关闭游标
    db.close()  # 关闭数据库
except Exception as e:
    print("查询失败")
    print(e)

"""
fetchall():  接受全部返回结果
fetchone():  获取下一个查询结果集
rowcount: 只读属性, 返回执行语句影响的行数
"""

