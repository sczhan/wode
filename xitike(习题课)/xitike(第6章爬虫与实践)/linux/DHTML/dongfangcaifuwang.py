import os
import time

import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

browser = webdriver.PhantomJS()

# 让窗口最大化
browser.maximize_window()
wait = WebDriverWait(browser, 10)


def index_page(page):
    try:
        print("正在抓取第 %s 页" % page)
        wait.until(EC.presence_of_all_elements_located((By.ID, "dt_1")))
        if page > 1:
            # 确定页数输入框
            input_page = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="PageContgopage"]')))
            input_page.click()
            input_page.clear()
            input_page.send_keys(page)

            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#PageCont > a.btn_link")))
            submit.click()
            time.sleep(2)
        # 确认是否成功跳转
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#PageCont > span.at"), str(page)))
        print("跳转成功")
    except Exception as e:
        print(e, 2)
        return None


def parse_table():
    # 提取表格内容
    # element = wait.until(EC.presence_of_all_elements_located((By.ID, "dt_1")))
    # 第二种
    element = browser.find_element_by_css_selector("#dt_1")

    # 提取表格内容
    td_content = element.find_elements_by_tag_name("td")

    lst = []
    for td in td_content:
        lst.append(td.text)
    # print(lst, 1)

    # 确定表格列数
    col = len(element.find_elements_by_css_selector("tr:nth-child(1)  td"))
    # print(col, 2)

    lst = [lst[i: i + col]for i in range(0, len(lst), col)]
    # print(lst, 3)

    # 获取详情页面链接
    lst_link = []
    links = element.find_elements_by_css_selector("#dt_1 a.red")
    # print(links)

    for link in links:
        # print(link)
        url = link.get_attribute("href")
        # print(url)
        lst_link.append(url)


    lst_link = pd.Series(lst_link)
    df_table = pd.DataFrame(lst)
    df_table["url"] = lst_link

    return df_table


def write_to_file(df_table, category, tag):
    file_path = "D:\\eastmoney"
    if not os.path.exists(file_path):
        os.mkdir(file_path)
    os.chdir(file_path)
    if category == "yjkb/13":
        category = "yjkb"
    else:
        category = category
    df_table.to_csv("{}{}.csv".format(category, tag), mode="a", encoding="utf_8_sig", index=0, header=0)



def set_table():
    print("**"*40)
    print("\t\t\t\t\东方财富财富网报表下载")
    print("....................."*5)

    # 设置财务表报获取时间
    year = int(float(input("请输入要查询的年份(四位数2007-2020): \n")))
    while (year < 2007 or year > 2020):
        year = int(float(input("请重新输入要查询的年份(四位数2007-2020): \n")))

    quarter = int(float(input("请输入小写数字季度(1：季度, 2: 年中报， 3： 季度， 4：年度 ")))
    while(quarter < 1 or quarter > 4):
        quarter = int(float(input("请重新输入小写数字季度(1：季度, 2: 年中报， 3： 季度， 4：年度 ")))

    quarter = "{:02d}".format(quarter*3)
    date = "{}{}".format(year, quarter)

    # 设置报表类型
    tables = int(float(input("请输入查询报表对应的内容数字(1, 业绩报表， 2， 业绩快报， 3， 业绩报告， 4.欲纰漏时间， 5， 资产负债， 6， 利润表， 7，现金流量表 ):")))

    dict_tables = {
        1: "业绩报表",
        2: "业绩快报",
        3: "业绩预告",
        4: "欲纰漏时间",
        5: "资产负债",
        6: "利润表",
        7: "现金流量表",
    }
    dict = {
        1: "yjbb",
        2: "yjkb/13",
        3: "yiyg",
        4: "yysj",
        5: "zcfz",
        6: "lrb",
        7: "xjll",
    }

    category = dict[tables]
    tag = dict_tables[tables]
    # 设置url地址
    url = "http://data.eastmoney.com/{}/{}/{}.html".format("bbsj", date, category)

    # 选择爬取的页数
    start_page = int(input("请输入下载起始页:"))
    nums = input("请输入要下载多少页：" )


    # 确定页面最后一页
    browser.get(url)
    try:
        page = browser.find_element_by_css_selector(".next+ a")
        # print(page.text)
        if page.text == "下一页":
            submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#PageCont > a.next")))
            submit.click()
            time.sleep(2)
            page = browser.find_element_by_css_selector("span.at")
            # print(page.text, "try")
        else:
            page = page
    except Exception as e:
        page = browser.find_elements_by_css_selector("div #PageCont > *")[-5]
        # print(page.text)


    print(page.text)
    end_page = int(page.text)


    if nums.isdigit():
        if int(nums) >= end_page or start_page + int(nums) >= end_page:
            end_page += 1
        else:
            end_page = start_page + int(nums)
    elif nums == "":
        end_page = end_page
    else:
        print("页数有错误")

    print("准备下载： {}  {}".format(date, dict_tables[tables]))
    print(url)
    yield {
        "url": url,
        "category": category,
        "start_page": start_page,
        "end_page": end_page,
        "tag": tag
    }


def main(category, page, tag):
    try:
        index_page(page)
        df_table = parse_table()
        write_to_file(df_table, category, tag)
        print("第%s抓取完成" % page)
        print("....." * 80)
    except Exception as e:
        print("抓取失败", e)


if __name__ == '__main__':
    for i in set_table():
        category = i.get("category")
        start_page = i.get("start_page")
        end_page = i.get("end_page")
        tag = i.get("tag")

    for page in range(start_page, end_page):
        print(start_page, end_page)
        main(category, page, tag)
    print("抓取完成")