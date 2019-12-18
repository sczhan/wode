
"""
爬取腾讯招聘的网站 https://hr.tencent.com/position.php?&start=10#a
"""


import json
from urllib import request


def qq(num):
    """
    :return: none
    """
    url = "https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1576603221735&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=%s&pageSize=10&language=zh-cn&area=cn"%num
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.26 Safari/537.36 Core/1.63.6823.400 QQBrowser/10.3.3117.400"
    }
    rep = request.Request(url, headers=headers)
    rsp = request.urlopen(rep)
    html = rsp.read()
    html = json.loads(html,)
    print(html)

    item = {}
    items = []
    for each in html["Data"]["Posts"]:

        jobname = each["RecruitPostName"]
        jobmiaosu = each['Responsibility'].strip().split("\n")
        joburl = each["PostURL"].strip()
        shiian = each["LastUpdateTime"].strip()
        country = each["LocationName"].strip()
        item["工作名称"] = jobname
        item["工作地点"] = country
        item["工作描述"] = jobmiaosu
        item["工作发布时间"] = shiian
        item["工作链接"] = joburl
        with open("腾讯招聘.txt", "a", encoding="utf-8")as f:
            f.write(json.dumps(item, ensure_ascii=False, indent=4))
    print(item)


if __name__ == "__main__":
    for i in range(1, 10):
        qq(i)
