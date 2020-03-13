"""
异步加载
pexel 未爬取下来

"""
import random

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

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
photos = []
url = "https://www.pexels.com/search/girl/"

driver = webdriver.Chrome()
driver.get(url)
# # for i in range(1, 2):
# #     js = "var q=document.documentElement.scrollTop=100000"
# #     driver.execute_script(js)
# #     time.sleep(10)
b = driver.page_source
driver.close()
soup = BeautifulSoup(b, "xml")
imgs = soup.find_all("img", attrs={"class": "photo-item__img"})

img_lists = []
for img_list in imgs:
    img_listss = img_list["srcset"]
    img_1 = str(img_listss).split(", ")[0]
    img_lists.append(img_1)
# print(img_lists, len(img_lists))

#
# def Schedule(blocknum, blocksize, totalsize):
#     """
#     显示下载速度
#     :param blocknum:  已经下载的数据块
#     :param blocksize:  数据块的大小
#     :param totalsize:  远程文件大小
#     :return:
#     """
#     per = 100.0 * blocknum * blocksize / totalsize
#     if per > 100:
#         per = 100
#     print("当前下载进度为: {}".format(per))


for item in img_lists:
    data = requests.get(item, headers=headers)
    photo_name = item.split("/")[4]
    # print(photo_name)
    path = "girl"
    if photo_name:
        fp = open(path + "/" + photo_name + ".jpeg", "wb")
        fp.write(data.content)
        fp.close()
        print(path + "/" + photo_name+"下载完成")
    # root_dir = "girl"
    # img = item.split(" ")[0]
    # if not os.path.exists(root_dir):
    #     os.mkdir(root_dir)
    # filename = item.split("/")[4]
    # opener = request.build_opener()
    # opener.addheaders = [('User-Agent',
    #                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
    # request.install_opener(opener)
    # request.urlretrieve(img, root_dir + "/" + filename + ".jpeg", Schedule)