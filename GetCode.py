import socket
import os
import time

ts = time.sleep

ts(1)
print("")
print("="*50, "Website Code Getter v1.3", "="*50)
ts(1)
print("Write the website name to get the code!")
code = input("Website name: ")
codeIP = socket.gethostbyname(code)
ts(1)
print("SEARCHING...")
ts(2)
print("-"*40, "CODE", "-"*40)
ts(1)
os.system(f"curl {codeIP}")