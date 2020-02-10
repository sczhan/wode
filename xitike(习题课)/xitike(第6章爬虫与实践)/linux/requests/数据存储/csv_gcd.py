import csv
import re

import requests
from lxml import etree

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88"
                  "  Safari/537.36"
}

r = requests.get("http://www.seputu.com/", headers=headers)

html = etree.HTML(r.text)

rows = []
div_mulus = html.xpath('//*[@class="mulu"]')
for div_mulu in div_mulus:
    div_h2 = div_mulu.xpath('.//div[@class="mulu-title"]/center/h2/text()')
    if len(div_h2) > 0:
        h2_title = div_h2[0]
        a_s = div_mulu.xpath('./div[@class="box"]/ul/li/a')
        for a in a_s:
            href = a.xpath("./@href")[0]
            box_title = a.xpath("./@title")[0]
            # box_title = a.xpath("./text()")[0]
            # print(href, box_title)
            pattern = re.compile(r"\s*\[(.*)\]\s+(.*)")
            match = pattern.search(box_title)
            if match != None:
                data = match.group(1)
                real_title = match.group(2)
                # print(data, "11", real_title)
                content = (h2_title, real_title, href,  data)
                rows.append(content)
                # print(content)
headers = ["大章节", "小章节", "链接", "日期"]

with open("gcd.csv", "a", newline="", encoding="gbk")as f:
    f_csv = csv.writer(f)
    f_csv.writerow(headers)
    f_csv.writerows(rows)