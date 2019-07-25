"""
Server端流程:
    1. 建立socket, socket是负责具体通信的一个实例
    2. 绑定, 为创建的socket指派固定的端口和ip地址
    3. 接受对方发送内容
    4. 给对方发送反馈,
"""

# socket 模块负责socket编程
import socket
import time


# 模拟服务器的函数
def severFunc():
    """
    服务器函数
    :return:
    """
    # 1. 建立socket
    # socket.AF_INET: 使用ipv4协议族
    # socket.SOCK_DGRAM: 使用UDP通信
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 2. 绑定ip和port
    # 127.0.0.1: 这个ip地址代表的是机器本身
    # 7852: 随机指定的端口号
    # 地址是一个tuple类型,(ip, port)
    addr = ("127.0.0.1", 7852)
    sock.bind(addr)

    # 3. 接受对方消息
    # 等待方式为死等, 没有其他可能性
    # recvfrom接受的返回值是一个tuple, 前一项表示数据, 后一项表示地址
    # 参数的含义是缓冲区的大小
    # rst = sock.recvfrom(500)
    date, addr = sock.recvfrom(500)
    print(date)
    print(type(date))

    # 发送过来的数据是bytes格式,必须通过解码才能得到str格式内容
    # decode默认参数书 utf8
    text = date.decode()
    print(type(text))
    print(text)

    # 4. 给对方返回消息
    rsp = "Ich hab keine Hunge"

    # 发送的数据需要编码成bytes格式
    # 默认是utf8  解码和编码的格式要一致
    date = rsp.encode()
    sock.sendto(date, addr)


if __name__ == "__main__":
    print("Starting server........")
    while True:
        try:
            severFunc()
        except Exception as e:
            print(e)
        time.sleep(1)
    print("End server .....")