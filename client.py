import socket
import os

def main(server, port):
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((server, port))
        data = input('enter message: ')
        s.sendall(data.encode('utf-8'))
        data = s.recv(1024)
        print(data)
        s.close()


if __name__ == '__main__':
    server = os.getenv('SERVER')
    port = int(os.getenv('PORT'))
    main(server, port)


