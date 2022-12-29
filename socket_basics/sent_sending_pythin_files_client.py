import socket
import pickle

PORT = 65500
HEADERSIZE = 10

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect( ( socket.gethostname(), PORT))
    while True:
        full_msg = b''
        new_msg_flag = True
        while True:
            msg_recvd = soc.recv(16)
            
            if len(msg_recvd) <= 0:
                break
            
            if new_msg_flag:
                new_msg_flag = False
                print(f'The message received is of length {msg_recvd[:HEADERSIZE]!r}')
                msg_len = int(msg_recvd[:HEADERSIZE])
                
            full_msg += msg_recvd
            
            if len(full_msg) - HEADERSIZE == msg_len:#len(full_msg[HEADERSIZE:]) == msg_len:
                print('Full message recvd')
                print(f'{full_msg[HEADERSIZE:]}')
                
                data_recieved = pickle.loads(full_msg[HEADERSIZE:])
                
                print(data_recieved)
                
                new_msg_flag = True
                full_msg = b''
                
            
