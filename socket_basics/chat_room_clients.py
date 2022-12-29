import socket
import select
import errno
import sys

HEADERLENGTH = 10
HOSTIP =  '127.0.0.1'
PORT = 65432

my_username = input('ENTER USERNAME')

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as client_scoket:
    client_scoket.connect( (HOSTIP, PORT))
    client_scoket.setblocking(False )
    
    username = my_username.encode( 'utf-8')
    username_header = f"{len(username):<{HEADERLENGTH}}".encode( 'utf-8')
    
    client_scoket.send( username_header + username)
    
    while True:
        message = input(f"{my_username} > ")
        
        if message:
            message = message.encode( 'utf-8')
            message_header = f"{len(message):< {HEADERLENGTH}}".encode( 'utf-8')
            
            client_scoket.send( message_header + message)
        try:    
            while True:
            #Receive other messages
                username_header = client_scoket.recv( HEADERLENGTH)
                
                if not len(username_header):
                    print('Connection closed by the server :(.')
                    sys.exit()
                username_length = int(username_header.decode( 'utf-8'))
                username = client_scoket.recv( username_length).decode( 'utf-8')
                
                message_header = client_scoket.recv( HEADERLENGTH)
                
                message_length = int( message_header.decode( 'utf-8'))
                message = client_scoket.recv( message_length).decode( 'utf-8')
                
                print(f"{username}: {message}")
                
        except IOError as ie:
            if ie.errno != errno.EAGAIN or ie.errno != errno.EWOULDBLOCK:
                print(f"Reading error {str(e)}")
                sys.exit()
            continue
        
        except Exception as e:
            print("General error: ", str(e))
            sys.exit()
            