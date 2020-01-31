"""
urllib 模拟登录华为官网
url = "https://www.huawei.com/en/accounts/LoginPost"
method:post
parm:
    userName:1585
    pwd:oDUOBOIcx34SgFzyT8rZVjr/9Az8/OXgdKqGY77F9EeXmxw7VoMhbJC/2pcYgeGpKGkd2eq9DxaclObbAoQoXyMOT7y7p9WFs7LkNZd35DWiicFE673i1CwpxGuymxGCEb8YjHS2Vv5uk6wpCjPXrvADGnEw0SOFLjKXg1NGZko=
    languages:zh
    fromsite:www.huawei.com
    authMethod:password
"""
from http import cookiejar
from urllib import request, parse

# 生成cookie对象
cookie = cookiejar.CookieJar()
# 生成cookie管理器
cookie_handler = request.HTTPCookieProcessor(cookie)
# 生成http请求管理器
http_handler = request.HTTPHandler()
# 生成https管理器
https_handler = request.HTTPSHandler()

# 构建发起请求管理器
opener = request.build_opener(cookie_handler, http_handler, https_handler)


# 构建登录函数

def login(url):
    data = {
        "userName": "13222057990",
        "pwd": "wang1998.?",
        "languages": "zh",
        "fromsite": "www.huawei.com",
        "authMethod": "password"
    }

    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
    }

    data = parse.urlencode(data)
    # data 数据类型为bytes
    req = request.Request(url, data=bytes(data, "utf-8"), headers=headers)
    content = opener.open(req)
    contents = content.read().decode("utf-8")
    print(contents)


if __name__ == '__main__':
    url = "https://www.huawei.com/en/accounts/LoginPost"
    login(url)
