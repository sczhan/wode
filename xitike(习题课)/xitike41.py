
"""
权重排序
权重是100
价格40%, 销量17%, 评级13% 评论30%
"""
goods =  [{"name": "good1", "price": 200, "sales": 100, "stars":5, "comments": 200},
         {"name": "good2", "price": 250, "sales": 200, "stars":6, "comments": 100},
         {"name": "good3", "price": 300, "sales": 500, "stars": 8, "comments": 300},
         {"name": "good4", "price": 410, "sales": 430, "stars": 10, "comments": 500},
         {"name": "good5", "price": 480, "sales": 305, "stars": 9, "comments": 700},
         {"name": "good6", "price": 600, "sales": 204, "stars": 5, "comments": 500},
         {"name": "good7", "price": 100, "sales": 150, "stars": 4, "comments": 250},
]
print(goods)

# sorted() 进行排序

def my_sorted(agr):
    price = agr["price"]
    sales = agr["sales"]
    stars = agr["stars"]
    comments = agr["price"]
    data = price*0.4 + sales*0.17 + stars*0.13 + comments*0.3
    return data


print(sorted(goods, key=my_sorted))


# 利用lambda排序
good =  [{"name": "good1", "price": 200, "sales":100, "stars":5, "comments": 200},
         {"name": "good2", "price": 250, "sales":200, "stars":6, "comments": 100},
         {"name": "good3", "price": 300, "sales": 500, "stars": 8, "comments": 300},
         {"name": "good4", "price": 410, "sales": 430, "stars": 10, "comments": 500},
         {"name": "good5", "price": 400, "sales": 305, "stars": 9, "comments": 700},
         {"name": "good6", "price": 600, "sales": 204, "stars": 5, "comments": 500},
         {"name": "good7", "price": 100, "sales": 150, "stars": 4, "comments": 250},
]
r = sorted(good, key=lambda x: x["price"]*0.4 + x["sales"]*0.17 + x["stars"]*0.13 + x["comments"]*0.3, reverse=True)
print(r)