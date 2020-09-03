import time

from selenium import webdriver

# driver = webdriver.Chrome("F:\wode\kgc\python数据爬取\chromedriver.exe")
# driver.get(
#     "https://www.zhipin.com/job_detail/?query=%E5%9B%BE%E5%83%8F%E5%A4%84%E7%90%86&city=100010000&industry=&position=")
# a = driver.get_cookies()
# a = [{'domain': '.zhipin.com', 'httpOnly': False, 'name': 'Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a', 'path': '/', 'secure': False, 'value': '1592128221'}, {'domain': '.zhipin.com', 'httpOnly': False, 'name': '__l', 'path': '/', 'secure': False, 'value': 'l=%2Fwww.zhipin.com%2Fjob_detail%2F%3Fquery%3D%25E5%259B%25BE%25E5%2583%258F%25E5%25A4%2584%25E7%2590%2586%26city%3D100010000%26industry%3D%26position%3D&r=&friend_source=0'}, {'domain': '.zhipin.com', 'expiry': 1907488220, 'httpOnly': False, 'name': '__a', 'path': '/', 'secure': False, 'value': '23949055.1592128220..1592128220.1.1.1.1'}, {'domain': '.zhipin.com', 'expiry': 1592358620, 'httpOnly': False, 'name': '__zp_stoken__', 'path': '/', 'secure': False, 'value': 'b073aaTgZI20wfmY9OEE4NAlAKSEqbUAuVGEwWEhcGU1wGhdgRWpMc350DyhwXAspPF1BcV1dQn1ZewcYIGMaE00wDwg%2BFWA8CCw0CxBzE18FOiItIjpGdxkUVSgnLEEyfmQEDiB9TwVpYXQ%3D'}, {'domain': '.zhipin.com', 'httpOnly': False, 'name': '__g', 'path': '/', 'secure': False, 'value': '-'}, {'domain': '.zhipin.com', 'httpOnly': False, 'name': 'lastCity', 'path': '/', 'secure': False, 'value': '100010000'}, {'domain': 'www.zhipin.com', 'expiry': 1907488220, 'httpOnly': False, 'name': '_uab_collina', 'path': '/job_detail', 'secure': False, 'value': '159212822058372351716854'}, {'domain': '.zhipin.com', 'httpOnly': False, 'name': '__c', 'path': '/', 'secure': False, 'value': '1592128220'}, {'domain': '.zhipin.com', 'expiry': 1623664220, 'httpOnly': False, 'name': 'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a', 'path': '/', 'secure': False, 'value': '1592128221'}, {'domain': 'www.zhipin.com', 'httpOnly': False, 'name': '__zp__pub__', 'path': '/job_detail', 'secure': False, 'value': ''}]
#
# # time.sleep(10)
# print(a)
# a = re.findall("b073+[a-z A-Z 0-9]+[%]", str(a))
# print(a)
# # driver.close()


headers = {
    # "authority": "www.zhipin.com",
    # "method": "GET",
    # "path": "/job_detail/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&city=100010000&industry=&position=",
    # "scheme": "https",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    # "accept-encoding": "gzip, deflate, br",
    "accept-language": "zh-CN,zh;q=0.9",
    "cache-control": "max-age=0",
    # "cookie": "_uab_collina=159071905074371533234384; __zp__pub__=; sid=sem; toUrl=/; JSESSIONID=""; __c=1592113817; __g=sem; __l=l=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D10642220335188829613&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000K5cNxA6dzipXA58wnSPeKs0YyiITM-cTvyyoJgtWN5ShqoxbLcQD6bfK1m1CHbEPNXUDxJC0NCyk6aSS3rMd9X7gaS82n8h38os1kDfh1S71VaguC8uq7OVJ54Ayq9S7ZUQB8yNsQ82UFzKzmfzm48sK_DXmyP9YmhQBMrDFv8SxcHGMHg_tAiFVGVT2xZlNP--TjSn_pyQG6i9po38Z3v.7D_NR2Ar5Od663rj6t8AGSPticnDpuCcYlxZMLWknwGYqxu68uTkxIW94UvTyj59tqvZut_r11sSXejE33I-XZ1LmIMzseOU9tOZjESyZdSVhHvde5OKeUrMkLqTI7hFWj4en5Vose59sSxu9qIhZxeT5M8sSL1seOU9tSMj_q8Zx813x5I9LtTrzEj4SrZuEse59l3cMYAQLwk3x5kseOgjlqhZ1vmI-XZx_lqJIZ0lp4W63rjz3pM3Lkc69o_ozNvNvy2pMpRt85R_nYQAHG_3tN0.U1Yz0ZDqmhq1TsKspynqn0KY5gILIzRzwgGCpgKGUBRzwyPEUiRzwhnknjDznH0knj00pyYqnWcd0ATqTZn10ZNG5yF9pywd0ZKGujYkrfKWpyfqPHT0UgfqnH0krNtknjDLg1DsPjwxn1msnfKopHYs0ZFY5Hf4nfK-pyfqn1D4nj-xnHfdPNt1nHmLn-tznHDkPNt1nH0vrNt1nW0YPNt1nj6zndtzPWndn0KBpHYkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PHfzPjRLnjKxnH0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYknHndPWTYP1nd0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVuyPJ0A-bm1dribGH0ZwdT1YkP1bdnWfLnH0YPjTvPjRYPHfzP6Kzug7Y5HDdrHcknHn3nH0kPW60Tv-b5yuhuADkuhR1nj0srym4mHc0mLPV5RfdnWR3n1KjnH6vn1NDfYc0mynqnfKYIgfqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1KxPjDLn1bsnNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5H60UAuW5H00uAPWujY0mhwGujdKwWc4wjR3rRfYfWuKnW0sfbmdPHTLwHDkPWf1rHmvf6KEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBnzPjcvrHcsnin1nW0sc1nznj08nj0snj0sc1DWnBnsczYWna3snj0snj0Wni3snj0snj00TNqv5H08rj-xna3sn7tsQW0sg108PHIxna3zP7tsQWnz0AF1gLKzUvwGujYs0APzm1YYnjn3n0%26ck%3D4959.14.87.282.302.446.261.285%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D2.0.1.0.1.300.0%26wd%3Dboss%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3066%26bc%3D110101&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D11323583472472588092&friend_source=0&friend_source=0; __zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591954250,1592113817,1592114026,1592114034; lastCity=100010000; __a=15264055.1590719051.1591954244.1592113817.173.5.64.64; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592134685; __zp_stoken__=b073aaTgZI20wUApZYkguNAlAKSFEQVMNK2EwWEhcGUFqXERlOWpMc350D3RLQWhHPF1BcV1dbHJWIC4YK2lxEihldQomBAhQdl9TfRBzE18FOkxOPwEadxkUVSgnUEEyfmQEDiB9TwVpYXQ%3D",

    # "cookie": "_uab_collina=159071905074371533234384; __zp__pub__=; sid=sem; toUrl=/; JSESSIONID=; __c=1592113817; __g=sem; __l=l=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D10642220335188829613&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000K5cNxA6dzipXA58wnSPeKs0YyiITM-cTvyyoJgtWN5ShqoxbLcQD6bfK1m1CHbEPNXUDxJC0NCyk6aSS3rMd9X7gaS82n8h38os1kDfh1S71VaguC8uq7OVJ54Ayq9S7ZUQB8yNsQ82UFzKzmfzm48sK_DXmyP9YmhQBMrDFv8SxcHGMHg_tAiFVGVT2xZlNP--TjSn_pyQG6i9po38Z3v.7D_NR2Ar5Od663rj6t8AGSPticnDpuCcYlxZMLWknwGYqxu68uTkxIW94UvTyj59tqvZut_r11sSXejE33I-XZ1LmIMzseOU9tOZjESyZdSVhHvde5OKeUrMkLqTI7hFWj4en5Vose59sSxu9qIhZxeT5M8sSL1seOU9tSMj_q8Zx813x5I9LtTrzEj4SrZuEse59l3cMYAQLwk3x5kseOgjlqhZ1vmI-XZx_lqJIZ0lp4W63rjz3pM3Lkc69o_ozNvNvy2pMpRt85R_nYQAHG_3tN0.U1Yz0ZDqmhq1TsKspynqn0KY5gILIzRzwgGCpgKGUBRzwyPEUiRzwhnknjDznH0knj00pyYqnWcd0ATqTZn10ZNG5yF9pywd0ZKGujYkrfKWpyfqPHT0UgfqnH0krNtknjDLg1DsPjwxn1msnfKopHYs0ZFY5Hf4nfK-pyfqn1D4nj-xnHfdPNt1nHmLn-tznHDkPNt1nH0vrNt1nW0YPNt1nj6zndtzPWndn0KBpHYkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PHfzPjRLnjKxnH0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYknHndPWTYP1nd0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVuyPJ0A-bm1dribGH0ZwdT1YkP1bdnWfLnH0YPjTvPjRYPHfzP6Kzug7Y5HDdrHcknHn3nH0kPW60Tv-b5yuhuADkuhR1nj0srym4mHc0mLPV5RfdnWR3n1KjnH6vn1NDfYc0mynqnfKYIgfqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1KxPjDLn1bsnNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5H60UAuW5H00uAPWujY0mhwGujdKwWc4wjR3rRfYfWuKnW0sfbmdPHTLwHDkPWf1rHmvf6KEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBnzPjcvrHcsnin1nW0sc1nznj08nj0snj0sc1DWnBnsczYWna3snj0snj0Wni3snj0snj00TNqv5H08rj-xna3sn7tsQW0sg108PHIxna3zP7tsQWnz0AF1gLKzUvwGujYs0APzm1YYnjn3n0%26ck%3D4959.14.87.282.302.446.261.285%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D2.0.1.0.1.300.0%26wd%3Dboss%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3066%26bc%3D110101&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D11323583472472588092&friend_source=0&friend_source=0; __zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591954250,1592113817,1592114026,1592114034; lastCity=100010000; __a=15264055.1590719051.1591954244.1592113817.131.5.22.22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1592131011; __zp_stoken__=bl8zNmpMc350DyJ6RTdGPF1BcV1dbAwgJHAYJWhdYURDdH9cYgwxdl48YRBzE18FOk0ROzBMdxkUVSgnX0EyfmQEDiB9TwVpYXQ%3D",

    # "referer": "https://www.zhipin.com/job_detail/?query=%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0&city=100010000&industry=&position=",
    # "sec-fetch-dest": "document",
    # "sec-fetch-mode": "navigate",
    # "sec-fetch-site": "same-origin",
    # "sec-fetch-user": "?1",
    # "upgrade-insecure-requests": "1",
}
# thisip = requests.get(
#     "http://dynamic.goubanjia.com/dynamic/get/6b1634d90b1994d851fe9493c4b49ac1.html?sep=3").content.decode(
#     "utf-8").strip()
# print(self.thisip)
# proxy = {"https": "https://" + thisip,
#          "http": "http://" + thisip
#          }
url = "https://www.zhipin.com/job_detail/54e86389321479d20HF92N24Fls~.html"
# driver = webdriver.Chrome("F:\wode\kgc\python数据爬取\chromedriver.exe")
# driver.get(url)
# a = driver.get_cookies()
# time.sleep(10)
# print(a)
# a = re.findall("[a-z A-Z 0-9]*[%]*3D", str(a))
# print(a)
# cookie = "_uab_collina=159071905074371533234384; __zp__pub__=; sid=sem; toUrl=/; JSESSIONID=""; __c=1592113817; __g=sem; __l=l=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D10642220335188829613&r=https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.Kf0000K5cNxA6dzipXA58wnSPeKs0YyiITM-cTvyyoJgtWN5ShqoxbLcQD6bfK1m1CHbEPNXUDxJC0NCyk6aSS3rMd9X7gaS82n8h38os1kDfh1S71VaguC8uq7OVJ54Ayq9S7ZUQB8yNsQ82UFzKzmfzm48sK_DXmyP9YmhQBMrDFv8SxcHGMHg_tAiFVGVT2xZlNP--TjSn_pyQG6i9po38Z3v.7D_NR2Ar5Od663rj6t8AGSPticnDpuCcYlxZMLWknwGYqxu68uTkxIW94UvTyj59tqvZut_r11sSXejE33I-XZ1LmIMzseOU9tOZjESyZdSVhHvde5OKeUrMkLqTI7hFWj4en5Vose59sSxu9qIhZxeT5M8sSL1seOU9tSMj_q8Zx813x5I9LtTrzEj4SrZuEse59l3cMYAQLwk3x5kseOgjlqhZ1vmI-XZx_lqJIZ0lp4W63rjz3pM3Lkc69o_ozNvNvy2pMpRt85R_nYQAHG_3tN0.U1Yz0ZDqmhq1TsKspynqn0KY5gILIzRzwgGCpgKGUBRzwyPEUiRzwhnknjDznH0knj00pyYqnWcd0ATqTZn10ZNG5yF9pywd0ZKGujYkrfKWpyfqPHT0UgfqnH0krNtknjDLg1DsPjwxn1msnfKopHYs0ZFY5Hf4nfK-pyfqn1D4nj-xnHfdPNt1nHmLn-tznHDkPNt1nH0vrNt1nW0YPNt1nj6zndtzPWndn0KBpHYkPH9xnW0Yg1ckPsKVm1Yknj0kg1D3PHfzPjRLnjKxnH0kg100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYknHndPWTYP1nd0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fK9TdqGuAnqTZnVuyPJ0A-bm1dribGH0ZwdT1YkP1bdnWfLnH0YPjTvPjRYPHfzP6Kzug7Y5HDdrHcknHn3nH0kPW60Tv-b5yuhuADkuhR1nj0srym4mHc0mLPV5RfdnWR3n1KjnH6vn1NDfYc0mynqnfKYIgfqnfKsUWYs0Z7VIjYs0Z7VT1Ys0Aw-I7qWTADqn0KlIjYs0AdWgvuzUvYqn7tsg1DsPjuxn0Kbmy4dmhNxTAk9Uh-bT1Ysg1KxPjDLn1bsnNts0ZK9I7qhUA7M5H00uAPGujYs0ANYpyfqQHD0mgPsmvnqn0KdTA-8mvnqn0KkUymqn0KhmLNY5H00pgPWUjYs0ZGsUZN15H00mywhUA7M5H60UAuW5H00uAPWujY0mhwGujdKwWc4wjR3rRfYfWuKnW0sfbmdPHTLwHDkPWf1rHmvf6KEm1Yk0AFY5H00Uv7YI1Ys0AqY5HD0ULFsIjYzc10WnH0WnBnzPjcvrHcsnin1nW0sc1nznj08nj0snj0sc1DWnBnsczYWna3snj0snj0Wni3snj0snj00TNqv5H08rj-xna3sn7tsQW0sg108PHIxna3zP7tsQWnz0AF1gLKzUvwGujYs0APzm1YYnjn3n0%26ck%3D4959.14.87.282.302.446.261.285%26shh%3Dwww.baidu.com%26sht%3Dbaiduhome_pg%26us%3D2.0.1.0.1.300.0%26wd%3Dboss%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D3066%26bc%3D110101&g=%2Fwww.zhipin.com%2Fuser%2Fsem7.html%3Fsid%3Dsem%26qudao%3Dbdpc_baidu-%25E5%258D%258E%25E5%2593%2581%25E5%258D%259A%25E7%259D%25BF02A18KA0679%26plan%3D%25E8%25A1%258C%25E4%25B8%259A%25E5%25AE%259A%25E6%258A%2595-%25E5%2593%2581%25E7%2589%258C%26unit%3Dboss%25E7%259B%25B4%25E8%2581%2598%26keyword%3Dwww.zhipin.com%2Fc101210100%26bd_vid%3D11323583472472588092&friend_source=0&friend_source=0; __zp__pub__=; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1591954250,1592113817,1592114026,1592114034; lastCity=100010000; __a=15264055.1590719051.1591954244.1592113817.131.5.22.22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a={}; __zp_stoken__={}".format(int(time.time()) - 60, a[0]),
# # driver.close()
# print(cookie)
# headers["cookie"] = cookie[0]
# driver.quit()
# time.sleep(20)
# ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument("headless")
driver = webdriver.Chrome(executable_path='F:\wode\kgc\python数据爬取\chromedriver.exe', chrome_options=options)
driver.get(url)
time.sleep(10)
print(driver.page_source)
# print(page.headers)
# print(proxy)