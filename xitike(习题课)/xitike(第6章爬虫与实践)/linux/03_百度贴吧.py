
"""
 https://tieba.baidu.com/f?ie=utf-8&kw=%E5%A6%96%E6%80%AA%E5%90%8D%E5%8D%95&fr=search
https://tieba.baidu.com/f?kw=妖怪名单&ie=utf-8&pn=50
"""
from urllib import request, parse


def tieba(url):
    name = input("请输入贴吧名称: ")
    page = input("请输入贴吧页数: ")
    for i in range(int(page)):
        qs = {
            "kw": name,
            "page": i * 50
        }
        qs_data = parse.urlencode(qs)
        url = url + qs_data
        print(url)
    headers = {
        "User_Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    req = request.Request(url, headers=headers)
    response = request.urlopen(req)
    html = response.read().decode("UTF-8")

    with open(name + "第" + str(i + 1) + "页" + ".html", "w", encoding="utf-8")as f:
        f.writelines(html)


if __name__ == '__main__':
    start_url = "https://tieba.baidu.com/f?ie=utf-8"
    tieba(start_url)