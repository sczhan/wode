
"""
python 连接mysqldemo
1. 获取数据库  pymysql mysqldb
2. 获取记录
3. 增加记录
4. 修改记录
5. 删除记录
6. ..........

"""
__author__ = "wyz"

import pymysql

class MysqlDemo(object):
    # 设置数据库连接参数, 默认编码类型为 utf-8, 参数为字符串
    def __init__(self, host, username, password, dbname):
        self.conn = pymysql.connect(host, username, password, dbname, charset="utf8")
        self.cursor = self.conn.cursor()

    # 获取数据
    def get_all(self, sql):
        # sql = "select * from tabname where value"
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        except Exception as e:
            print(e)
            return False

    # 获取单条数据
    def get_one(self, sql):
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchone()
            return results
        except Exception as e:
            print(e)
            return False

    # 插入一条数据 tableName data(字典)
    def insert(self, table_name, data):
        if len(data.keys()) == 1:
            sql = "insert into {}({}) values".format(table_name, tuple(data.keys())[0]).replace("'", "") + \
                  '("{}")'.format(tuple(data.values())[0])
            # print(sql)
        else:
            sql = "insert into {}{} values".format(table_name, tuple(data.keys())).replace("'", "") + \
                 str('{}'.format(tuple(data.values())))
            # print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            # 返插入后的id
            return self.cursor.lastrowid
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False


    # 更新记录 tableName data(字典) restrication_str
    def update(self, table_name, data, restrication_str):
        data_str = ""
        for item in data.items():
            data_str += '{}="{}",'.format(item[0], item[1])
        values = data_str[:-1]
        sql = "update {} set {} where {}".format(table_name, restrication_str)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return self.cursor.rowcount
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False

    # 执行一条sql语句
    def query(self, sql):
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return int(self.cursor.lastrowid)
        except Exception as e:
            self.conn.rollback()
            print(e)
            return False


    # 删除一条记录 tableName restrication_str
    def delete(self, ):
        sql = ""


    # 删除表
    def delete_tab(self, table_name):
        pass


    # 格式化表  trncate
    def format_tab(self, table_name):
        sql = "trncate table table_name"
        pass
