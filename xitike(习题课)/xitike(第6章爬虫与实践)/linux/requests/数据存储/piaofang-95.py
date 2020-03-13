# """
# 利用pandas 保存数据
# "抓取中国票房网站的数据
# yrl: "www.cbooo.cn"
# """
# import pandas as pd
# import requests, random,json
# from selenium import webdriver
# from bs4 import BeautifulSoup
#
# my_headers = [
#     "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
#     "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
#     "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
#     "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
# ]
# headers = {
#     "User-Agent": random.choice(my_headers),
#     "Host": "www.endata.com.cn",
#     "Connection":"keep-alive",
#     'Upgrade-Insecure-Requests': '1',
# }
#
# url = "http://www.endata.com.cn/BoxOffice/BO/Year/index.html"
# driver = webdriver.Chrome()
# driver.get(url)
#
# soup = BeautifulSoup(driver.page_source, "lxml")
# # print(soup)
# driver.close()
# # 获取数据集合
# movies_table = soup.find_all('table', {'class': "bo-table img-table"})[0]
#
# movies = movies_table.find_all("tr")
# # 获取电影名称
# names = [tr.find_all("td")[1].a.p.string for tr in movies[1:]]
# # print(names)
#
# # 获取电影url地址
# hrefs = ["http://www.endata.com.cn" + tr.find_all("td")[1].a.get("onclick").split("'")[1] for tr in movies[1:]]
# # print(hrefs)
#
# # 获取电影类型
# types = [tr.find_all("td")[2].string for tr in movies[1:]]
#
# # 获取总票房数据
# boxoffice = [int(tr.find_all("td")[3].string.replace(",", "")) for tr in movies[1:]]
#
# # 获取平均票价
# mean_price = [int(tr.find_all("td")[4].string) for tr in movies[1:]]
#
# # 获取场均人次
# mean_people = [int(tr.find_all("td")[5].string) for tr in movies[1:]]
#
# # 获取国家和地区
# contries = [tr.find_all("td")[6].string for tr in movies[1:]]
#
# # 获取上映时间
# times = [tr.find_all("td")[7].string for tr in movies[1:]]
#
#
# # 获取导演
# def getInfo(url):
#     id = url.split("=")[1]
#     from_data = {
#         'movieId': id,
#         'MethodName': 'BoxOffice_GetMovieData_Details'
#     }
#     url = "http://www.endata.com.cn/API/GetData.ashx?"
#     datas = requests.post(url, data=from_data, headers=headers).text
#     jsons = json.loads(datas)
#     for j in jsons["Data"]["Table"]:
#         daoyan = j["MovieDyan"].split("|")[0]
#     return daoyan
#
# directors = [getInfo(url) for url in hrefs]
# # print(directors)
#
# df = pd.DataFrame({
#     "name": names,
#     "href": hrefs,
#     "type": types,
#     "boxoffice": boxoffice,
#     "mean_price": mean_price,
#     "mean_people": mean_people,
#     "times": times,
#     "director": directors,
# })
#
# # 数据存储
# df.to_csv("movies.csv", encoding="gbk")
#
# x = df.groupby("type").agg({"boxoffice": ["count", "mean"]})
# print(x)
# df_2 = pd.read_csv("movies.csv", encoding="gbk")
# print(df_2.head())


"""
利用pandas 保存数据
"抓取中国票房网站的数据
yrl: "www.cbooo.cn"
"""
import json
import random

import pandas as pd
import requests

my_headers = [
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.153 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:30.0) Gecko/20100101 Firefox/30.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.75.14 (KHTML, like Gecko) Version/7.0.3 Safari/537.75.14",
    "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Win64; x64; Trident/6.0)"
]
headers = {
    "User-Agent": random.choice(my_headers),
    "Host": "www.endata.com.cn",
    "Connection": "keep-alive",
    'Upgrade-Insecure-Requests': '1',
}

url = "http://www.endata.com.cn/API/GetData.ashx?"
# year = input("请输入要查询的年份: ")
year = [i for i in range(2020, 2007, -1)]
years = []
names, hrefs, types, boxoffice, mean_price, mean_people, contries, times \
        = [], [], [], [], [], [], [], list()
for y in year:
    zhu_from_data = {
        "year": y,
        "MethodName": "BoxOffice_GetYearInfoData",
    }
    print(y)
    datas = requests.post(url, data=zhu_from_data, headers=headers).text
    jsons = json.loads(datas)
    for j in jsons["Data"]["Table"]:
        years.append(y)
        names.append(j["MovieName"])
        hrefs.append("http://www.endata.com.cn/BoxOffice/MovieStock/movieShow.html?id={}".format(j["Movieid"]))
        types.append(j["Genre_Main"])
        boxoffice.append(int(j["BoxOffice"]))
        mean_price.append(int(j["AvgPrice"]))
        mean_people.append(int(j["AvgPeoPle"]))
        contries.append(j["Area"])
        times.append(j["ReleaseTime"])


# 获取导演
def getInfo(url):
    # print(url)
    id = url.split("=")[1]
    from_data = {
        'movieId': id,
        'MethodName': 'BoxOffice_GetMovieData_Details'
    }
    url = "http://www.endata.com.cn/API/GetData.ashx?"
    datas = requests.post(url, data=from_data, headers=headers).text
    jsons = json.loads(datas)
    for j in jsons["Data"]["Table"]:
        daoyan = j["MovieDyan"]
        if daoyan == "":
            daoyan = daoyan.split("|")[0]
        else:
            daoyan = "null"
    return daoyan


directors = [getInfo(url) for url in hrefs]
# print(directors)

df = pd.DataFrame({
    "year": years,
    "name": names,
    "href": hrefs,
    "type": types,
    "boxoffice": boxoffice,
    "mean_price": mean_price,
    "mean_people": mean_people,
    "times": times,
    "director": directors,
})

# 数据存储
df.to_csv("movies2.csv", encoding="gbk")

x = df.groupby("type").agg({"boxoffice": ["count", "mean"]})
print(x)
df_2 = pd.read_csv("movies2.csv", encoding="gbk")
print(df_2.head())