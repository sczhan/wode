
"""
爬取酷狗 500

url = "https://www.kugou.com/yy/rank/home/1-8888.html?from=rank"
变换页面信息
    1-23   500

最终存储至 mongodb
"""

import random
import time

import requests
from bs4 import BeautifulSoup

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

# client = MongoClient("mongodb://192.168.80.136:27017")
# songs = client.KG_DB.songs


def kg_spider(url):
    """
    获取酷狗音乐top500, 保存至mongodb
    :param url:  请求地址
    :return:
    """
    data = {}
    res = requests.get(url, headers=headers)
    # print(res.text)
    soup = BeautifulSoup(res.text, "lxml")
    ranks = soup.select(".pc_temp_num")
    # print(ranks)
    titles = soup.select(".pc_temp_songlist > ul > li > a")
    # print(titles)
    times = soup.select(".pc_temp_time")
    # print(times)
    for rank, title, time in zip(ranks, titles, times):
        rank = rank.get_text().strip()
        # print(rank)
        # 歌曲名称
        song = title.get_text().split("-")[-1].strip()

        # 歌手
        singer = title.get_text().split("-")[0].strip()

        href = title["href"]
        req = requests.get(href, headers=headers)
        soup = BeautifulSoup(req.text, "lxml")
        mp3s = soup.select(".mainPage")
        print(mp3s)
        mp3 = mp3s["src"]
        print(mp3)
        song_time = time.get_text().strip()
        # print(rank, song, singer, song_time)

        data = {
            "rank": rank,
            "singer": singer,
            "song": song,
            "time": song_time,
            "href": href,
        }

        # data = {
        #     "rank": rank.get_text().strip(),
        #     "singer": title.get_text().split("-")[0].strip(),
        #     "song": title.get_text().split("-")[-1].strip(),
        #     "time": time.get_text().strip(),
        #     "href": title["href"],
        # }
        # songs_id = songs.insert(data)
    return data


# # 数据存储
# def storage_mongo(data):
#     """
#     数据存储
#     :param data:
#     :return:
#     """
#     client = MongoClient("mongodb://192.168.80.136:27017")
#     songs = client.KG_DB.songs
#     songs_id = songs.insert(data)
#     print(songs_id)


if __name__ == '__main__':
    urls = ["https://www.kugou.com/yy/rank/home/{}-8888.html?from=rank".format(str(i)) for i in range(1, 24)]
    for url in urls:
        kg_spider(url)
        # storage_mongo(data)
        time.sleep(1)

"""
https://webfs.yun.kugou.com/202003061905/40104ea015fa7f9f5b2a198c279d423d/G173/M07/1F/08/TYcBAF2y052AJ8TSAEHU69hU-QU049.mp3
https://webfs.yun.kugou.com/202003061826/8f6039545b835a412adb1f40566721a7/G189/M00/17/03/XYcBAF4NnfOAdKH5ADn3W1bs4L0215.mp3
https://webfs.yun.kugou.com/202003061905/40104ea015fa7f9f5b2a198c279d423d/G173/M07/1F/08/TYcBAF2y052AJ8TSAEHU69hU-QU049.mp3
"""