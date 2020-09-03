import csv
import os
import requests
from lxml import etree


def save_csv(job):
    is_exist = False
    if os.path.exists("职位名.csv"):
        is_exist = True
    with open('职位名.csv', mode="a", encoding="gbk", newline="") as c:
        writer = csv.writer(c)
        if not is_exist:
            writer.writerow(["职位名"])
        writer.writerow([job])


def get_job(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
    }
    html = requests.get(url, headers=headers)
    html.encoding = "gbk"
    html = html.text
    tree = etree.HTML(html)
    jobs = tree.xpath('//div[@class="el"]/p/span/a/text()')
    for job in jobs:
        job = str(job).strip('\r\n').strip(" ")
        save_csv(job)


if __name__ == '__main__':
    url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
    get_job(url)