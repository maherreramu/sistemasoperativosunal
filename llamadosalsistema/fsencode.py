import os

#El metodo os.fsencode(filename) codifica el nombre del archivo
#retornando bytes. El proceso inverso lo realiza os.fsdecode(filename)

filename = input("Ingrese el nombre del archivo: ")

try:
    encode = os.fsencode(filename)
    print("Codificación del archivo: ", encode)
except Exception:
    print("Error  en la codificación")