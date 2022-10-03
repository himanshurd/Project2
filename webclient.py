import socket  
import sys 

#Request from the client
request = "GET / HTTP/1.1\r\nHost: example.com\r\nConnection: close\r\n\r\n" 

s = socket.socket()
s.connect(("example.com",80))
s.sendall(request.encode("ISO-8859-1"))
data = s.recv(4096).decode("ISO-8859-1")
while len(data) > 0:
    print(sys.argv, data)
    print(sys.argv[1])
    data = s.recv(4096)
s.close()