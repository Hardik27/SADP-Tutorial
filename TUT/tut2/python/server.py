import socket
import sys
from clientThread import clientThread

host='localhost'
port=5454

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((host, port))
except server.error:
    print("Connection Problem. ")
    sys.exit();
print("Server Bound...")

s.listen(10)

print("Server Started...")

while True:
    client,addr=s.accept()
    print("Connected with " + str(addr[0]) + " : " + str(addr[1]))
    user=clientThread(client)
    user.start()

s.close()
#input()
