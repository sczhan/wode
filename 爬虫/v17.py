
# 导入python ssl处理模块
import ssl
from urllib import request

# 利用非认证上下文环境
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://www.4399.com/"
rsp = request.urlopen(url)
html = rsp.read().decode("gbk")
print(html)