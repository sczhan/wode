
"""
爬取百度贴吧, 李现吧
1. 李现贴吧主页是 http://tieba.baidu.com/f?kw=李现
2. 进去之后,贴吧很多页
    第一页网址:http://tieba.baidu.com/f?kw=李现&ie=utf-8&pn=0
    第二页网址:http://tieba.baidu.com/f?kw=李现&ie=utf-8&pn=50
    第三页网址:http://tieba.baidu.com/f?kw=李现&ie=utf-8&pn=100
    第四页网址:http://tieba.baidu.com/f?kw=李现&ie=utf-8&pn=150
    第五页网址:http://tieba.baidu.com/f?kw=李现&ie=utf-8&pn=200
    第六页网址:http://tieba.baidu.com/f?kw=李现&ie=utf-8&pn=250
3. 由上面网址可以找到规律,每一页后面数字不同,且数字应该是(页数-1)*50

解决方案:
    1. 准备构建参数字典
        字典包含三部分 kw. ie.  pn
    2. 使用parse构建完成
    3. 使用for循环下载

"""

from urllib import request, parse

if __name__ =="__main__":

    #1.构建参数字典
    qs = {
        "kw": "李现",
        "ie": "utf-8",
        "pn": 0
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
        'Connection': 'Keep-Alive',
        }

    # 2.使用parse构建完整url
    # 假定只需要钱前10页
    urls = []
    baseurl = "https://tieba.baidu.com/f?"
    filename = 0
    for i in range(10):
        pn = i * 50
        qs["pn"] = str(pn)
        # 把qs编码后和基础url进行拼接
        urls.append(baseurl + parse.urlencode(qs))
    print(urls)
    # 3. 使用for循环下载
    for url in urls:

        req = request.Request(url, headers=headers)
        rsp = request.urlopen(req)
        html = rsp.read().decode("utf-8")
        filename += 1
        filenames = "李现" + str(filename) + ".html"
        with open(filenames, "w", encoding="utf-8")as file:
            file.write(html,)
        print(url)
        print(html)


"""
做完善
1. 把每个抓到的内容保存到文件中,文件后缀是html
"""
