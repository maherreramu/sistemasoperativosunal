import os

#El metodo os.getlogin() retorna el nombre del usuario que inicio
#inició sesion en la terminal de control

user = os.getlogin()
print(user)