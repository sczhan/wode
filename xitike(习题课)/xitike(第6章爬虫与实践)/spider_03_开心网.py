
"""
登录开心网
利用cookie
免除ssl

步骤:
    1.寻找登录入口, 通过搜查相应文字可以快速定位
        login_url = "https://security.kaixin001.com/login/login_post.php"
        相应的用户名和密码对应名称为loginemail password
    2. 构造opener
    3. 构造login函数
"""
import ssl
from http import cookiejar
from urllib import request, parse

# 忽略安全问题
ssl._create_default_https_context = ssl._create_unverified_context

# filename = "cookie.txt"
# # cookie = cookiejar.MozillaCookieJar(filename)
cookie = cookiejar.CookieJar()
cookie_handler = request.HTTPCookieProcessor(cookie)
http_handler = request.HTTPHandler()
https_handler = request.HTTPSHandler()

opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    login_url = "https://security.kaixin001.com/login/login_post.php"

    data = {
        "loginemail": "13222057990",
        "password": "wang1998"
    }
    # 对post的data内容进行编码
    data = parse.urlencode(data)

    # http协议的请求头
    headers = {
        "Content": str(len(data)),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"

    }
    # 构造请求 Request对象
    # date要求是一个bytes对象,所有需要进行编码
    req = request.Request(login_url, data=data.encode(), headers=headers)
    rsp = opener.open(req)
    html = rsp.read()
    html = html.decode()
    print(html)

    # 保存cookie到文件
    # ignore_discard 表示及时cookie将要被丢弃也要保存下来
    # ignore_expires 表示如果该文件中cookie即使已经过期,保存
    # cookie.save(ignore_discard=True, ignore_expires=True)


def getHomePage():
    base_url = "http://www.kaixin001.com/set/logo.php"
    rsp = opener.open(base_url)
    html = rsp.read().decode()
    with open("开心网.html", "w", encoding="utf-8")as f:
        f.write(html)


if __name__ == "__main__":
    login()
    # 打印cookie
    # print(cookie)
    # for i in cookie:
    #     print(i)
    #     print(type(i))
    #     for l in dir(i):
    #         print(l)
    getHomePage()