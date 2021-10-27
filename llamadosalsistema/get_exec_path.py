import os

#El metodo os.get_exec_path() retorn una lista de directorios donde se puede
#buscar un ejecutable por nombre

lista = os.get_exec_path()

for path in lista:
    print(path)