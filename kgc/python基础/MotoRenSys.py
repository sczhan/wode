

class MotoVehicle():
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def calRent(self, days):
        zujin = int(days) * int(self.price)
        print("您预定{} {}天,费用合计: {}".format(self.brand, days, zujin))


class Car(MotoVehicle):
    def calRent(self, days):
        zujin = int(days) * int(self.price)
        print("您预定{} {}天,费用合计: {}".format(self.brand, days, zujin))


class Bus(MotoVehicle):
    def calRent(self, days):
        zujin = int(days) * int(self.price)
        print("您预定 {} {}天,费用合计: {}".format(self.brand, days, zujin))


if __name__ == '__main__':
    while True:
        print("------小客汽车租赁系统------")
        car_type = input("请选择车型: 1.轿车  2.客车  0.退出: ")
        if car_type == "1":
            brank_type = input("请选择车型: 1.奔驰  2.宝马  3.别克: ")
            day = input("请输入天数:")
            if brank_type == "1":
                car = Car("奔驰GLC", 600)
                car.calRent(day)
            elif brank_type == "2":
                car = Car("宝马 550i", 500)
                car.calRent(day)
            elif brank_type == "3":
                car = Car("别克林荫大道", 300)
                car.calRent(day)
            else:
                print("请正确输入")
        elif car_type == "2":
            brank_type = input("请选择车型: 1.金杯  2.金龙 : ")
            day = input("请输入天数:")
            if brank_type == "1":
                car = Bus("金杯", 800)
                car.calRent(day)
            elif brank_type == "2":
                car = Bus("金龙", 1500)
                car.calRent(day)
            else:
                print("请正确输入")
        elif car_type == "0":
            print("欢迎下次光临")
            break
        else:
            print("请正确输入")