from socket import * 
s = socket(AF_INET,SOCK_STREAM) 
host ='127.0.0.1'
port = 40444
message_size = 4096
s.connect((host, port)) 
print(s.recv(message_size)) 
s.close()