"""
任务:
1. 利用selenium模拟鼠标下拉
2. 每次多出现几部电影的信息
"""
import json
import time

from bs4 import BeautifulSoup
from selenium import webdriver

url = "https://movie.douban.com/typerank?type_name=剧情&type=11&interval_id=100:90&action="

driver = webdriver.Chrome()
driver.get(url)

# 向下滚动10000像素
js = "var q=document.documentElement.scrollTop=10000"
time.sleep(3)

# 保存快照
driver.save_screenshot("douban1.png")

# 执行js
for i in range(1):
    driver.execute_script(js)
    time.sleep(5)

# 保存快照
driver.save_screenshot("douban2.png")

# 爬取网页信息
soup = BeautifulSoup(driver.page_source, "xml")
name = soup.find_all("span", {"class": "movie-name-text"})
score = soup.find_all("span", {"class": "rating_num"})
starring = soup.find_all("div", {"class": "movie-crew"})
movie_type = soup.find_all("div", {"class": "movie-misc"})
for names, scores, starrings, movie_types in zip(name, score, starring, movie_type):
    dt = {}
    dt["name"] = names.get_text().strip()
    dt["movie_type"] = movie_types.get_text().strip(" ")
    dt["score"] = scores.get_text().strip(" ")
    dt["starrings"] = starrings.get_text().strip(" ")
    dt = json.dumps(dt, ensure_ascii=False, indent=4)
    with open("douban.json", "a", encoding="utf-8")as f:
        f.write(dt)
    # print("电影名称:{}, 类型是: {}, 评分:{}, \n主演是: {}\n".format(names.get_text().strip(" "),
    #                                                     movie_types.get_text().strip(" "),
    #                                                   scores.get_text().strip(" "),
    #                                                 starrings.get_text().strip(" ")))

driver.quit()
