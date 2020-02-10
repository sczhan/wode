
"""
python 对json文件操作分为编码与解码
编码:
    dumps 字符串
    dump  json对象   可以通过fp文件流写入文件

解码:
    load
    loads
"""
# import json
#
# str = '[{"username": "daochang", "age": "18"}]'
# print(type(str))
# json_str = json.dumps(str, ensure_ascii=False)
# print(json_str, type(json_str))
# new_str = json.loads(json_str)
# print(new_str, type(new_str))

import json

import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88"
                  "  Safari/537.36"
}

r = requests.get("http://www.seputu.com/", headers=headers)

soup = BeautifulSoup(r.text, "lxml")
content = []
for mulu in soup.find_all(class_="mulu"):
    # 标题
    h2 = mulu.find("h2")
    if h2 != None:
        h2_title = h2.string   # 获取标题
        # 获取章节内容与url地址
        list = []
        for a in mulu.find(class_="box").find_all("a"):
            href = a.get("href")  # 获取链接
            # box_title = a.get("title")
            box_title = a.get_text()
            # print(href, box_title)
            list.append({"href": href, "box_title": box_title})
        content.append({"title": h2_title, "content": list})
with open("gcd.json", "a", encoding="utf-8")as f:
    json.dump(content, fp=f, ensure_ascii=False, indent=4)