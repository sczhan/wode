

from urllib import request

from bs4 import BeautifulSoup

url = "http://www.baidu.com"

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, "lxml")

# bs自动转码
content = soup.prettify()
# print(content)
print(soup.name)
print("*"*70)
for node in soup.head.contents:
    if node.name == "meta":
        print(node)
    if node.name == "title":
        print(node.string)

