import socket  
import threading  
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#参数1：可以有AF_INET(基于ip，不同服务器进行通信)
#             AF_UNIX(基于文件，在本机通信)
#参数2：可以有SOCK_STREAM(tcp/ip协议)
#             SOCK_DGRAM (udp协议)
s.bind(("127.0.0.1",8088))  #绑定端口和ip
s.listen(10)  #请求队列为10
sock,addr=s.accept()  
temp=True  
def rec(sock):  
    global temp  #设置全局变量
    while temp:  
        t=sock.recv(1024).decode('utf8')  #函数的核心语句就一条接收方法
        #接受1024个数据
        if t == "quit":  
            temp=False  
        print(t)  
trd=threading.Thread(target=rec,args=(sock,))  #创建一个线程
#target方法名  args参数名
trd.start()  
while temp:  
    t=input()  
    sock.send(t.encode('utf8'))  
    if t == "quit":  
        temp=False  
s.close() 
