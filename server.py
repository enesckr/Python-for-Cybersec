import socket

host = "127.0.0.1"
port = 2121

with socket.socket() as soket:
    soket.bind((host, port))
    soket.listen()
    conn, address = soket.accept()
    with conn:
        print("Connection successful:", address)
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
