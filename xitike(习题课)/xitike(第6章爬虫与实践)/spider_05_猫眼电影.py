
"""
利用正则表达式爬取猫眼电影
1. url: https://maoyan.com/board
2. 把电影信息尽可能多拿下来

分析:
1. 一个影片的内容是以dd开头的单元
2. 在单元内容在一部电影的所有信息


思路:
1. 利用re 把dd内容都给找到
2. 对应找到每一个dd, 用re挨个查找需要的信息

方法就是三步走:
1. 把页面down下来
2. 提取出dd单元为单位的内容
3. 对每一个dd, 进行单独信息提取
"""
import re
from urllib import request

# 1. 下载页面
url = "https://maoyan.com/board"

headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
}
rep = request.Request(url, headers=headers)
rsp = request.urlopen(rep)
html = rsp.read().decode()

# print(html)


# 2. 按dd提取出内容来, 缩小处理范围
s = r"<dd>(.*?)</dd>"
pattern = re.compile(s, re.S)
files = pattern.findall(html)
print(files)

# 3. 从每一个dd中，单独提取出各个信息
for file in files:

    # 提取电影名称
    s = r'<a.*?title="(.*?)"'
    pattern = re.compile(s)
    title = pattern.findall(file)[0]
    print(title)