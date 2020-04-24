import socket                                                               #import socket library
import sys                                                                  #import sys library
c=socket.socket(socket.AF_INET,socket.SOCK_STREAM)                          #create an instance of socket for client
c.connect(('0.0.0.0',8080))                                                 #connect to server
while(True):
    print("1. Addition \n2. Subtraction \n3. Multiplication \n4. Division")
    n=input("Enter your choice : ")                                         #user input of choice
    c.send(str(n).encode())                                                 #send the user input after converting to string and encoding it. it is usually encoded to UTF-8 if no paramter is given
    resp=c.recv(1024).decode()                                              #receive response from server and decode it
    if(resp=='op'):                                                         #if the responce is 'op'
        a=input("Enter first operand : ")                                   #ask user for 1st operand
        b=input("Enter second operand : ")                                  #ask user for 2nd operand
        c.send(str(a).encode())                                             #send 1st operand after converting to string and encoding
        c.send(str(b).encode())                                             #send 2st operand after converting to string and encoding
        answer=c.recv(1024).decode()                                        #receive answer from server and decode it
        answer=int(answer)                                                  #convert answer to integer                                
        print("Answer : ",ans)                                              #print aswer
c.close()                                                                   #close connection
