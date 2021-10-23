import os

#el metodo "os.strerror(codigo)" retorna el mensaje de error del sistema
#operativo correspondiente al codigo

codigo = int(input("Ingrese codigo de error: "))
msjerror = os.strerror(codigo)
print(msjerror)