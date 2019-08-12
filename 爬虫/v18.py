
"""
破解有道词典
v1
"""
from urllib import request, parse


def youdao(key):
    """
    :param key:
    :return:
    """
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": "gril",
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": "15655383585630",
        "sign": "a333c8e67b1a6d160c2578aed906f79b",
        "ts": "1565538358563",
        "bv": "178ca06f6316ddf200d82f6a513c25f5",
        "doctype": "json",
        "version": "2.1",
        "keyfrom": "fanyi.web",
        "action": "FY_BY_REALTlME"
    }
    # 参数data需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        # "Accept-Encoding": "gzip, deflate",
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": "249",
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Cookie": '_ntes_nnid=463e9b1db222eb1a437e2cc18943aa41,1552315053810; OUTFOX_SEARCH_USER_ID_NCOO=1092953891.9585066; OUTFOX_SEARCH_USER_ID="-268813542@10.169.0.84"; JSESSIONID=abcrlc_dyPkET4XC9vbYw; ___rl__test__cookies=1565538788039',
        "Host": "fanyi.youdao.com",
        "Origin": "http://fanyi.youdao.com",
        "Referer": "http://fanyi.youdao.com/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
        "X-Requested-With": "XMLHttpRequest",
    }
    req = request.Request(url, data=data, headers=headers)
    rsp = request.urlopen(req)
    html = rsp.read().decode()
    print(html)


if __name__ == "__main__":
    youdao("gril")