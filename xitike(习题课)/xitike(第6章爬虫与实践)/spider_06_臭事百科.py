
"""
爬取臭事百科  页面自己来找
分析:
1. 需要用到requests爬取页面, 用xpath , re 来提取数字
2. 可提取信息 用户头像, 段子内容,  点赞, 好评次数
3. 保存到json文件中

大致三部分
1. down下页面
2. 利用xpath 提取信息
3. 保存文件落地
"""

import requests
from lxml import etree


url = "https://www.qiushibaike.com"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9"
}

# 下载页面
rsp = requests.get(url, headers=headers)
html = rsp.text
# print(html)

# 把页面解析成html
html = etree.HTML(html)
rst = html.xpath("//div[contains(/@id, 'qiushi_tag')]")

for r in rst:
    item = {}
    content = r.xpath("//div[@class='content'/span")[0].text
    print(content)

#     print(type(r))
#     print(r.tag)
#     print(r)
# print(html)
