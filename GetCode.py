import socket
import os
import time

ts = time.sleep

ts(1)
print("")
print("="*50, "Website Code Getter v1.5", "="*50)
ts(1)
print("Write the website name to get the code!")
code = input("Website URL: ")
codeAfter = input("Path to file (/file.fileEnding)[not required]: ")
print("-"*40, "CODE", "-"*40)
input(print(code + codeAfter))
os.system(f"curl {code + codeAfter}")