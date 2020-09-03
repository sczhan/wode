
import pymysql
from selenium import webdriver
# expected_conditions 负责条件的发起, 触发
from selenium.webdriver.support import expected_conditions as Ec

"""
设置等待
selenium 主要提供隐性等待和显示等待
driver : 传入webdriver的实例
timeout: 超时时间, 等待的最长时间(考虑隐性等待时间)
poll_frequency=POLL_FREQUENCY: 调用until或者until_not方法的间隔时间, 默认是0.5秒
ignored_exceptions=None: 忽略异常, 如果在调用until或者until_not的过程中抛出元组中的异常, 则不中断代码,继续等待,
                            如果排除的是元组外的异常, 则中断代码, 抛出异常
"""
from selenium.webdriver.support.ui import  WebDriverWait
import time

# 捕获超时异常
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup



# 启动浏览器
browser = webdriver.PhantomJS()

wait = WebDriverWait(browser, 50)

# # 连接数据库
# client = pymongo.MongoClient("192.168.80.134", 27017)
# db = client.jd_computer
# collection = db.computer
#
#
# def to_mongodb(data):
#     # 数据存储
#     try:
#         collection.insert(data)
#         print("插入成功")
#     except:
#         print("插入失败")

# 连接数据库
db = pymysql.connect(host="127.0.0.1", user="root", password="zhan", db='jd', port=3306)
# 创建游标, 对数据库进行操作, 使用cursor()方法
cursor = db.cursor()
# # 使用execute() 执行sql语句
# sql = """create table bijiben(
# id int(4) PRIMARY KEY AUTO_INCREMENT,
# title VARCHAR(200) not null,
# price int(4) not null,
# commit int(4),
# mess  varchar(20) not null,
# local varchar(20) not null,
# url  varchar(50) not null)
# """
# cursor.execute(sql)


def mysql(data):
    sql = "INSERT INTO bijiben(title, price, commit, mess, local, url)" \
          "VALUES ('%s', '%s','%s','%s','%s','%s')" % \
          (data["title"], data["price"], data["commit"], data["mess"], data["local"], data["url"])
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交执行
        db.commit()
        print("执行成功")
    except:
        # 发生意外
        db.rollback()
        print("执行失败")
    # db.close()


def search():
    browser.get("https://www.jd.com/")
    try:
        # 查找搜素框 与搜索按钮, 输入信息后点击
        input = wait.until(Ec.presence_of_all_elements_located((By.CSS_SELECTOR, "#key")))
        submit = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR, "#search > div >  div.form > button")))
        # print(input[0])
        input[0].send_keys("笔记本")
        submit.click()

        # 查找笔记本按钮 销售按钮
        button1 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,
            "#J_selector > div:nth-child(2) > div > div.sl-value > div.sl-v-list > ul > li:nth-child(1) > a")))
        button1.click()

        button2 = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,
                                                        "#J_filter > div.f-line.top > div.f-sort > a:nth-child(2)")))
        button2.click()

        # 获取总页数
        page = wait.until(Ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                                "#J_bottomPage > span.p-skip > em:nth-child(1)> b")))
        return page[0].text
    except TimeoutException:
        search()


# 获取下一页
def next_page(page_num):
    try:
        # 滑动网页到底部, 加载所有商品信息
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        html = browser.page_source
        num = page_num - 1
        parse_html(html, num)
        while page_num == 101:
            exit()
        # 查找下一页按钮, 并点击
        button = wait.until(Ec.element_to_be_clickable((By.CSS_SELECTOR,
                                "#J_bottomPage > span.p-num > a.pn-next > em")))
        button.click()
        wait.until(Ec.presence_of_all_elements_located((By.CSS_SELECTOR,
                                "#J_goodsList > ul > li:nth-child(60)")))
        # 判断翻页是否成功
        wait.until(Ec.text_to_be_present_in_element((By.CSS_SELECTOR,
                                                    "#J_bottomPage > span.p-num > a.curr"), str(page_num)))
        print("翻页成功")
    except TimeoutException:
        # print("翻页失败", str(page_num))
        return next_page(page_num)


def parse_html(html, num):
    # 解析页面
    data = {}
    soup = BeautifulSoup(html, "lxml")
    goods_info = soup.select(".gl-item")
    # 查看当前商品数量, 是否加载完成
    quantity = str(len(goods_info))
    # print(quantity)

    for info in goods_info:
        # 获取商品标题信息
        title = info.select(".p-name.p-name-type-2 a em")[0].text.strip().strip("京东电脑").strip("品电脑\t\n")
        data["title"] = title
        # 获取价格
        price = info.select(".p-price i")[0].text.strip()
        data["price"] = price
        # price = int(float(price))

        # 获取商品的评论数量
        commit = info.select(".p-commit strong")[0].text.strip()
        commit = commit.replace("条评价", "")
        if "万" in commit:
            commit.split("万")
            commit = int(float(commit[0])) * 10000
        elif commit == "0" or commit == "":
            commit = 0
        else:
            commit = int(float(commit.replace("+", "")))
        data["commit"] = commit
        # 获取店铺属性
        shop_property = info.select(".p-icons i")
        if len(shop_property) >= 1:
            mess = shop_property[0].text.strip()
            if mess == "自营":
                data['mess'] = "自营"
            else:
                data['mess'] = "非自营"
            try:
                local = shop_property[1].text.strip()
                if local == "本地仓":
                    data['local'] = "本地仓"
                else:
                    data['local'] = "无"
            except:
                data['local'] = "无"
        else:
            data['mess1'] = "非自营"

        # 获取url
        url = str(info.select(".p-name.p-name-type-2 > a")).split('href="')[1].split('" onclick=')[0]
        data['url'] = url
        # print(data)
        mysql(data)


def main():
    # print(type(search()))
    total = int(search())
    # print(total)
    for i in range(2, total+2):
        time.sleep(20)
        print("第", i - 1, "页正在爬取")
        next_page(i)
        print("第", i - 1, "页完成")


if __name__ == '__main__':
    main()
    db.close()
