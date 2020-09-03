
import requests


def main():
    url_start = "https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput="
    url_parse = "https://www.lagou.com/jobs/positionAjax.json?city=成都&needAddtionalResult=false"
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    }

    # driver = webdriver.Chrome("F:\wode\kgc\python数据爬取\chromedriver.exe")
    # driver.get(url_start)
    # print(driver.page_source)
    # print()
    for x in range(1, 5):
        data = {
            'first': 'true',
            'pn': str(x),
            'kd': ''
                }
    #     s = requests.Session()
    #     s.get(url_start, headers=headers, timeout=3)  # 请求首页获取cookies
    #     cookie = s.cookies  # 为此次获取的cookies
    #     # cookie = cookies
    #     cookie = cookie.get_dict()
    #     # headers = {
    #     #     'Accept': 'application/json, text/javascript, */*; q=0.01',
    #     #     'Referer': 'https://www.lagou.com/jobs/list_%E6%9C%BA%E5%99%A8%E5%AD%A6%E4%B9%A0?labelWords=&fromSearch=true&suginput=',
    #     #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
    #     #     "cookie": "user_trace_token=20200408170451-29a87a1a-2ca8-4d57-9eb9-4d1f0347208d; LGUID=20200408170451-b5c104a1-2e8d-4658-857a-d57c3b9ce74a; _ga=GA1.2.404826130.1586336693; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22%24device_id%22%3A%22171592c18c531d-072a631f34a5b3-6701b35-1327104-171592c18c6346%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; RECOMMEND_TIP=true; index_location_city=%E5%85%A8%E5%9B%BD; JSESSIONID=ABAAABAABEIABCI3DA8B41D6302A195C1441364308EF3AD; WEBTJ-ID=20200614210126-172b2eba339368-0d540fb10511b9-d373666-1327104-172b2eba33a384; Hm_lvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1591928278,1591928499,1591928502,1592139687; _gid=GA1.2.728047838.1592139687; TG-TRACK-CODE=search_code; LGSID=20200615004927-58b40ae5-c02f-4964-8d16-f271589fdc01; PRE_UTM=; PRE_HOST=; PRE_SITE=; PRE_LAND=https%3A%2F%2Fwww.lagou.com%2Fjobs%2Flist%5F%25E6%259C%25BA%25E5%2599%25A8%25E5%25AD%25A6%25E4%25B9%25A0%3FlabelWords%3D%26fromSearch%3Dtrue%26suginput%3D; X_HTTP_TOKEN=01dd9aa456f606ad5104512951e021a7f77e9b9a86; Hm_lpvt_4233e74dff0ae5bd0a3d81c6ccf756e6=1592154019; LGRID=20200615010037-b798c841-f522-405a-bccc-0aadb26991c9; SEARCH_ID=71e70aa255fd4fb1a07b622b94a4faaa"
    #     # }
        response = requests.post(url_parse, data=data, headers=headers, timeout=3)  # 获取此次文本
    #     time.sleep(5)
    #     response.encoding = response.apparent_encoding
        print(response.text)
    #     # text = json.loads(response.text)
    #     # info = text["content"]["positionResult"]["result"]
    #     # for i in info:
    #     #     print(i["companyFullName"])
    #     #     companyFullName = i["companyFullName"]
    #     #     print(i["positionName"])
    #     #     positionName = i["positionName"]
    #     #     print(i["salary"])
    #     #     salary = i["salary"]
    #     #     print(i["companySize"])
    #     #     companySize = i["companySize"]
    #     #     print(i["skillLables"])
    #     #     skillLables = i["skillLables"]
    #     #     print(i["createTime"])
    #     #     createTime = i["createTime"]
    #     #     print(i["district"])
    #     #     district = i["district"]
    #     #     print(i["stationname"])
    #     #     stationname = i["stationname"]



if __name__ == '__main__':
	main()
