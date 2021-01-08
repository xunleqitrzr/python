import sys
import socket
import os
from datetime import datetime

ver = "v3.6"

print ("")
print("╔", "═"*40, "PortScanner", ver, "═"*40, "╗")
print("║", " "*98, "║")
print("╚", "═"*98, "╝")

print("")
print("Select Type: FTP, SFTP, Webserver, All")
print("Note: Please write in Caps!")
type = input("Type: ") #FTP, SFTP...
target = input("Target IP: ") #Ipv4 or domain/text
targetIP = socket.gethostbyname(target)

if type == "FTP":
    print("Scan started - PortScanner" + ver)

    tstart = datetime.now()

    try:
        for p in range(20, 22):
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
    print("Scan started - PortScanner" + ver)

    tstart = datetime.now()

    try:
        for p in range(21, 23):
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
    print("Scan started - PortScanner" + ver)

    tstart = datetime.now()

    try:
        for p in range(79, 81):
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

    print("Scan started - PortScanner" + ver)

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