
"""
构建代理集群/队列
每次访问服务器,随机抽取一个代理
抽取可以使用 random.choice

分析步骤:
1. 构建代理群
2. 每次访问随机选取代理并执行
"""

from urllib import request, error


if __name__ == "__main__":
    # 1. 设置代理地址
    proxy_list = [
        # 列表中存放的是dict类型的元素
        {"http:": "47.106.124.179:80"},
        {"http:": "117.28.97.52:9999"},
        {"http:": "117.69.201.161:9999"},
        {"http:": "221.178.232.130:8080"}
    ]
    # 2. 创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list:
    proxy_handler = request.ProxyHandler(proxy)
    proxy_handler_list.append(proxy_handler)

# 3. 创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)

import random

# 现在如果url,使用代理服务器
try:
    # 4. 安装Opener
    opener = random.choice(opener_list)
    request.install_opener(opener)
    rsp = request.urlopen(url="http://www.baidu.com")
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)