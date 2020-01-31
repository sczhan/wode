
import json
from urllib import request, parse


def db_spider(content):
    """
    :param content:
    :return:
    """
    # 参数封装
    data = {
        "kw": content
    }

    # 参数的拼接
    data = parse.urlencode(data)
    base_url = "https://fanyi.baidu.com/sug"

    # 封装header头部信息
    header = {
        "Content-Length": len(data),
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36"
    }
    # 封装Request对象
    req = request.Request(base_url, data=bytes(data, encoding="utf-8"), headers=header)
    response = request.urlopen(req)
    html = response.read().decode()

    # 使用json格式化数据
    json_data = json.loads(html)
    for item in json_data["data"]:
        print(item["k"], item["v"])


if __name__ == '__main__':
    content = input("请输入你要翻译的内容")
    db_spider(content)