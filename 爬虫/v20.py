
"""
爬取豆瓣
了解ajax的基本爬取方式
"""
import json
from urllib import request

if __name__ == "__main__":
    url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20"
    rsp = request.urlopen(url)
    data = rsp.read().decode()

    data = json.loads(data)  # 可以不用
    print(data)
