from socket import *
from multiprocessing import process

#服务器地址
ADDR = ("127.0.0.1",8000)
def login(sock):
    while True:
        name = input("Name:")
        #给服务端发送请求
        msg = "L " + name
        sock.sendto(msg.encode(),ADDR)

        #等待结果
        result,addr = sock.recvfrom(128)
        #约定OK作为请求成功的标志
        if result.decode() == b'ok':
            print("进入聊天室")
            break
        else:
            print("该用户已存在")


def main():
    sock = socket(AF_INET,SOCK_DGRAM)
    # sock.sendto("测试信息:".encode(),ADDR)


if __name__ == '__main__':
    main()