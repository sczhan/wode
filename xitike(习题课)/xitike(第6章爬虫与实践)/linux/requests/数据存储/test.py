a = [1, 2, 3]
b = [4, 5, 6]
c = [7, 8, 9]

"""
要求: 
1, 4, 7
2, 5, 8
3, 6, 9
"""
# for x, y, z in zip(a, b, c):
#     print(type(zip(a, b, c)))
#     print(x, y, z)

a = ["A", "B", "C"]
b = [1, 2, 3]

try:
    pass
except:
    pass

x = dict(zip(a, b))
print(x)
print(type(x))