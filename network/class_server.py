
# class Server:
#     HOST = '127.0.0.1'
#     PORT = 9999
#     BUFFER = 10000
#     FORMAT = 'utf-8'
#     HEADER_LENGTH = 30

# from socket import *
#
# serverSock = socket(AF_INET, SOCK_STREAM)
# serverSock.bind(('', 8080))
# serverSock.listen(1)
#
# connectionSock, addr = serverSock.accept()
#
# print(str(addr),'에서 접속이 확인되었습니다.')
#
# # data = connectionSock.recv(1024)
# # print('받은 데이터 : ', data.decode('utf-8'))
# #
# # connectionSock.send('I am a server. I receivd message'.encode('utf-8'))
# # print('메시지를 보냈습니다.')
#
# while True:
#     sendData = input('>>>')
#     connectionSock.send(sendData.encode('utf-8'))
#
#     recvData = connectionSock.recv(1024)
#     print('상대방 :', recvData.decode('utf-8'))

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

serverSock = socket(AF_INET, SOCK_STREAM)
serverSock.bind(('', port))
serverSock.listen(1)

print('%d번 포트로 접속 대기중...'%port)

connectionSock, addr = serverSock.accept()

print(str(addr), '에서 접속되었습니다.')

sender = threading.Thread(target=send, args=(connectionSock,))
receiver = threading.Thread(target=receive, args=(connectionSock,))

sender.start()
receiver.start()

while True:
    time.sleep(1)
    pass