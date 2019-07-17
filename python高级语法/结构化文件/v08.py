
import json

date = {"name": "sgg", "age": 15}

with open("t.json", "w")as f:
    json.dump(date, f)

with open("t.json", "r")as f:
    d = json.load(f)
    print(d)