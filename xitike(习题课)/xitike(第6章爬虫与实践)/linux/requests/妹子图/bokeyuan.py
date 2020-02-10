import requests
from bs4 import BeautifulSoup


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945."
                  "88 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/"
              "signed-exchange;v=b3;q=0.9",
    "Cache-Control:":  "max-age=0",

}
url = "https://www.cnblogs.com/cate/python/"
html = requests.get(url)
soup = BeautifulSoup(html.text, "lxml")

items = soup.select('div[class="post_item_body"]')
# print(items)
for item in items:
    # 标题
    title = item.select('h3 a[class="titlelnk"]')[0].get_text()

    # 详细链接
    href = item.select('h3 a[class="titlelnk"]')[0]["href"]

    # 作者
    author = item.select('div a[class="lightblue"]')[0].get_text()

    # 作者主页链接
    author_home = item.select('div a[class="lightblue"]')[0].get("href")
    print(author_home)
    # 简要信息
    infos = item.select('p[class="post_item_summary"]')[0].get_text().strip("\n").strip(" ")

    datas = item.select('div[class="post_item_foot"]')[0].get_text()
    datas = datas.split(" ")
    # ['\n承受', '\r\n', '', '', '', '发布于', '2020-01-30', '21:08', '\r\n', '', '', '', '\r\n', '', '', '', '', '', '', '', '评论(0)阅读(44)']
    # 发布日期
    time = datas[6] + " " + datas[7]
    # print(time)
    # 评论信息
    pinglun = datas[-1].lstrip("评论(").split(")")[0]

    #阅读数
    read_num = datas[-1].rstrip(")").split("(")[-1]
    # read_num = datas[-1].lstrip("评论(").rstrip(")").split("(")[-1]
    print(read_num)



