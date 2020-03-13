"""
网易云音乐歌手信息抓取
url = https://music.163.com/discover/artist/cat?id=4001&initial=65

id=4001 id歌手类型
initial=0
init = [-1, 65-90, 0]
"""
import csv
import random

import requests
from bs4 import BeautifulSoup


def get_artlist(url):
    my_headers = [
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
        "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
    ]
    headers = {
        "User-Agent": random.choice(my_headers),
        "Referer": "https://music.163.com/",
        "Host": "music.163.com"
    }
    r = requests.get(url, headers=headers)
    # print(r.status_code)
    soup = BeautifulSoup(r.text, "lxml")
    for item in soup.find_all("a", attrs={'class': "nm nm-icn f-thide s-fc0"}):
        artist_name = item.string
        artist_id = item['href'].replace("/artist?id=", "").strip()
        # print(artist_name, artist_id)
        try:
            writer.writerow((artist_name, artist_id))
        except Exception as e:
            print("保存失败: " + e)


if __name__ == '__main__':
    init_list = [-1, 0]
    init_list.extend([i for i in range(65, 91)])
    # print(init_list)
    id_list = [1001, 1002, 1003, 2001, 2002, 2003, 6001, 6002, 6003, 4001, 4002, 4003, 7001, 7002, 7003]
    csvfile = open("music.csv", "a", newline="", encoding="gbk", errors="ignore")
    writer = csv.writer(csvfile)
    writer.writerow(("artist_name", "artist_id"))
    for i in id_list:
        for j in init_list:
            url = "https://music.163.com/discover/artist/cat?id={0}&initial={1}".format(i, j)
            get_artlist(url)
    # url = "https://music.163.com/discover/artist/cat?id=4001&initial=65"
    # get_artlist(url)