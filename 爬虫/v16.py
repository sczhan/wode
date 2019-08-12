

from http import cookiejar
from urllib import request

# 创建cookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load("cookie.txt", ignore_expires=True, ignore_discard=True)
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https 管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def getHomePage():
    url = "http://www.renren.com/971835091/profile"

    # 如果已经执行了login函数, 则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    # print(html)

    with open("rsp4.html", "w", encoding="UTF-8")as f:
        f.write(html)


if __name__ == "__main__":
    getHomePage()