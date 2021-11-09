import sys, os

repo ='parcial1/P4/Repositorio'
name = repo+'/prueba.txt'
print(name)
handler = open(name, 'rb')

#handler = open(repo+'/'+name, 'wb')