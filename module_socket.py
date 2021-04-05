import socket

port_list = []
banner_list = []
file = open("ip.txt", "r")
ip_list = file.read()
file.close()
for ip in ip_list.splitlines():
    print(ip)
    for port in range(1, 25):
        try:
            soket = socket.socket()
            soket.connect((str(ip), int(port)))
            banner = soket.recv(1024)  # 3 way sonrası cevap
            banner_list.append(str(banner))
            port_list.append(str(port))
            soket.close()
            print(port)
            print(banner)
            if "SSH" in str(banner):
                print("System can be Linux or network device")
                log = str(ip) + "\n"
                file = open("linux.txt", "a")
                file.write(log)
                file.close()
        except:
            pass

print(port_list)
print(banner_list)
