# import requests, json
#
# url = "http://www.endata.com.cn/API/GetData.ashx?"
# form_data={
#     'movieId': '685447',
#     'MethodName':'BoxOffice_GetMovieData_Details'
# }
# # 伪装头部
# headers ={
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
# 'Content-Length': '56'
# }
# # 转换数据
# data = requests.post(url, data=form_data, headers=headers).text
# # data.encoding = "gbk"
# jsons = json.loads(data)
# for j in jsons["Data"]["Table"]:
#     print(j["MovieDyan"].split("|")[0])
