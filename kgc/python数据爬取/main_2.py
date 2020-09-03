from lxml import etree

import kgc.python数据爬取.html_feach_url as h

prefix_url = "http://beijing.8684.cn"
url = "http://beijing.8684.cn/line1"
html = h.get_html_by_requests(url)
tree = etree.HTML(html)
bus_lines_url = tree.xpath('//div[@class="list clearfix"]/a/@href')
for bus_lines in bus_lines_url:
    bus_html = h.get_html_by_requests(prefix_url + bus_lines)
    tree = etree.HTML(bus_html)
    bus_line = tree.xpath('//div[@class="name"]/text()')[0] + " " + tree.xpath('//div[@class="trip"]/text()')[0]
    bus_station = tree.xpath('//div[@class="bus-lzlist mb15"]')[0].xpath("ol/li/a/text()")
    print(bus_line, bus_station, len(bus_station))
    h.save_csv(bus_line, bus_station)

