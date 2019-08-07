
"""
利用request下载页面
自动检测页面编码
"""
import urllib
import urllib.request

if __name__ == "__main__":
    url ="http://stock.eastmoney.com/news/1407,20170807763593890.html"

    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    html = rsp.read()

    # 使用get取值保证不出错
    html = html.decode()
    print(html)

    print("URL: {0}".format(rsp.geturl()))
    print("INFO: {0}".format(rsp.info()))
    print("Code: {0}".format(rsp.getcode()))