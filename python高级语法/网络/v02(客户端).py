
"""
Client端流程:
            1. 建立通信的socket
            2. 发送内容到指定服务器
            3. 接受服务器给定的反馈内容
"""
import socket


def clientFunc():
    """
    客户端
    :return:
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    text = "l love you"

    # 发送的数据必须是bytes格式
    data = text.encode()

    # 发送
    sock.sendto(data, ("127.0.0.1", 7852))

    data1, addr = sock.recvfrom(200)

    data2 = data1.decode()

    print(text)
    print(data2)


if __name__ == "__main__":
    clientFunc()
