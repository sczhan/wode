
import json

import requests

from mongodb.MysqlAPI import Sql

city_list = []
with open(r"F:\wode\xitike(习题课)\xitike(第6章爬虫与实践)\linux\requests\API\cities.txt", "r", encoding="utf-8")as f:
    for eachline in f:
        # print(eachline)
        fileds = eachline.split("\t")
        city = fileds[0]
        city_list.append(city)

# print(city_list, len(city_list))


def getjson(loc, page_num=0):
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
    }
    data = {
        'query': '公园',
        'region': loc,
        'scope': '2',
        'page_size': 20,
        'page_num': page_num,
        'output': 'json',
        'ak': 'dFSQFgfUITO3Z6GZhYD02tYH63cvOxZm',
    }
    url = "http://api.map.baidu.com/place/v2/search"
    res = requests.get(url, params=data, headers=headers)
    # decodejson = res.json()
    decodejson = json.loads(res.text)
    return decodejson


for eachcity in city_list:
    flag = True
    page_num = 0
    while flag:
         decodejson = getjson(eachcity, page_num)
         # print(eachcity, page_num)
         if decodejson['results']:
             for eachone in decodejson["results"]:
                 # print(eachone)
                try:
                    park = eachone['name']
                except:
                    park = None

                try:
                    location_lat = eachone['location']['lat']
                except:
                    location_lat = None

                try:
                    location_lng = eachone['location']['lng']
                except:
                    location_lng = None

                try:
                    address = eachone['address']
                except:
                    address = None

                try:
                    street_id = eachone['street_id']
                except:
                    street_id = None

                try:
                    uid = eachone['uid']
                except:
                    uid = None

                print(eachcity, park, location_lat, location_lng, address, street_id, uid)
                Sql.insert_city(eachcity, park, location_lat, location_lng, address, street_id, uid)
             page_num += 1
         else:
            flag = False


