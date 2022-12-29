import socket

HEADERSIZE = 10

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.connect( (socket.gethostname(), 50000))
    
    #while True:
    full_msg = ''
    new_msg_flg = True
    while True:
        msg = soc.recv(16)
        
        if len(msg) <= 0:
            break
        
        if new_msg_flg:
            print(f'Message length is {msg[:HEADERSIZE]!r}')
            msg_len = int(msg[:HEADERSIZE].strip())
            new_msg_flg = False
        
        
        full_msg += msg.decode('utf-8')
        #print(msg.decode('ASCII'))
        if len(full_msg) - HEADERSIZE == msg_len:
            print('The entire message was recvd, yay!')
            print(full_msg[HEADERSIZE:])
            new_msg_flg = True
            full_msg = ''
            
    
#    print(f'Recieved the message:- {full_msg}')
