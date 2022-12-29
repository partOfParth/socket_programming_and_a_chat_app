import socket

HOST = '127.0.0.1'
PORT = 65412

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect(( HOST, PORT))
    soc.sendall(b'Own Message Yohoo!!')
    data = soc.recv(1024)
    
print(f'Recieved {data!r}')