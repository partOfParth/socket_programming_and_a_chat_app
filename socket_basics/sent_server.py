import socket
import time


HEADERSIZE = 10


with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as soc:
    
    soc.bind( (socket.gethostname(), 50000)) #Bind socket to host and a port so this is where someone can connect to.
    soc.listen(2) #The max number of connections allowed at a time.
    
    while True: # We are listening forever....
    
        conn, addr = soc.accept() # Gets a connection
        print(f'Connection established to {addr}')
        
        msg = 'Welcome to the server!'
        #print(f'{len(msg):<10}'+msg)
        msg = f'{len(msg):<{HEADERSIZE}}'+msg
        
        conn.send(bytes(msg, 'utf-8'))
        #conn.close()
        
        while True:
            time.sleep(3)
            msg = f'The time is {time.time()}'
            msg = f'{len(msg):<{HEADERSIZE}}'+msg
            conn.send(bytes(msg, 'utf-8'))
        