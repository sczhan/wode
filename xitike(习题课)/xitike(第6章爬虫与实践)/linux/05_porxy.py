import random
from urllib import request

proxy_list = [
    {"https": "223.199.29.227:9999"},
    {"https": "144.123.68.25:9999"},
]

proxy = random.choice(proxy_list)

# 构建代理服务器
proxy_handler = request.ProxyHandler(proxy)

# 创建网络请求对象
opener = request.build_opener(proxy_handler)

url = "http://www.langlang2017.com"
headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }

req = request.Request(url, headers=headers)
response = opener.open(req)
content = response.read().decode()

print(content)