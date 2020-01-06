
"""
访问一个网址
更改自己的UserAgent进行伪装
"""

from urllib import request, error


if __name__ == "__main__":
    url = "http://www.baidu.com"

    try:
        # 使用head方法伪装Ua
        # headers = {}
        # headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
        # req = request.Request(url, headers=headers)

        # 使用add_header方法
        req = request.Request(url)
        req.add_header("User - Agent", " Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19")

        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print(html)
    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)

print("Done ----->")