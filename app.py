import socket
import os

def main(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                print(data)
                conn.sendall(data+data)

if __name__ == '__main__':
    port = int(os.getenv('PORT'))
    main('0.0.0.0', port)

