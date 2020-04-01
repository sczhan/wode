
import pymysql

db = pymysql.connect("192.168.80.136", 'root', 'Zhan@1998.', "BaiduMap")
cursor = db.cursor()

# # 创建city表
# sql = """
# create table city(
# id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
# city varchar(200) not NULL,
# park varchar(200) not NULL,
# location_lat FLOAT,
# location_lng FLOAT,
# address VARCHAR(200),
# street_id VARCHAR(200),
# uid VARCHAR(200),
# create_time TIMESTAMP DEFAULT current_timestamp
# )
# """
# cursor.execute(sql)


class Sql():
    @classmethod
    def insert_city(cls, city, park, location_lat, location_lng, address, street_id, uid):
        sql = 'insert into city(city, park, location_lat, location_lng, address, street_id, uid)' \
              'VALUES (%(city)s, %(park)s, %(location_lat)s, %(location_lng)s, %(address)s, %(street_id)s, %(uid)s)'

        value = {
            'city': city,
            'park': park,
            'location_lat': location_lat,
            'location_lng': location_lng,
            'address': address,
            'street_id': street_id,
            'uid': uid
        }

        try:
            cursor.execute(sql, value)
            db.commit()
            print("插入成功")
        except Exception as e:
            print("插入失败: ", e)
            db.rollback()