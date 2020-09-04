
number = []
number1 = input("请输入第1个整数: ")
number2 = input("请输入第2个整数: ")
number3 = input("请输入第3个整数: ")
number4 = input("请输入第4个整数: ")
number5 = input("请输入第5个整数: ")
number6 = input("请输入第6个整数: ")
number.append(number1)
number.append(number2)
number.append(number3)
number.append(number4)
number.append(number5)
number.append(number6)

for i in range(0, len(number)):
    for j in range(0, len(number) - i - 1):
        if int(number[j]) > int(number[j+1]):
            number[j],  number[j+1] = number[j+1],  number[j]

print(number)


song = "Twinkle,twinkle,little star," \
       "How I wonder what you are!" \
       "Up above the world so high," \
       "Like a diamond in the sky." \
       "Twinkle,twinkle,little star," \
       "How I wonder what you are!" \
       "When the blazing sun is gone," \
       "When he nothing shines upon," \
       "Then you show your little light," \
       "Twinkle,twinkle,all the night"

songs = song.lower().replace(",", " ").replace("!", " ").replace(".", " ").split(" ")
dict = {}
print(songs)
for i in songs:
    if i in dict.keys():
        dict[i] += 1
    else:
        dict[i] = 1

dict_sort = sorted(dict.items(), key=lambda k: k[1], reverse=True)
print(dict_sort)
for key in dict_sort:
    print(key[0], key[1])