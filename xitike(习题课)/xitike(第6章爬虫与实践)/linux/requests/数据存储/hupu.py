
import random

import requests
from lxml import etree

# from .hupu_mongodb import MongoAPI
from mongodb.hupu_mongodb import MongoAPI


# 获取初始页面信息
def spider(url):
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
    # 请求页面
    res = requests.get(url, headers)
    html = res.text
    # print(html)
    html = etree.HTML(html)
    return html


# 获取标题
def title(href):
    html = spider(href)
    try:
        title = html.xpath("//div[@class='bbs-hd-h1']/h1/text()")[0]
    except:
        title = "未知请查看详情链接"
    return title


# 解析页面内容
def parse(html):
    # 标题
    # titles = html.xpath("//ul[@class='for-list']//div[@class='titlelink box']/a[@class='truetit']/text()")
    # print(len(titles))
    parse_hrefs = html.xpath("//ul[@class='for-list']//div[@class='titlelink box']/a[@class='truetit']/@href")
    # print(parse_hrefs, len(parse_hrefs))
    parse_hrefs = ["https://bbs.hupu.com" + href for href in parse_hrefs]

    titles = []
    # 获取标题
    for href in parse_hrefs:
        titles.append(title(href))
    print(len(titles), titles)

    # 获取作者
    authors = html.xpath("//div[@class='author box']/a[@class='aulink']/text()")
    # print(authors, len(authors))

    times = html.xpath("//div[@class='author box']/a[2]/text()")
    # print(times, len(times))

    # 获取回复数和发布时间
    datas = html.xpath("//ul[@class='for-list']/li/span[@class='ansour box']/text()")
    # print(datas, len(datas))
    datas = [x.split("\xa0/\xa0") for x in datas]
    print(datas)

    # 回复数
    replies = [x[0] for x in datas]
    # 浏览数
    browses = [x[1] for x in datas]
    # print(len(replies), len(browses))

    # 最后回复时间
    last_times = html.xpath("//div[@class='endreply box']/a/text()")
    # print(last_times, len(last_times))

    # 最后回复人
    last_names = html.xpath("//div[@class='endreply box']/span[@class='endauthor ']/text()")
    print(len(last_names), len(parse_hrefs), len(titles), len(times), len(browses), len(last_names), len(last_times), len(replies))

    items = zip(titles, parse_hrefs, authors, times, replies, browses, last_times, last_names)
    return items


def data_storage(items):
    hupu_post = MongoAPI("192.168.80.136", 27017, "new_hupu", "post")
    for item in items:
        hupu_post.add(
            {
                "titles": item[0],
                "parse_hrefs": item[1],
                "authors": item[2],
                "times": item[3],
                "replies": item[4],
                "browses": item[5],
                "last_times": item[6],
                "last_names": item[7],
            }
        )



def main():
    for i in range(1, 11):
        url = "https://bbs.hupu.com/nba-{}".format(str(i))
        print("正在抓取第{}页数据, 请耐心等待----".format(str(i)))
        html = spider(url)
        data_storage(parse(html))


if __name__ == '__main__':
    main()