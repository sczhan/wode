from lxml import etree

import kgc.python数据爬取.html_feach_url as h

url = "http://beijing.8684.cn/x_35b1e697"
html = h.get_html_by_requests(url)
# print(html)
tree = etree.HTML(html)
bus_station = tree.xpath('//div[@class="bus-lzlist mb15"]')[0].xpath("ol/li/a/text()")
line = tree.xpath('//div[@class="name"]/text()')[0] + " " + tree.xpath('//div[@class="trip"]/text()')[0]
h.save_csv(line, bus_station)
print(bus_station, len(bus_station), line)