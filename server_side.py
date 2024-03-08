from socket import * 
s = socket(AF_INET,SOCK_STREAM) 
print ("The socket created")
host ='127.0.0.1'
port = 40444
s.bind((host, port)) 
print("The socket binded to ",port) 
s.listen(1)
print ("The socket is listening") 
while True:
    connection , address = s.accept() 
    print ('The server get connection from address',address)
    connection.send(b'Thank you for connecting with the server')
    connection.close()
