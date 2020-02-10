import requests

url = "https://inv-veri.chinatax.gov.cn"
res = requests.get(url, verify=False)
res.encoding = res.apparent_encoding  # 解决页面乱码
print(res.text)
