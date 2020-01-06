
from urllib import request, parse

url = "https://fanyi.sogou.com/reventondc/translateV2"
data = {
        "from": "auto",
        "to": "zh-CHS",
        "text": "gril",
        "client": "pc",
        "fr": "browser_pc",
        "pid": "sogou-dict-vr",
        "dict": "true",
        "word_group": "true",
        "second_query": "true",
        "uuid": "3cab6d60-d78f-4ca7-847a-ed1bc1a91457",
        "needQc": "1",
        "s": "d3668d601955efcee561de3cc45ada0a"
}
data = parse.urlencode(data)
heard = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Length": str(len(data)),
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Cookie": "IPLOC=CN3201; SUID=CB6B66B42B12960A000000005D4BDFBB; usid=lFq5s4nbUps701BG; SUV=00A5252BB4666BCB5D4BDFBC51658529; QIDIANID=/j13mbLilO00Wq0q0ml5Ssx2rV2ISxugD3cGkOuz9gIanlaOvPnTw9NuakqEbQvdfEj3kZraJyP7jx9keX5s4w==; SNUID=CB6B67B401048EE368E4DAD6018A2F8F; ad=lAJXYyllll2NUuIClllllVCvzXUlllllHpBrhZllllGlllllRQB1B5@@@@@@@@@@; ABTEST=0|1565686955|v17; SELECTION_SWITCH=1; HISTORY_SWITCH=1; sct=9; ld=FZllllllll2Nvd@vlllllVCF0nolllllHpBrhZllllklllllRklll5@@@@@@@@@@; LSTMV=289%2C279; LCLKINT=3192",
    "Host": "fanyi.sogou.com",
    "Origin": "https://fanyi.sogou.com",
    "Referer": "https://fanyi.sogou.com/?fr=websearch",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3722.400 QQBrowser/10.5.3738.400",
    "X-Requested-With": "XMLHttpRequest",
}

rep = request.Request(url, headers=heard, data=data, method="post")
rsp = request.urlopen(rep)
html = rsp.read().decode()
print(html)
# rep = requests.request("POST", url, data=data, headers=heard)
# print(rep.text)
