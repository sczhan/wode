"""
http://www.langlang2017.com/index.html
http://www.langlang2017.com/route.html
http://www.langlang2017.com/FAQ.html
"""
import random
from urllib import request


def spider(url: str):
    user_headers = [
        "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
        " Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    ]
    # 随机user_headers
    user_agent = random.choice(user_headers)

    # 构建headers头部信息
    headers = {
        "User_Agent": user_agent
    }

    # 构建Request对象
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()

    name = url.split("/")
    filename = name[-1]

    with open(filename, "a", encoding="UTF-8")as f:
        f.writelines(html)


if __name__ == '__main__':
    url_list = ["http://www.langlang2017.com/index.html", "http://www.langlang2017.com/route.html", "http://www.langlang2017.com/FAQ.html"]
    for urls in url_list:
        spider(urls)