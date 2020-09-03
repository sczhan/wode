
"""
解析豆瓣音乐排行榜
url = "https://music.douban.com/chart"
"""

import os

from lxml import etree
from selenium import webdriver

# 路径
root_dir = r"F:\wode\xitike(习题课)\xitike(第6章爬虫与实践)\linux\DHTML\豆瓣"
if not os.path.exists(root_dir):
    os.mkdir(root_dir)

driver = webdriver.PhantomJS()

driver.get("https://music.douban.com/chart")
driver.implicitly_wait(5)

filename = root_dir + "\music1.png"
# driver.save_screenshot(filename)

result = driver.page_source

html = etree.HTML(result)

ul_list = html.xpath("//ul[@class='col5']")
count = 1
for li in ul_list[0]:

    # 获取排名信息
    index = li.xpath("./span")
    # print(index)
    if index != []:
        index = index[0].text
        # print(index)
    if count <= 10:
        #获取图片
        src = li.xpath(".//img/@src")
        # count += 1
        # print(src)
        if src != []:
            src = src[0]

        # 获取歌名
        name = li.xpath(".//h3/a")
        if name:
            name = name[0].text
            # print(name)

        # 获取歌手以及播放次数
        singer = li.xpath(".//p")
        if singer:
            singer = singer[0].text
            # print(singer)
    else:
        # 取后十名内容
        # 歌名
        li_1 = li.xpath(".//p[@class='icon-play']/a")
        if li_1:
            name = li_1[0].text
            # print(name)
    count += 1
    print(index, name, singer, src)