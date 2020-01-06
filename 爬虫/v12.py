

from urllib import request

if __name__ == "__main__":
    url = "http://www.renren.com/971834521/profile"

    headers = {"Cookie": "anonymid=jz2phto4-yoof6p; depovince=GW; _r01_=1; JSESSIONID=abcG4s_Gzqwix5BfkyXXw; ick_login=b5283de0-69ea-4a90-a44b-0d6d6d5399c7; t=f0a3c9727d1533c36504a5a41d1907691; societyguester=f0a3c9727d1533c36504a5a41d1907691; id=971834521; xnsid=8e9dc4d9; jebecookies=c3cf31f8-91e5-4172-a336-37e9b3006816|||||; ver=7.0; loginfrom=null; jebe_key=5c1cca05-bc2d-4422-96b8-f5f358182d63%7C09f7694c91cb66dc742cb694162e62ff%7C1565270362287%7C1%7C1565270363267; jebe_key=5c1cca05-bc2d-4422-96b8-f5f358182d63%7C09f7694c91cb66dc742cb694162e62ff%7C1565270362287%7C1%7C1565270363277; wp_fold=0",
               "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0",
               'Connection': 'Keep-Alive',
               }
    req = request.Request(url, headers=headers)

    rsp = request.urlopen(req)
    html = rsp.read().decode()
    # print(html)

    with open("rsp1.html", "w", encoding="UTF-8")as f:
        f.write(html)