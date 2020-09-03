
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
    url = "https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    headers = {
        'Host': 'www.lagou.com',
        'Origin': 'https://www.lagou.com',
        'Referer': 'https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400",
        'Content-Length': str(len(data)),
        'Connection': 'keep-alive',
        'Cookie': "user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; _gid=GA1.2.422016146.1586336693; index_location_city=%E5%85%A8%E5%9B%BD; sajssdk_2015_cross_new_user=1; LGSID=20200408194750-4396a520-63ce-4c1e-a0bf-444702022aed; JSESSIONID=ABAAAECAAFDAAEHE590B3D2B0A1D554A9F6001C3782020D; WEBTJ-ID=20200408194829-171599ec5fbb1-0e6d543f9617a7-6701b35-1327104-171599ec5fc260; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586336693,1586346511; TG-TRACK-CODE=search_code; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; X_HTTP_TOKEN=01dd9aa456f606ad1038436851e021a7f77e9b9a86; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1586348303; LGRID=20200408203610-8b756230-8688-4111-b5ea-c90fa9af621d; SEARCH_ID=6b216f7df0244977ba6c8528fae5e6d2",
        "X-Requested-With": "XMLHttpRequest",
        "Accept":"application/json, text/javascript, */*; q=0.01"
    }
    res = requests.request("POST", url, data=data, headers=headers, proxies=porxy)
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