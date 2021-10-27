import os, sys

#El metodo "os.chdir(path)" solicita como argumento un str con la ruta
#a la cual se cambiará el espacio de tranajo

actdir = os.getcwd()
print("directorio actual = ", actdir)
path = input("Ingrese la ruta a la cual desea cambiar el directorio de trabajo: ")

try:
    os.chdir(path)
    actdir = os.getcwd()
    print("directorio de trabajo actualizado a: ", actdir)
except Exception as e:
    print("Error: ", os.strerror(e.errno)) 