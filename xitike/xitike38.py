
# 6位数随机验证码
# import random
# import string
#
# code = []
# code.append(random.choice(string.ascii_lowercase)) # 保证验证码中有一个小写字母
# code.append(random.choice(string.ascii_uppercase))# 保证验证码中有一个大写字母
# code.append(random.choice(string.digits))# 保证验证码中有一个数字
#
# while len(code)<6:
#     code.append(random.choice(string.ascii_uppercase+string.ascii_lowercase+string.digits))
#
# print(code)
# q_code = "".join(code)
# print(q_code)


# 用户登录验证
import json
import os
import time

count = 0  # 次数为0
exit_flag = False  # 退出标志

while count < 3:
    user = input("请输入用户名:")
    f = user.strip()+".json"
    if os.path.exists(f):
        fp = open(f, "r+", encoding="utf-8")
        j_user = json.load(fp)
        if j_user["status"] == 1:
            print("账号被锁定")
            break
        else:
            expire_dt = j_user["expire_date"]
            current_st = time.time()
            expire_st = time.mktime(time.strptime(expire_dt, "%Y-%m-%d"))

            if current_st > expire_st:
                print('用户过期')
            else:
                while count < 3:
                    pwd = input("请输入密码")
                    if pwd.strip() == j_user["password"]:
                        print("登陆成功")
                        exit_flag = True
                        break
                    else:
                        if count == 2:
                            print("用户登录超过3次, 锁定用户")
                            j_user["status"] = 1
                            exit_flag = True
                            fp.seek(0)
                            fp.truncate()  # 清空文件内容
                            json.dump(j_user, fp)
                        else:
                            print("密码错误")

                    count += 1


    if exit_flag:
        break
    else:
        print("用户名不存在")
        count += 1

#
# f = open("1234.json")
# help(f.seek)
# help(f.truncate)