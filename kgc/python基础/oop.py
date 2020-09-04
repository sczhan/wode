#
# class Preson():
#     def __init__(self, name, weapons="", blood="100"):
#         self.name = name
#         self.blood = blood
#         self.weapons = weapons
#         print("创建名为{}的玩家对象".format(self.name))
#
#     def equipment(self, weapons):
#         print("{}装备了杀伤力为{}的{}".format(self.name, weapons.lethality, weapons.type))
#
#     def attack(self, preson1, weapons, preson2):
#         # print("{}使用{}攻击了{},造成了{}伤害".format(self.name, weapons.type, preson.name, weapons.lethality))
#         # preson.blood = int(preson.blood) - int(weapons.lethality)
#         # print("{}还剩{}点血".format(preson.name, preson.blood))
#         weapons.attack_preson(preson1, weapons, preson2)
#
#
# class Weapons():
#     def __init__(self, type, lethality):
#         self.type = type
#         self.lethality = lethality
#
#     def attack_preson(self, preson1, weapons, preson2):
#         print("{}使用{}攻击了{},造成了{}伤害".format(preson1.name, weapons.type, preson2.name, weapons.lethality))
#         preson2.blood = int(preson2.blood) - int(weapons.lethality)
#         print("{}还剩{}点血".format(preson2.name, preson2.blood))
#
#
# w1 = Weapons("平底锅", 5)
# preson1 = Preson("大漠孤烟")
# preson2 = Preson("大反派")
# preson1.equipment(w1)
# preson1.attack(preson1, w1, preson2)
# preson1.attack(preson1, w1, preson2)


# class Preson():
#     def __init__(self, attack, skills):
#         self.attack = attack
#         self.skills = skills
#
#     def normal_attack(self):
#         print("使用普通攻击")
#
#     def skills_attack(self):
#         print("使用技能攻击")
#
#
# class Guanyu(Preson):
#     def normal_attack(self):
#         print("关羽使用普通攻击, 攻击力为{}".format(self.attack))
#
#     def skills_attack(self):
#         print("关羽使用特殊攻击{}".format(self.skills))
#
#
# guanyu = Guanyu(10, "单刀赴会")
# guanyu.normal_attack()
# guanyu.skills_attack()
#
#
# class Lvbu(Preson):
#     def normal_attack(self):
#         print("吕布使用普通攻击, 攻击力为{}".format(self.attack))
#
#     def skills_attack(self):
#         print("吕布: 谁敢战我!!!")
#         print("吕布使用特殊攻击{}".format(self.skills))
#
#
# lvbu = Lvbu(15, "贪狼之握")
# lvbu.normal_attack()
# lvbu.skills_attack()


class Phones():
    def call(self):
        print("使用功能机打电话")

class IPhone(Phones):
    def call(self):
        print("使用苹果手机打电话")

class APhone(Phones):
    def call(self):
        print("使用安卓手机打电话")

class Preson():
    def use_phone_call(self, phone):
        phone.call()


p = Preson()
phone = Phones()
iphone = IPhone()
aphone = APhone()
p.use_phone_call(phone)
p.use_phone_call(iphone)
p.use_phone_call(aphone)