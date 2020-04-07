
"""
url = http://api.map.baidu.com/place/v2/detail?uid=435d7aea036e54355abbbcc8&output=json&scope=2&ak=您的密钥 //GET请求
"""
import json
import requests

from mongodb.MysqlAPI import Sql


def getjson(uid):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    }
    data = {
        'uid': uid,
        'scope': '2',
        'output': 'json',
        'ak': 'dFSQFgfUITO3Z6GZhYD02tYH63cvOxZm',
    }
    url = "http://api.map.baidu.com/place/v2/detail"
    res = requests.get(url, params=data, headers=headers)
    # decodejson = res.json()
    decodejson = json.loads(res.text)
    return decodejson


# 从数据库中获取uid号
results = Sql.read_city()
# print(results[0], type(results[0]))  # 类型为元组
for item in results:
    uid = item[0]
    decodejson = getjson(uid)
    # print(decodejson)
    infos = decodejson['result']
    # print(infos)

    # 获取想要的信息
    try:
        # 获取uid
        uid = infos['uid']
    except:
        uid = None

    try:
        # 获取street_id
        street_id = infos['street_id']
    except:
        street_id = None


    try:
        # 获取name
        name = infos['name']
    except:
        name = None

    try:
        # 获取address
        address = infos['address']
    except:
        address = None

    try:
        # 获取shop_hours
        shop_hours = infos["detail_info"]['shop_hours']
    except:
        shop_hours = None

    try:
        # 获取detail_url
        detail_url = infos["detail_info"]['detail_url']
    except:
        detail_url = None

    try:
        # 获取content_tag
        content_tag = infos["detail_info"]['content_tag']
    except:
        content_tag = None
    # print(uid, street_id, name, address, shop_hours, detail_url, content_tag)
    Sql.insert_park(uid, street_id, name, address, shop_hours, detail_url, content_tag)






