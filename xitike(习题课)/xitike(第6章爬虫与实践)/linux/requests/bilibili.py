"""
url = "https://api.bilibili.com/x/web-interface/search/type?context=&page=2&order=&keyword=%E8%A7%86%E9%A2%91&duration=&tids_1=&tids_2=&__refresh__=true&_extra=&search_type=video&highlight=1&single_column=0&jsonp=jsonp"
"""

import json
import os

import random
import requests


# 获取scrurl地址和title
def get_Info(startPage, endPage):
    data = []
    for page in range(startPage, endPage):
        url = "https://api.bilibili.com/x/web-interface/search/type?context=&page={}&order=&keyword=%E8%A7%86%E9%A2%91&duration=&tids_1=&tids_2=&__refresh__=true&_extra=&search_type=video&highlight=1&single_column=0&jsonp=jsonp".format(page)
        decodejson = requests.get(url).text
        decodejson = json.loads(decodejson).get("data")
        items = decodejson["result"]
        for item in items:
            title = str(item["title"]).replace(" ", "").replace('<emclass="keyword">视频</em>', "")
            video_url = item['arcurl']
            data.append([title, video_url])
            # print(title, video_url)
    downloadVideo(data)


# 下载视频
def downloadVideo(data):
    path = r"F:\wode\xitike(习题课)\xitike(第6章爬虫与实践)\linux\requests\bilibili"
    if not os.path.exists(path):
        os.mkdir(path)
    for title, url in data:
        #视频存放地址
        root = path + "\\" + title
        print("....................")
        print("正在下载视频:  {}....".format(title))
        # 利用os.system操作you-get
        os.system("you-get -o {} {}".format(root, url))
        print("视频: {}  下载完成".format(title))


if __name__ == '__main__':
    # get_Info(1, 2)
    print(random.randint(1, 10))
    print(int(1100 /100)%10)