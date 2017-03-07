import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#s.bind(("localhost", 12234))
s.connect(("localhost",10000))
tm = s.recv(1024)                                    

#s.close()

print(tm)
s.close()