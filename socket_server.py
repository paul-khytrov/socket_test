import socket
import caesar
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 10082
sock.bind(('', PORT))
sock.listen(100)
print("listening on port" + str(PORT))
conn, addr = sock.accept()
print("connected:", addr)

data = conn.recvmsg(1024)
print(data[0].decode())
if input("Do you want to decode this?Y/n") == "y":
    print(caesar.decode(data[0].decode()))
else:
    pass


