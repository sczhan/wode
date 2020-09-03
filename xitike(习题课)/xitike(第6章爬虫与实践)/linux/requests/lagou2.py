
"""
url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
post
data{
    first: false
    pn: 2
    kd: python
    sid: 3a472a01eb7f4d1ea7ededcf03225a75
    }
"""
import pandas as pd
import requests

ls = []
porxy = {"HTTP": "http://39.137.69.9:80"}
for page in range(1, 2):
    data = {
        'first': 'false',
        'pn': page,
        'kd': 'python',
        'sid': '259bce1971b7496e9747a7e69870d165',
    }
    headers = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
        # 'Content-Length': str(len(data)),
    }
    s = requests.Session()
    url = "https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput="
    s.get(url, headers=headers)
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    res = s.request("POST", url, data=data, headers=headers, cookies=s.cookies)
    print(res.json())
    data = res.json()['content']['positionResult']['result']
    print(data)

    for item in data:
        positionName = item["positionName"]
        companyId = item["companyId"]
        companyFullName = item["companyFullName"]
        salary = item["salary"]
        workYear = item["workYear"]
        education = item['education']
        city = item["city"]
        # print(positionName, companyId, companyFullName)
        ls.append([positionName, companyId, companyFullName, salary, workYear, education, city])

print(ls)
df = pd.DataFrame(ls, columns=['positionName', 'companyId', 'companyFullName', 'salary', 'workYear', 'education', 'city'])
print(df)

df.to_csv("lagou.csv", index=False, mode="a+", encoding="GBK")