
from http import cookiejar
from urllib import request, parse

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()
# 生成cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 生成https 管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
opener = request.build_opener(http_handler, https_handler, cookie_handler)


def login():
    """
    负责初次登录
    需要输入用户名密码, 用来获取登录的cookie凭证
    :return:
    """
    # 此处url需要从登录form的action属性中提取
    url = "http://www.renren.com/PLogin.do"

    # 此键值对需要登录form的两个对应input中提取纳闷属性
    data = {"email": "13222057990",
            "password": "wang1998"
            }
    # 把数据进行编码
    data = parse.urlencode(data)

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0"}
    # 创建一个请求对象
    req = request.Request(url, data=data.encode(), headers=headers)

    # 使用opener发起请求
    rsp = opener.open(req)


def getHomePage():
    url = "http://www.renren.com/971835091/profile"

    # 如果已经执行了login函数, 则opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()
    # print(html)

    with open("rsp2.html", "w", encoding="UTF-8")as f:
        f.write(html)


if __name__ == "__main__":
    login()
    getHomePage()