import os

#El metodo "os.environ" mapea las varibles del entorno
#retornando un diccionario de estas

environ = os.environ

input("Oprima Enter para ver informacion basica del entorno")

for val in environ:
    print(val, " = ", environ[val]) 