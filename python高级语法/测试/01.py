
def SayHello(name):
    """
    :param name:
    :return:
    """
    print("l want to say hello with your {0}".format(name))
    print("hello, {0}".format(name))
    print("Done.........")
    return name


if __name__ == "__main__":
    print("***" * 10)
    name = input("Please input your name: ")
    print(SayHello(name=name))
    print("@@@" * 10)
