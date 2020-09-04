import requests

url = "http://beijing.8684.cn/x_35b1e697"
r = requests.get(url)

print(r.text)
print(r.status_code)
print(r.content)