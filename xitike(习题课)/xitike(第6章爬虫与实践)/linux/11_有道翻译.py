
from urllib import request, parse

import hashlib
import json
import random
import time


def getMd5(value):
    md5 = hashlib.md5()
    md5.update(bytes(value, encoding="utf-8"))
    sign = md5.hexdigest()
    return sign


def fy_parse(content):
    data_json = json.loads(content)
    try:
        sr_dict = data_json["smartResult"]["entries"]
        for item in sr_dict:
            print(item, end="")
        print()
    except KeyError as e:
        print("单词不正确")


def yd_fanyi(key):
    """
    :param key:
    :return:
    """
    # salt
    t = int(time.time() * 1000) + random.randint(0, 10)

    # sign
    new_sign = "fanyideskweb" + key + str(t) + "n%A-rKaT5fb[Gy?;N5@Tj"

    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': t,
        'sign': getMd5(new_sign),
        'ts': '1580474152571',
        'bv': '42160534cfa82a6884077598362bbc9d',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
    }
    data = parse.urlencode(data)
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": "OUTFOX_SEARCH_USER_ID=1625632176@10.169.0.84; OUTFOX_SEARCH_USER_ID_NCOO=50747714.85477814; JSESSIONID=aaaEV-XtBT4SAg51-J7-w; ___rl__test__cookies=1580474152565",
        "Host": "fanyi.youdao.com",
        'Origin': 'http:// fanyi.youdao.com',
        'Referer': 'http:// fanyi.youdao.com',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        'X-Requested-With': 'XMLHttpRequest'
    }
    req = request.Request(url, data=bytes(data, encoding="utf-8"), headers=headers)
    response = request.urlopen(req)
    html = response.read().decode()
    fy_parse(html)


if __name__ == '__main__':
    while True:
        key = input("请输入要翻译的内容")
        if key == "q":
            break
        yd_fanyi(key)
