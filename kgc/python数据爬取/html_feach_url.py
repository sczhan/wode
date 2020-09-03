
import csv
import os
import requests
import urllib3


def get_html_by_urllib3(url):
    pool_manager = urllib3.PoolManager()
    r = pool_manager.request("get", url)
    return r.data.decode('utf-8')


def get_html_by_requests(url):
    r = requests.get(url)
    return r.text


def save_csv(line, stations):
    is_exist = False
    if os.path.exists("stations.csv"):
        is_exist = True
    with open('stations.csv', mode="a", encoding="gbk", newline="") as c:
        writer = csv.writer(c)
        if not is_exist:
            writer.writerow(["公交线路", "站点"])
        writer.writerow([line, ",".join(stations)])

