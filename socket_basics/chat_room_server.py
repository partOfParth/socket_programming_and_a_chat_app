import socket
import select

HEADERLENGTH = 10
HOSTIP = '127.0.0.1'
PORT = 65432

with socket.socket( socket.AF_INET, socket.SOCK_STREAM) as soc:
    soc.setsockopt( socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    soc.bind( (HOSTIP, PORT))
    soc.listen()
    
    socket_list = [soc]
    
    clients = {}
    
    
    def receive_message( client_socket):
        try:
            message_header = client_socket.recv(HEADERLENGTH)
            
            if not len(message_header):
                return  False
            
            message_len = int(message_header.decode('utf-8'))
            
            return {'header' : message_header, 'data' : client_socket.recv( message_len)}
            
        except:
            return False 


    while True:
        read_sockets, _, exception_sockets = select.select( socket_list, [], socket_list)
        
        for notificed_socket in read_sockets:
            if notificed_socket == soc:
                client_socket, client_addr = soc.accept()
                
                user = receive_message( client_socket)
                
                
                if not user:
                    continue
                
                socket_list.append( client_socket)
                clients[client_socket] = user
                
                print(f"Accepted the connection from {client_addr} with usernaeme {user['data'].decode('utf-8')}")
                
            else:
                message  = receive_message( notificed_socket)
                
                if not message:
                    print(f"Closed connection from {clients[notificed_socket]['data'].decode('utf-8')}")
                    socket_list.remove( notificed_socket)
                    del clients[notificed_socket]
                    continue
                
                user = clients[notificed_socket]
                print(f"Received message from {user['data'].decode('utf-8')} the message {message['data'].decode('utf-8')}")
                
                for client_socket in clients:
                    if client_socket != notificed_socket:
                        client_socket.send(user['header'] + user['data'] + message['header'] + message['data'])
                        
        for notificed_socket in exception_sockets:
            socket_list.remove(notificed_socket)
            del clients[notificed_socket]
        
        
