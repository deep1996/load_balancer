import socket                                         


serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 

port = 11000                                           

# bind to the port
serversocket.bind(('localhost', port))                                  

# queue up to 10 requests
serversocket.listen(10)                                           

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()  
    print "a new client is connected now"    
    clientsocket.send("hi, this message is being sent by server 1")
    clientsocket.close()
