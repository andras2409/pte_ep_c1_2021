try:
    fileobject = open("lorem.txt", "r")
    tartalom = fileobject.readline()
    print(tartalom)
    print(type(tartalom))
    print(len(tartalom))
    print(fileobject.tell())
    fileobject.close()
except FileNotFoundError:
    print("Nem található ilyen fájl.")

fileobject2 = open("lorem5.txt", "w")
fileobject2.write("Phyton")
fileobject2.flush()
fileobject2.write("Phyton")
fileobject2.close()