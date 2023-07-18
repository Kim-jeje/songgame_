# from socket import *
#
# clientSock = socket(AF_INET, SOCK_STREAM)
# clientSock.connect(('127.0.0.1', 8080))
#
# print('연결 확인 됐습니다.')
# clientSock.send('I am a client'.encode('utf-8'))
#
# # print('메시지를 전송했습니다.')
# #
# # data = clientSock.recv(1024)
# # print('받은 데이터 : ', data.decode('utf-8'))
#
# while True:
#     recvData = clientSock.recv(1024)
#     print('상대방 :', recvData.decode('utf-8'))
#
#     sendData = input('>>>')
#     clientSock.send(sendData.encode('utf-8'))

from socket import *
import threading
import time


def send(sock):
    while True:
        sendData = input('>>>')
        sock.send(sendData.encode('utf-8'))


def receive(sock):
    while True:
        recvData = sock.recv(1024)
        print('상대방 :', recvData.decode('utf-8'))


port = 8081

clientSock = socket(AF_INET, SOCK_STREAM)
clientSock.connect(('127.0.0.1', port))

print('접속 완료')

sender = threading.Thread(target=send, args=(clientSock,))
receiver = threading.Thread(target=receive, args=(clientSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass