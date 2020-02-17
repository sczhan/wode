"""
1. 获取到下载文件url  二进制方式下载
urllib  模块提供urlretrieve()  此模块可以进行音频文件下载
                             也支持将远程数据下载到本地
 urlretrieve(url, filename=None, reporthook=None, data=None):
 url:  我们下载url地址
 filename: 数据存储路径 + 文件名
 reporthook: 要求回调函数, 连接上服务器或者相应数据传输下载完毕时触发该回调函数
            显示当前下载进度
 data:(filename, headers)元组
"""
import random
from urllib import request

import os
import requests
from lxml import etree


def Schedule(blocknum, blocksize, totalsize):
    """
    显示下载速度
    :param blocknum:  已经下载的数据块
    :param blocksize:  数据块的大小
    :param totalsize:  远程文件大小
    :return:
    """
    per = 100.0 * blocknum * blocksize / totalsize
    if per > 100:
        per = 100
    print("当前下载进度为: {}".format(per))


us = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)"
]

headers ={
    "User-Agent": random.choice(us)
}

url = "https://www.ivsky.com/tupian/ziranfengguang/"
reponse = requests.get(url)

html = etree.HTML(reponse.text)

img_urls = html.xpath('.//div[@class="il_img"]//img/@src')

# print(img_url)
for img_urll in img_urls:
    root_dir = "img"
    if not os.path.exists(root_dir):
        os.mkdir(root_dir)
    filename = img_urll.split("/")[-1]
    img_url = "http:" + img_urll
    # print(img_url)
    request.urlretrieve(img_url, root_dir + "/" + filename + "500x500" + ".jpg", Schedule)