import socket
import sys

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error:
    print("Failed to create socket.")
    sys.exit();

print("Socket created.")


host= input("Enter Hostname: ")
port= 5454

IP= socket.gethostbyname(host)

s.connect((IP,port))

print("Connected to " + host)

summary={}

while True:
    expr=input("Enter expression: ")
    s.send(expr.encode('utf-8'))
    if expr == 'q':
        break;
    data= s.recv(1024).decode('utf-8')
    summary[expr]=data
    print("Result: ", data)

print("summary: \n", summary)
s.close()
#input()
