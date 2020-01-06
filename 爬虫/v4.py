

"""
掌握对url进行参数编码的方法
需要使用parse编码
"""
import urllib.request

from urllib import parse

if __name__ == "__main__":

    url ="http://www.baidu.com/s?"
    wd = input("Input your keyword")

    # 要想使用data, 需要使用字典
    qs = {"wd": wd}

    # 转化url编码
    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    # 如果直接使用可读的带参数的url, 是不能访问的
    # fullurl = "http://www.baidu.com/s?wd=大熊猫"
    rsp = urllib.request.urlopen(fullurl)

    html = rsp.read()

    # 使用get取值保证不出错
    html = html.decode()
    print(html)

    # print("URL: {0}".format(rsp.geturl()))
    # print("INFO: {0}".format(rsp.info()))
    # print("Code: {0}".format(rsp.getcode()))