import socket  
import sys 
import os
extensions = {'.txt':'text/plain', '.html':'text/html'}

s = socket.socket()
s.bind(('', int(sys.argv[1])))
s.listen()

def getData(data):
    encode_data = data.recv(4096)
    
    req = ""
    while True:
        decoded_req = encode_data.decode("ISO-8859-1")
        req = req + decoded_req

        if decoded_req.find('\r\n\r\n'):
            return req

while True:

    new_conn = s.accept()
    new_socket = new_conn[0]  
    header_data = getData(new_socket) 
    get = header_data.split("\r\n")[0].split()
    
    req_method = get[0]
    req_path = get[1]
    req_protocol = get[2]

    get_file_path = os.path.split(req_path)[1]
    get_file_extension = os.path.splitext(get_file_path)[1]
        
    try:
        with open(get_file_path) as fp:
            data = fp.read()   
            data_length = data.encode("ISO-8859-1")
            length = len(data_length)
            response = ("HTTP/1.1 200 OK\r\nContent-Type: {}\r\nContent-Length: {}\r\n\r\n{}").format(extensions[get_file_extension], length, data)
            new_socket.sendall(response.encode("ISO-8859-1"))
    except:
           response = ("HTTP/1.1 404 Not Found\r\nContent-Type: text/plain\r\nContent-Length: 13\r\nConnection: close\r\n\r\n404 not found")
           new_socket.sendall(response.encode("ISO-8859-1"))
    new_socket.close()
