import sys
import socket
import time
from datetime import datetime

ver = "v4.7"

print ("")
time.sleep(0.5)
print("╔", "═"*40, "PortScanner ", ver, "═"*40, "╗")
time.sleep(0.5)
print("║", " "*37, "github.com/xunleqitrzr", " "*37, "║")
time.sleep(0.5)
print("╚", "═"*98, "╝")
time.sleep(0.5)

print("")
print("Select Type: FTP, SFTP, Webserver, Minecraft, All (without Minecraft)")
print("Note: Please write in Caps!")
type = input("Type: ") #FTP, SFTP...
target = input("Target IP: ") #Ipv4 or domain/text
targetIP = socket.gethostbyname(target)

if type == "FTP":
    print("Scan started - PortScanner " + ver)

    tstart = datetime.now()

    try:
        for p in range(21, 22):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("Open Port " + str(p) + ".")
            sock.close()
    except Exception:
        print("Connecting failed.")
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart
    print("Scan completed in " + str(diff) + "sec.")

#----------------------------------------------------------------

if type == "SFTP":
    print("Scan started - PortScanner " + ver)

    tstart = datetime.now()

    try:
        for p in range(22, 23):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("Open Port " + str(p) + ".")
            sock.close()
    except Exception:
        print("Connecting failed.")
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart
    print("Scan completed in " + str(diff) + "sec.")

#-----------------------------------------------------------------

if type == "WEBSERVER":
    print("Scan started - PortScanner " + ver)

    tstart = datetime.now()

    try:
        for p in range(80, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("Open Port " + str(p) + ".")
            sock.close()
    except Exception:
        print("Connecting failed.")
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart
    print("Scan completed in " + str(diff) + "sec.")
    
#------------------------------------------------------------------

if type == "MINECRAFT":
    print("Scan started - PortScanner " + ver)

    tstart = datetime.now()

    try:
        for p in range(25565, 25566):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("Open Port " + str(p) + ".")
            sock.close()
    except Exception:
        print("Connecting failed.")
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart
    print("Scan completed in " + str(diff) + "sec.")

#------------------------------------------------------------------

if type == "ALL":

    print("Scan started - PortScanner " + ver)

    tstart = datetime.now()

    try:
        for p in range(20, 81):
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = sock.connect_ex((targetIP, p))
            if res == 0:
                print("Open Port " + str(p) + ".")
            sock.close()
    except Exception:
        print("Connecting failed.")
        sys.exit()

    tend = datetime.now()
    diff = tend - tstart
    print("Scan completed in " + str(diff) + "sec.")
    
input ("Press Enter to close")