import socket 
import threading 

bind_ip = '192.168.43.81'
bind_port = 80

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)
print ("[*] listening on %s:%d" % (bind_ip, bind_port))

#client thread 
def handle_client(client_socket):
    #client data
    request = client_socket.recv(1014)
    
    print("[*] Recived: %s" % request)

    #Server responce 
    ack = 'hi, im a server'
    client_socket.send(ack.encode())
    print ('sending data')
    client_socket.close()


while True: 
    client,addr = server.accept()
    print ("[*] Accepted connection from %s:%d" % (addr[0], addr[1]))

    #start client thread for incoming data 
    client_handler = threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
