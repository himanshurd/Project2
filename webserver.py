import socket  
import sys 

s = socket.socket()
s.bind(('', int(sys.argv[1])))
s.listen()

while True:
    new_conn = s.accept()
    new_socket = new_conn[0]
    req = new_socket.recv(4096)
    while True:
        if "\r\n\r\n" in req.decode():
            break

    request = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: 6\r\nConnection: close\r\n\r\nHello!\r\n"
    new_socket.sendall(request.encode())
    print("Socket is closed")
    new_socket.close()