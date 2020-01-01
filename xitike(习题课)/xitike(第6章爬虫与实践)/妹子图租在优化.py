
import json
import os
import random
import re
import time
from urllib import request

from lxml import etree
from selenium import webdriver

img_down = []


def lianjie(page):
    for i in range(1, page):
        url = "https://www.mzitu.com/page/%d" % i
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
            # pages(imgss)
            img_down.append(img_downs)
        pages(random.choice(img_down))
            # pages(img_downs)


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
    imgsss = html.xpath("//div[@class='main-image']/p/a/img/@src")[0]
    print(imgsss)
    jilu = {}
    jilu["name"] = name
    jilu["page"] = page
    jilu["img_zhuye"] = imgsss
    cont = json.dumps(jilu, ensure_ascii=False, indent=4)
    with open("meizitu.json", "a", encoding="utf-8")as f:
        f.write(cont)
    print(jilu)
    down(page, name, imgsss)



def down(page, name, imgsss):
    co = re.compile(r"\d+\w\d+")
    a = co.findall(imgsss)
    c = re.compile(r"\d+\w")
    d = c.findall(a[1])
    e = [i for i in range(1, 10)]
    page = int(page) + 1
    fi= os.makedirs(r"F:\wode\妹子图\%s" %(name))   # 创建文件夹
    file_root_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录的绝对路径
    img_dir_path = os.path.join(file_root_path, r'F:\wode\妹子图\%s'% name)  # 文件路径
    c = []
    for i in range(1, page):
        if i in e:
            q = str(d[0]) + "0" + str(i)
            urls = re.sub(a[1], q, imgsss)

        else:
            q = str(d[0]) + str(i)
            urls = re.sub(a[1], q, imgsss)

        try:

            tpianname = str(name) + str(i) + ".jpg"
            urls = urls
            c.append(urls)
            opens = request.build_opener()
            opens.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"),("Referer", "https://www.mzitu.com/xinggan/")]
            request.install_opener(opens)
            file_down = os.path.join(img_dir_path, tpianname)
            request.urlretrieve(urls, file_down)
            print("下载完成:   " + tpianname)
            time.sleep(0.2)
        except Exception as es:
            print(es)
    b = c
    bs = json.dumps(b, ensure_ascii=False, indent=4)
    with open("meizitu.json", "a", encoding="utf-8")as f:
        f.write(bs)

def sele(img_down):
    driver = webdriver.Chrome()
    url = random.choice(img_down)
    print(url)
    driver.get(url)
    driver.save_screenshot("妹子图.png")
    driver.quit()


if __name__ == "__main__":
    lianjie(2)
    print(img_down)
    # sele(img_down)