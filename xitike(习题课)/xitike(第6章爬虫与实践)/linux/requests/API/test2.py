
import json
import requests


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


province_list = ['四川省', "山东省", "江苏省", "浙江省"]
for eachprovienc in province_list:
    decodejson = getjson(eachprovienc)
    for eachcity in decodejson["results"]:
        # print(eachcity)
        city = eachcity['name']
        num = eachcity['num']
        output = "\t".join([city, str(num)]) + "\n"
        with open('cities.txt', 'a', encoding='utf-8')as f:
            f.write(output)