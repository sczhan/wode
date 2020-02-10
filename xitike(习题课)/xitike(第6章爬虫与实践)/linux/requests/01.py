import requests

url = "https://item.jd.com/1250438.html"

try:
    response = requests.get(url)      # 发起get请求
    print(response.status_code)       # 获取状态码
    print(response.url)                # 获取完整的url
    print(response.apparent_encoding)   # 获取原文编码类型
    print(response.encoding)        # 获取原文编码类型
    print(type(response.text))   # text 响应得到字符串
    print(type(response.content))  # content 响应得到bytes
    print(response.text)  # text 响应得到字符串
    print(response.content)  # content 响应得到bytes
    cookiejar = response.cookies
    cookiedict = requests.utils.dict_from_cookiejar(cookiejar)
    print(cookiedict)
except:
    print("爬取失败")