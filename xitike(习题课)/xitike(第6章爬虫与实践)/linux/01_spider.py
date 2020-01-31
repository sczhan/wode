#
from urllib import request, error
#
# url = "http://www.baidu.com"
# resp = request.urlopen(url)
# print(resp)
# content = resp.read().decode()
# print(content)

"""
# w3school简单的资料爬取
# url = "https://www.w3school.com.cn/js/index.asp"
# """
# from urllib import request
#
# url = "https://www.w3school.com.cn/js/index.asp"
# response = request.urlopen(url)
# print(response)
# content = response.read().decode("GBK", 'ignore')
# print(content)
#

try:
    base_url = "https://www.w3school.com.cn/js/index.asp"
    response = request.urlopen(base_url)
    content = response.read().decode("GBK", 'ignore')
    print(content)
except error.HTTPError as e:
    print(e)
except error.URLError as e:
    print("url 错误")


