import socket                                       #import socket library
c=socket.socket(socket.AF_INET, socket.SOCK_STREAM)  #create a socket instance
c.connect(('0.0.0.0', 8080))                        #connect client to server using address 0.0.0.0 and port 8080
text=input("Enter a string to send : ")             #Taking user input for message to sen
c.send(str(text).encode())                          #the message is converted to string is encoded. if not parameter is given, it is usually encoded to UTF-8
acknowledgment= c.recv(4096)                        # receive acknowlegement from server. 4096 is maximum size of data that can be received
c.close()                                           #close the socket.
print(acknowledgment)                               #print the acknowledgement
