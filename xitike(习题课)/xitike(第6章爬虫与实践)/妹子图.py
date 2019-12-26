import os
from urllib import request

from lxml import etree

img_down  = []
names = []

def lianjie(page):
    url = "https://www.mzitu.com/page/%d"%page
    # for i in range(2, 10):
    #     url = "https://www.mzitu.com/page" + str(i)
    #     start_urls.append(url)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
    }
    rsp = request.Request(url, headers=headers)
    rep = request.urlopen(rsp)
    html = rep.read().decode()
    # print(html)
    html = etree.HTML(html)
    img = html.xpath("//div/ul[@id='pins']/li")
    # name = html.xpath("//div/ul[@id='pins']/li")
    for i in img:
        img_downs = i.xpath(".//a/@href")[0]
        img_down.append(img_downs)
    # for na in name:
    #     name = na.xpath(".//@alt")[0]
    #     names.append(name)


def page(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
    }
    rsp = request.Request(url, headers=headers)
    rep = request.urlopen(rsp)
    html = rep.read().decode()
    html = etree.HTML(html)
    # img = html.xpath("//div[@class='main-image']/p/a/img/@src")[0]
    page = html.xpath("//div[2]/div[1]/div[4]/a[5]/span/text()")[0]
    name = html.xpath("//div[@class='content']/h2/text()")[0]
    page = int(page) + 1
    file_root_path = os.path.dirname(os.path.abspath(__file__))  # 获取当前目录的绝对路径
    img_dir_path = os.path.join(file_root_path, r'F:\wode\妹子图\%s'%name)  # 文件路径
    # fi= os.makedirs(r"F:\wode\妹子图\%s" %(name))
    # os.chdir(r"F:\wode\妹子图\%s" %(name))

    # rsps = request.Request(img, headers=headers)
    # reps = request.urlopen(rsps)
    # htmls = reps.read()
    # htmls = requests.get(img, headers=headers)
    # tpianname = "1.jpg"
    # with open(tpianname, "wb")as f:
    #     f.write(htmls)
    for i in range(1, page):
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36",
            "Referer": "https://www.mzitu.com/xinggan/"
        }
        urls = url + "/" + str(i)
        rsps = request.Request(urls, headers=headers)
        repss = request.urlopen(rsps)
        htmls = repss.read().decode()
        htmls = etree.HTML(htmls)
        # img = html.xpath("//div[@class='main-image']/p/a/img/@src")[0]
        img = htmls.xpath("//div[@class='main-image']/p/a/img/@src")[0]
        tpianname = str(i) + ".jpg"
        urls = img
        # rsp = request.Request(url, headers=headers)
        # htmll = request.urlopen(rsp).read()
        # with open(tpianname, "wb")as f:
        #     f.write(htmll)
        open = request.build_opener()
        open.addheaders = [("User-Agent", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36"),("Referer", "https://www.mzitu.com/xinggan/")]
        request.install_opener(open)
        file_down = os.path.join(img_dir_path, tpianname)
        request.urlretrieve(urls, file_down)


# lianjie(1)
# print(names, img_down)
url = 'https://www.mzitu.com/202182'
page(url)
