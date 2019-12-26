
import os
from urllib import request

from lxml import etree

img_down = []


def lianjie(page):
    for i in range(1, page):
        url = "https://www.mzitu.com/page/%d"%page
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
        }
        rsp = request.Request(url, headers=headers)
        rep = request.urlopen(rsp)
        html = rep.read().decode()
        # print(html)
        html = etree.HTML(html)
        img = html.xpath("//div/ul[@id='pins']/li")

        for i in img:
            img_downs = i.xpath(".//a/@href")[0]
            imgss = str(img_downs)
            pages(imgss)
            img_down.append(img_downs)


def pages(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
    }
    rsp = request.Request(url, headers=headers)
    rep = request.urlopen(rsp)
    html = rep.read().decode()
    html = etree.HTML(html)
    page = html.xpath("//div[2]/div[1]/div[4]/a[5]/span/text()")[0]
    name = html.xpath("//div[@class='content']/h2/text()")[0]
    page = int(page) + 1
    fi= os.makedirs(r"F:\wode\妹子图\%s" %(name))   # 创建文件夹
    file_root_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录的绝对路径
    img_dir_path = os.path.join(file_root_path, r'F:\wode\妹子图\%s'% name)  # 文件路径
    for i in range(1, page):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/xinggan/"
        }
        try:
            urls = url + "/" + str(i)
            rsps = request.Request(urls, headers=headers)
            repss = request.urlopen(rsps)
            htmls = repss.read().decode()
            htmls = etree.HTML(htmls)
            img = htmls.xpath("//div[@class='main-image']/p/a/img/@src")[0]
            tpianname = str(name) + str(i) + ".jpg"
            urls = img
            open = request.build_opener()
            open.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"),("Referer", "https://www.mzitu.com/xinggan/")]
            request.install_opener(open)
            file_down = os.path.join(img_dir_path, tpianname)
            request.urlretrieve(urls, file_down)
            print("下载完成:   " + tpianname)

            # # 或者
            # urls = url + "/" + str(i)
            # rsps = request.Request(urls, headers=headers)
            # repss = request.urlopen(rsps)
            # htmls = repss.read().decode()
            # htmls = etree.HTML(htmls)
            # img = htmls.xpath("//div[@class='main-image']/p/a/img/@src")[0]
            # tpianname = str(name) + str(i) + ".jpg"
            # img_urls = img
            # rspss = request.Request(img_urls, headers=headers)
            # repsss = request.urlopen(rspss)
            # htmls = repsss.read()
            # os.chdir(r"F:\wode\妹子图\%s" %(name))
            # with open(tpianname, "wb")as f:
            #     f.write(htmls)
            #     print("下载完成:  " + tpianname)

        except Exception as e:
            print(e)


if __name__ == "__main__":
    lianjie(2)


