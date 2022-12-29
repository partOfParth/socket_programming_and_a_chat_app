import socket
import time
import pickle

PORT = 65500
HEADERSIZE = 10
#print(msg)

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.bind( ( socket.gethostname(), PORT))
    soc.listen()
    
    while True:
        conn, addr = soc.accept()
        print(f'Connection established to {addr}')
        
        send_dict = {'Sender' : 'Localhost', 'Reciever' : 'You the random system'}

        msg = pickle.dumps(send_dict)
        msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
        
        conn.send(msg)