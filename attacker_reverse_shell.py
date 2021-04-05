import socket

host = "0.0.0.0"
port = 1535
soket = socket.socket()
soket.bind((host, port))
soket.listen()
conn, address = soket.accept()
print("Connection established : ", str(conn))
message = "Connection established".encode(encoding="utf8")
conn.send(message)
while True:
    command = input("Command:",)
    conn.send(command.encode(encoding="utf8"))
    if command.lower() == "exit":
        print("Exiting, bye ...")
        break
    res = conn.recv(4096).decode()
    print(res)
conn.close()
soket.close()
