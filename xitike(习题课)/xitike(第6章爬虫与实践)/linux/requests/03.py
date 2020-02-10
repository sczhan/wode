import os

import requests

url = "https://img02.sogoucdn.com/app/a/100520021/34d78513dcf65bd3eadd96a01eccd397"
root = "pics"
path = root + "/" + url.split("/")[-1] + ".jpg"
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r = requests.get(url)
        with open(path, "wb")as f:
            f.write(r.content)
            print("文件保存完成")
    else:
        print("文件已经存在")
except:
    print("爬取失败")