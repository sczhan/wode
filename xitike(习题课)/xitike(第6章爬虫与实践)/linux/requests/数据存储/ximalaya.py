"""
喜马拉雅音乐下载
https://www.ximalaya.com/revision/play/v1/show?id=274677298&sort=1&size=30&ptype=1
https://www.ximalaya.com/revision/play/v1/show?id=274416241&sort=1&size=30&ptype=1
pip install pypinyin  将中文解析成对应的拼音

"""
from urllib import request

import json
import random
import re
import requests
import time
from pypinyin import lazy_pinyin


# 翻译要查找的歌曲类型
def fanyi(vars):
    var = lazy_pinyin(vars)
    str = "".join(var)
    return str


# 获取详情页面信息
def start_spider(str, headers):
    url = "https://www.ximalaya.com/yinyue/{}/".format(str)
    html = requests.get(url, headers=headers).text
    # print(url)
    get_ablumid(html)


def get_ablumid(html):
    """{"albumId":302327,"title":"文 | 民谣---阳光的背面"""
    ablumid = re.findall('{"albumId":(.*?),', html)
    # print(ablumid)
    ablumId = ablumid[:1][0]
    # print(ablumId)
    down_url = "https://www.ximalaya.com/revision/album?albumId={}".format(ablumId)
    # print(down_url)
    # print(down_url)
    # 请求音乐json文件
    res = requests.get(down_url, headers=headers)
    music_json = res.text
    download_music(music_json)

    # for ablumId in ablumid:
    #     # print(ablumId)
    # # 构建下载地址
    #     down_url = "https://www.ximalaya.com/revision/album?albumId={}".format(ablumId)
    #     # print(down_url)
    #     # print(down_url)
    #     # 请求音乐json文件
    #     res = requests.get(down_url, headers=headers)
    #     music_json = res.text
    #     download_music(music_json)


# 开始下载音乐
def download_music(music_json):
    # 获取歌曲标题与连接
    music_json = json.loads(music_json)
    lists = music_json["data"]["tracksInfo"]["tracks"]
    for list in lists:
        id = list["trackId"]
        title = list["title"]
        a = ["/", "\\", ",", "?", "|"]
        for b in a:
            if b in title:
                title = str(list["title"]).replace(str(b), "-")
        down(id, title)


def down(id, title):
    down_url = "https://www.ximalaya.com/revision/play/v1/audio?id={}&ptype=1".format(id)
    # print(down_url)
    res = requests.get(down_url, headers=headers)
    down_musci = res.text
    down_urls = json.loads(down_musci)
    downs = str(down_urls["data"]["src"])
    try:
        if downs.endswith(".m4a"):
            time.sleep(0.2)
            request.urlretrieve(downs, "F:/wode/xitike(习题课)/xitike(第6章爬虫与实践)/linux/requests/数据存储/musci/" + title + ".mp4")
            print(title + "  : 下载成功")
        else:
            time.sleep(0.2)
            baidu(id, title)
            print(title + "  : 下载成功")
    except Exception as e:
        print("下载失败, 原因是: ", e)


def baidu(id, title):
    down_url = "https://www.ximalaya.com/revision/play/baiduMusic?trackId={}".format(id)
    # print(down_url)
    res = requests.get(down_url, headers=headers)
    down_musci = res.text
    down_urls = json.loads(down_musci)
    downs = str(down_urls["data"]["baiduMusicSrc"])
    request.urlretrieve(downs, "F:/wode/xitike(习题课)/xitike(第6章爬虫与实践)/linux/requests/数据存储/musci/" + title + ".mp4")


if __name__ == '__main__':
    while True:
        music_type = input("请输入音乐类型: (quit)")
        if music_type == "quit":
            break
        us = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)"
        ]
        headers = {
            "User-Agent": random.choice(us)
        }
        start_spider(fanyi(music_type), headers)