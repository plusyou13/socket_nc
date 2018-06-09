import socket  
import threading  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.connect(("127.0.0.1",8088))  
temp=True  
def rec(s):  
    #global temp  
    while temp:  
        t=s.recv(1024).decode("utf8")  #客户端也同理  
        if t == "quit":  
            temp=False  
        print(t)  
trd=threading.Thread(target=rec,args=(s,))  
trd.start()  
while temp:  
    t=input()  
    s.send(t.encode('utf8'))  
    if t == "quit":  
        temp=False  
s.close()  
