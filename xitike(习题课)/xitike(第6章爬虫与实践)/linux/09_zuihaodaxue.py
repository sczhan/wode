from urllib import request

from lxml import etree

base_url = "http://zuihaodaxue.com/subject-ranking/mathematics.html"
response = request.urlopen(base_url)
html = response.read().decode()
html = etree.HTML(html)
items = html.xpath("//tr[@class='bgfd']")
for item in items:
    # 排名
    number = item.xpath("./td")[0].text

    # 学校
    school = item.xpath(".//td[@class='align-left']")[0].text
    # school = item.xpath("./td")[1].text

    # 地区
    addr = item.xpath('./td/img//@title')[0]
    # 总分
    # print(addr)
    score = item.xpath("./td")[3].text
    if score != None:
        print(number + "......" + school + "....." + addr + "....." + score)
    else:
        print(number + "......" + school + "....." + addr)