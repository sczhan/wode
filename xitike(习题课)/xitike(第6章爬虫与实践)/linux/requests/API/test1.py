"""
注册百度地图API账号并进行开发者认证
目标: 获取全国公园信息并保存mysql里

地点检索详情连接
http://api.map.baidu.com/place/v2/search?query=银行&location=39.915,116.404&radius=2000&output=xml&ak=您的密钥 //GET请求

基础地址
http://api.map.baidu.com/place/v2/search?
参数:
    query: 公园
    region: 成都市
    scope: 2
    page_size: 20
    output: json
    ak: u0IbK90oVnHYn174jZpTQUPDTwxaWiFb
"""
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
    decodejson = res.json()
    print(res.url)

    return decodejson

a = getjson("南京市")
print(a)