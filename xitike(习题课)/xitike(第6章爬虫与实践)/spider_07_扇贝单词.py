"""
扇贝单词:
1. 把python单词列表download下来
2. 主要练习目的是xpath
3. 理论上讲不需要登录
4. url: https://www.shanbay.com/wordlist/104899/202159/
"""
import json
from urllib import request

from lxml import etree

words = []

def shanbei(page):
    """
    page: 页数
    爬取扇贝单词
    :return:
    """
    print(1)
    url = "https://www.shanbay.com/wordlist/104899/202159/?page=%s"%page
    print(url)

    rsp = request.urlopen(url)
    html = rsp.read()
    print(html)
    # 解析html
    html = etree.HTML(html)
    tr_list = html.xpath("//tr")

    # 遍历每一个tr元素, 每一个tr对应一个单词和解释
    for tr in tr_list:
        """
        查找相应的单词和介绍
        """

        word = {}
        strong = tr.xpath(".//strong")

        if len(strong):
            # strip 去掉空格
            name = strong[0].text.strip()

            word["name"] = name
        # print(word)

        # 查找解释
        td_content = tr.xpath('./td[@class="span10"]')
        if len(td_content):
            content = td_content[0].text.strip()
            word["content"] = content
            print(word)
        # print(word)
        if word != {}:
            words.append(word)


if __name__ == "__main__":
    shanbei(2)
    file = "扇贝单词.json"
    # print(type(words))
    with open(file, "w", encoding="utf-8")as f:
       f.write(json.dumps(words, ensure_ascii=False, indent=4))