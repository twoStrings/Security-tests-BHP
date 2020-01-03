import socket 

target_host = "localhost"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((target_host, target_port))
cMsg = 'Client socket sending to bhp'
#client.send(cMsg.encode())

response = client.recv(4040)
print(response)
cmd = input()
client.send(cmd.encode())
