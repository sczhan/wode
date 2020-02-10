import os
import time

import requests
from lxml import etree


def mz_spider(base_url, headers):
    res = requests.get(base_url, headers=headers)
    html = etree.HTML(res.text)

    # 获取详细呀信息
    img_src = html.xpath('//div[@class="postlist"]/ul/li/a/@href')
    for img_url in img_src:
        # print(img_url)
        img_parse(img_url)


def img_parse(img_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        "Referer": "https://www.mzitu.com/"
    }
    res = requests.get(img_url, headers=headers)
    html = etree.HTML(res.text)

    # 获取标题
    title = html.xpath('//div[@class="content"]/h2/text()')[0]
    # print(title)

    # 获取页数
    page_num = html.xpath('//div[@class="pagenavi"]/a/span/text()')[-2]
    # print(page_num)

    # 拼接图片详情页地址
    for num in range(1, int(page_num) + 1):
        img_src = img_url + "/" + str(num)
        # print(img_src)
        download_img(img_src, title)


def download_img(img_src, title):
        headers = {
            "User-Agent": "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; 360SE)",
            "Referer": "https://www.mzitu.com/"
        }
        res = requests.get(img_src, headers=headers)
        html = etree.HTML(res.text)

        # 图片具体地址获取
        time.sleep(0.5)
        img_url = html.xpath('//div[@class="main-image"]/p/a/img/@src')[0]
        # print(img_url)
        #下载路径
        root_dir = "mz_img"
        img_name = img_url.split("/")[-1]
        title = title.replace(" ", "")

        root_dir = root_dir + "\\" + title
        if not os.path.exists(root_dir):
            os.makedirs(root_dir)

        res = requests.get(img_url, headers=headers)
        with open(root_dir + "\\" + img_name, "wb")as f:
            f.write(res.content)
            f.close()
            print(title + img_name + "下载成功")


if __name__ == '__main__':
    # url = "https://www.mzitu.com/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
        "Referer": "https://www.mzitu.com"
    }

    for i in range(1, 2):
        url = "https://www.mzitu.com/page/{}/".format(i)
        mz_spider(url, headers)