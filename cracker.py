import zipfile
import itertools
import string
from threading import Thread

def crack(zip, pwd):
    try:
        zip.exctractall(pwd=str.encode(pwd))
        print('Passwort erfolgreich gefunden. Pawwort ist: ' + pwd)
    except Exception:
        pass

zipFile = zipfile.ZipFile("C:/Users/home/Desktop/ll.zip")
myLetters = string.ascii_letters + string.digits + string.punctuation
for i in range(3, 4):
    for j in map(''.join, itertools.product(myLetters, repeat=i)):
        t = Thread(target=crack, args=(zipFile, j))
        t.start()
        print(j)
