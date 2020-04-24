import socket                                        #import socket library
import sys                                           #import sys library
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)   #create an instance of socket for server
s.bind(('0.0.0.0',8080))                             #bind ip and port to the server
s.listen(5)                                          #listen for connection request. the argument is listening time in seconds
con,add=s.accept()                                   #create connection instance when connection is established
while(True):
    option=con.recv(1024).decode()                   #receive option from client and decode it
    option=int(option)                               #convert option to integer
    if option in range(1,5):                         #if option lies between 1 and 4
        con.send('op'.encode())                      #send response 'op' after encoding
        a=con.recv(1024).decode()                    #receive operand 1 from client and decode it
        b=con.recv(1024).decode()                    #receive operand 2 from client and decode it
        a=int(a)                                     #converting operands to integers
        b=int(b)            
        if(option==1):                              #if option is 1                        
            ans=a+b                                 #do addition
        elif(option==2):                            #if option is 2
            ans=a-b                                 #do subtraction
        elif(option==3):                            #if option is 3
            ans=a*b                                 #do multiplication
        elif(option==4):                            #if option is 4
            ans=a/b                                 #do division
        con.send(str(ans).encode())                 #send answer to client after converting to string and encoding
con.close()                                         #close connection
