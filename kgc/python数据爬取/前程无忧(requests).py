"""
方法:
requests.get(): 获取HTML网页的主要方法，对应HTTP的GET
requests.post(): 向HTML网页提交POST请求方法，对应HTTP的POST
对象的属性:
r.status_code:	HTTP请求的返回状态
r.text:	HTTP响应内容的字符串形式，即：url对应的页面内容
r.encoding:	从HTTP header中猜测的响应内容编码方式
r.apparent_encoding:	从内容中分析出的响应内容编码方式（备选编码方式）
r.content:	HTTP响应内容的二进制形式
"""


import requests

url = "https://search.51job.com/list/000000,000000,0000,00,9,99,%25E6%2595%25B0%25E6%258D%25AE%25E5%2588%2586%25E6%259E%2590,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36"
}
r = requests.get(url, headers=headers)
r.encoding = "gbk"
print(r.text)
