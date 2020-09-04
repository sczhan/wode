"""
url = "https://search.douban.com/book/subject_search?search_text=python&cat=1001&start=0”
"""

import time

from lxml import etree
from selenium import webdriver


def spider(url, i):
    driver = webdriver.PhantomJS()
    driver.get(url)

    # 等待两秒钟
    time.sleep(2)

    # 生成图片快照
    driver.save_screenshot("douban_book{}.png".format(i))

    filename = "douban_book{}.html".format(i)
    with open(filename, "w", encoding="utf-8")as f:
        f.write(driver.page_source)
    parse(filename, i)
    driver.quit()


# 解析数据
def parse(file, i):

    # 读取文件
    with open(file, "r", encoding="utf-8")as f:
        html = f.read()
    # print(html)
    html = etree.HTML(html)
    # print(html)

    # 获取所有book
    books = html.xpath("//div[@class='item-root']")
    # print(books)

    # 获取所有子节点
    for book in books:
        try:
        # 封面图片连接
            book_src = book.xpath("./a/img/@src")[0]
        except:
            book_src = None
        # 书名
        book_name = book.xpath(".//div[@class='title']/a")[0].text

        try:
        # 书链接
            book_url = book.xpath(".//div[@class='title']/a/@href")[0]
        except:
            book_url = None

        try:
        # 评分
            book_start = book.xpath(".//span[@class='rating_nums']")[0].text
        except:
            book_start = None

        try:
        # 作者
            book_author = book.xpath(".//div[@class='meta abstract']")[0].text
        except:
            book_author = None
        print(book_src, book_name, book_url, book_start, book_author)
    print("完成豆瓣读书第{}页面".format(i))


if __name__ == '__main__':
    for i in range(0, 10):
        url = "https://search.douban.com/book/subject_search?search_text=python&cat=1001&start={}".format(i * 15)
        # print(url)
        spider(url, i)