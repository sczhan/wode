
import ssl
from urllib import request

# ssl免验证
ssl._create_default_https_context = ssl._create_unverified_context
base_url = "https://inv-veri.chinatax.gov.cn"
response = request.urlopen(base_url)
print(response.read().decode(errors="ignore"))


