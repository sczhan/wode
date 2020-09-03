
import time

from lxml import etree
from selenium import webdriver

driver = webdriver.PhantomJS()

def getPage():
    driver.get("https://www.douyu.com/directory/all")
    time.sleep(5)
    html = driver.page_source
    # print(html)
    return html


def parse(html):
    html = etree.HTML(html)

    room_lis = html.xpath('//ul[@class="layout-Cover-list"]/li')
    # print(room_lis)
    for room_li in room_lis:
        # 标题
        title = room_li.xpath('.//h3[@class="DyListCover-intro"]/text()')[0].strip()

        # 标签
        tag = room_li.xpath('.//span[@class="DyListCover-zone"]/text()')[0].strip()
        # print(tag)

        # 作者
        auth = room_li.xpath('.//h2[@class="DyListCover-user"]/text()')[0].strip()
        # print(auth)
        print(title, "****", tag, "****", auth)


def main():
    html = getPage()
    parse(html)


if __name__ == '__main__':
    main()