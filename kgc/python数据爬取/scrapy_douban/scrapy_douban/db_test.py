
import pymysql

def load_all_from_mysql():
    connect = pymysql.Connect(
        host="127.0.0.1", user="root", password="zhan", db='jd', port=3306
    )
    cursor = connect.cursor()
    print(cursor)
    sql = """
    insert into
    """
    # cursor.execute(sql)
    # cursor.fetchall()
    # connect.commit()  # 插入 删除什么的需要  查询不需要


load_all_from_mysql()