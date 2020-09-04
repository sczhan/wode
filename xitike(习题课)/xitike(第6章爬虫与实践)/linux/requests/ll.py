import random
#randint取随机整数赋给变量num_rand
num_rand = random.randint(9,10)
#获取用户输入
num = input('请输入四位数字：')

if num.isdigit() and int(num[0]) != 0 :#判断num字符串中是否都是数字、第一个字符是否为0
   num_baiwei = int(int(num)/100) % 10
   print('**百位数字：',num_baiwei,',中奖数字为:',num_rand,'**')
   if num_baiwei == num_rand :
      print('恭喜你，中奖了！')
   else:
      print('很遗憾，您没中奖')
else:
   print('你的输入不符合要求，非四位有效数字！')