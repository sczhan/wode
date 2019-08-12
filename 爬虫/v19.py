
"""
v2
处理js加密处理
"""
"""
通过查找,能找到js代码中的操作代码
salt i : r = "" + (new Date).getTime(),
         i = r + parseInt(10 * Math.random(), 10);
sign: n.md5("fanyideskweb" + e + i + "n%A-rKaT5fb[Gy?;N5@Tj")
md5一共需要四个参数,第一个和第四个都是是固定值的字符串, 第三个是所谓的salt, 第二个是...
第二个参数就是输入的要查找的单词
"""
import hashlib
import random
import time
from urllib import request, parse


def getSalt():
    """
    salt公式是 : ("" +((new Date).getTime())+ parseInt(10 * Math.random(), 10);
    :return:
    """
    salt = int(time.time()*1000) + random.randint(0, 10)
    return salt


def getMD5(v):
    """
    :param v:
    :return:
    """
    md5 = hashlib.md5()

    # updata需要一个bytes格式的参数
    md5.update(v.encode("utf-8"))
    sign = md5.hexdigest()

    return sign


def getSign(key, salt):
    sign = "fanyideskweb" + key + str(salt) + "n%A-rKaT5fb[Gy?;N5@Tj"
    sign = getMD5(sign)
    return sign


def youdao(key):
    """
    :param key:
    :return:
    """
    salt = getSalt()
    url = "http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule"
    data = {
        "i": key,
        "from": "AUTO",
        "to": "AUTO",
        "smartresult": "dict",
        "client": "fanyideskweb",
        "salt": str(salt),
        "sign": getSign(key, salt),
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
        # "Accept-Encoding": "gzip, deflate", 这里gzip, deflate 改成utf-8 也可以
        "Accept-Language": "zh-CN,zh;q=0.9",
        "Connection": "keep-alive",
        "Content-Length": len(data),
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
    youdao("man")