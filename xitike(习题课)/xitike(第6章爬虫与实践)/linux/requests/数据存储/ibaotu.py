"""
http://video-qn.ibaotu.com/00/92/75/46j888piCKCW.mp4_10s.mp4

"""
import random
import requests
from lxml import etree


class Spider(object):
    def __init__(self):
        us = [
            "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
            "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
            "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
            "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
            "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
            "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)"
        ]
        self.headers = {
            "User-Agent": random.choice(us)
        }
        self.offset = 1

    def start(self, url):
        res = requests.get(url=url, headers=self.headers)
        html = res.text
        html = etree.HTML(html)

        video_src = html.xpath('//div[@class="video-play"]/video/@src')
        # print(video_src)
        # video_title = html.xpath('//div[@class="show-image"]/img/@alt')
        video_title = html.xpath('//span[@class="video-title"]/text()')
        # print(video_title)
        self.write_file(video_src, video_title)

    def write_file(self, video_src, video_title):
        for src, title in zip(video_src, video_title):
            response = requests.get("http:" + src, headers=self.headers)
            filename = title + ".mp4"
            # print(filename)

            with open(r"F:/wode/xitike(习题课)/xitike(第6章爬虫与实践)/linux/requests/数据存储/ibaotu/" + filename, "wb")as f:
                f.write(response.content)


if __name__ == '__main__':
    spider = Spider()
    for i in range(1, 2):
        url = "https://ibaotu.com/shipin/7-0-0-0-0-{}.html".format(str(i))
        spider.start(url)