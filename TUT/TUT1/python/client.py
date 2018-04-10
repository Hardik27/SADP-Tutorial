import socket

host= input("Enter Host: ")
port= 5444

server=('localhost', 5454)
#server=((host,port))  //doesn't work
s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))

expr=input("input expression: ")
while expr!='q':
    s.sendto(expr.encode('utf-8'),server)
    ans,addr=s.recvfrom(1024)
    ans=ans.decode('utf-8')
    print("Answer from server: ",ans)
    expr=input("input expression: ")
s.sendto(expr.encode('utf-8'),server)    
s.close()
#input()
