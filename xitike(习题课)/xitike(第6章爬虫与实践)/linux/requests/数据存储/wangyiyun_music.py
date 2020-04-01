"""
网易云音乐 下载

下载外链
http://music.163.com/song/media/outer/url?id=song_id.mp3

href="/song?id=1434033729"

http://music.163.com/song/media/outer/url?id=1434033729.mp3
1. 获取页面源码 https://music.163.com/#/playlist?id=2821115454
2. 获取歌曲id以及歌曲名称
3. 下载音乐

"""

from tkinter import *
from urllib import request

import os
import requests
from bs4 import BeautifulSoup


def music_spider():
    # 获取用户输入的url地址
    url = entry.get()
    # url = "https://music.163.com/playlist?id=2821115454"
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36",
        "referer": "https://music.163.com/",
        "host": "music.163.com",
    }
    # 请求页面详情信息
    res = requests.get(url, headers=headers).text
    # print(res.text)

    # 创建soup对象
    soup = BeautifulSoup(res, "lxml")

    # 获取歌曲id与歌曲名称
    music_dicts = {}
    items = soup.find("ul", {'class': 'f-hide'}).find_all("a")

    for item in items:
        music_id = item.get('href').strip("/song?id=")
        music_name = item.text
        music_dicts[music_id] = music_name

    for song_id in music_dicts:
        # 拼接歌曲下载url地址
        song_url = "http://music.163.com/song/media/outer/url?id={}.mp3".format(song_id)

        # 设置下载路径
        path = r"F:/wode/xitike(习题课)/xitike(第6章爬虫与实践)/linux/requests/数据存储/163.music/"
        if not os.path.exists(path):
            os.mkdir(path)

        # 添加数据到控件中
        text.insert(END, "正在下载: {}".format(music_dicts[song_id]))

        # 文本框向下滚动
        text.see(END)

        # 更新
        text.update()
        res = requests.get(song_url, headers=headers, allow_redirects=False)
        # print(res.status_code)
        # print(res.headers)
        m_url = res.headers["Location"]
        try:
            request.urlretrieve(m_url, path + "\\" + music_dicts[song_id] + ".mp3")
            print("下载成功: " + music_dicts[song_id])
        except Exception as e:
            print("下载失败: " + music_dicts[song_id], e)


# 创建一个窗口
root = Tk()

# 设置窗口标题
root.title("网易云音乐下载器")

# 设置窗口大小
root.geometry('850x550')

# # 设置窗口大小
# width = input("请输入宽度: ")
# height = input("请输入高度: ")
# size = width + "x" + height
# root.geometry(size)
# # 设置窗口位置
# window_width = root.winfo_screenwidth()
# window_height = root.winfo_screenheight()
# size_width = (window_width - int(width))/2
# size_height = (window_height - int(height))/2
# size = '+{}+{}'.format(int(size_width), int(size_height))
# root.geometry(size)

# 设置窗口位置
root.geometry("+380+150")

# 设置下载标签, 请输入您下载的地址
lable = Label(root, text="请输入您要下载的地址: ", font=("华文行楷", 20))

# 定位 pack palce grid
lable.grid()

# 设置输入框
entry = Entry(root, font=("微软雅黑", 20), width=34)
entry.grid(row=0, column=1)

# 设置列表框
text = Listbox(root, font=("隶书", 20), width=60, height=15)
text.grid(row=1, columnspan=2)

# 设置按钮 N S W E
button = Button(root, text="Start", font=("微软雅黑", 15), command=music_spider)
button.grid(row=2, column=0, sticky="s")  # sticky 对齐方式

# 退出按钮
button2 = Button(root, text="Quit", font=("微软雅黑", 15), command=root.quit)
button2.grid(row=2, column=1, sticky="s")  # sticky 对齐方式


# 显示窗口, 显示消息回环
root.mainloop()
