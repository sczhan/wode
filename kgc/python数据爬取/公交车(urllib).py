import urllib3


url = "http://beijing.8684.cn/x_35b1e697"
pool_manage = urllib3.PoolManager()
r = pool_manage.request("get", url)
print(r.data.decode("utf-8"))
print(r.status)
print(r.headers)
