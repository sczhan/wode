
from urllib import request

if __name__ == "__main__":
    url = "http://www.renren.com/971834521/profile"

    req = request.Request(url)

    rsp = request.urlopen(req)
    html = rsp.read().decode()
    # print(html)

    with open("rsp.html", "w", encoding="UTF-8")as f:
        f.write(html)