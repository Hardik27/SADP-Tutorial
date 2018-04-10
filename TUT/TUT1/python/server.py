import calculator
import socket

host='localhost'
port=5454

s=socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host, port))
print("Server Started...")

while True:
    data,addr = s.recvfrom(1024)
    data=data.decode('utf-8')
    if data == 'q':
        break
    print(data)
    ans= calculator.infix(data)
    #print("Server: ",ans)
    print("Sending ans to Client. ")
    s.sendto(ans.encode('utf-8'), addr)
s.close()
#input()
