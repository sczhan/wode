
# 导入python ssl处理模块
import requests


url = "https://www.4399.com/"
rsp = requests.get(url, verify=False)
print(rsp.text)