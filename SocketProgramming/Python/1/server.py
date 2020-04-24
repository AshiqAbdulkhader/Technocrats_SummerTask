import socket                                       #import socket library
f=open(r"data_log.txt","a+")                        #open file data_log.txt with file mode a+. a+ allows reading and appending of file
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #create socket instance for server
s.bind(('0.0.0.0',8080))                            #bind server with the specified ip and port
s.listen(5)                                         #sets the server for listening for connection request. the paramter is time of listening in seconds
while True:                                         #if connection is established
    con,add=s.accept()                              #create an instance of the connection
    while True:
        data=con.recv(4096).decode()                #receive the data from client and decode it
            if not data:                            #if data is not availale
            break                                   #break
        f.write(data)                               #else write the message to the file
        con.send('String Received at server')       #send an acknowledgement message to the client
    f.close()                                       #close file
    con.close()                                     #close connection
    
