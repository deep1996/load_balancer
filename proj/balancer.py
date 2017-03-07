import socket                                         
import time
import os
import thread
from random import randint

serversocket = socket.socket(
	        socket.AF_INET, socket.SOCK_STREAM) 
          
port = 10000                          

# bind to the port
serversocket.bind(('localhost', port))                                  


serversocket.listen(10)                                           

#variables storing number of connections to each server

#for server 1
a=0

#for server 2
b=0

#for server 3
c=0


#function runs when thread is started
def x(clientsocket,addr):
	global a
	global b
	global c
	use="1"
	to_use=a
	if(b<to_use):
		use="2"
		to_use=b

	if(c<to_use):
		use="3"
		to_use=c

	#c+=1
	#tm = clientsocket.recv(1024)
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	if(use=="1"):
		s.connect(("localhost",11000))
		a+=1
	if(use=="2"):
		s.connect(("localhost",12000))
		b+=1
	if(use=="3"):
		s.connect(("localhost",13000))
		c+=1

	#s.send(tm)
	tm=s.recv(1024)
	
	clientsocket.send(tm)
	gh=randint(5,15)
	time.sleep( gh )
	clientsocket.close()
	s.close()
	if(use=="1"):
		a-=1
	if(use=="2"):
		b-=1
	if(use=="3"):
		c-=1




#server is started 
while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()    
    thread.start_new_thread( x, (clientsocket,addr, ) )
    #currentTime = time.ctime(time.time()) + "\r\n"
    #clientsocket.send(currentTime.encode('ascii'))
    #clientsocket.close()
