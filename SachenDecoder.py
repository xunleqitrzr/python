f = open("C:/Users/home/PyCharmProjects/PythonCoding/PythonHacking/SachenDecoder.py",
         encoding="ISO-8859-1", mode="r")
#f.write(".lol dateien sind unlogisch und dienen nur der unterhaltung. daher ist ergibt dieser text keinen sinn und wird sich selbstzerstören in 3........2.........1........... BUUUUUUUM!!!")
try:
    byte = f.read(1)
    str = ""
    while byte != "":
        str = str + byte
        byte = f.read(1)
    print(str)
finally:
    f.close()
