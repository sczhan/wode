from urllib import request

isProxy = input("plese input is daili? y/n")
# 有代理
proxy_1 = request.ProxyHandler({"https": "223.199.29.227:9999"})

# 无代理
proxy_2 = request.ProxyHandler()

opener = request.build_opener(proxy_2)

if isProxy == "y":
    opener = request.build_opener(proxy_1)

url = "http://www.langlang2017.com"

req = request.Request(url)
response = opener.open(req)

print(response)