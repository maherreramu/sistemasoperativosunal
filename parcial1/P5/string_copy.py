
#Fue necesario buscar la variable destino dentro el listado ce variables globales
#ya que al reasignar la variable destino de forma directa se realiza localmente.
#Es decir, unicamente dentro de la función.
#Para lograr encontrar la variable destino dentro de el listado de variables globales
#fue necesario hacer una comparación por el id de la variable destino
def str_copy(str1, str2):
    listOfGlobals = globals()
    s2 = ''
    for name in listOfGlobals:
        if id(name) == id(str2):
            s2 = name
            break
    if s2 == '':
        print('Variable destino no creada globalmente')
        return
    listOfGlobals[s2] = ''
    for i in range(len(str1)):
        listOfGlobals[s2] += str1[i]
    return 

str1 = 'Hola mundo'
str2 = ''

str_copy(str1, 'str2')
print(str2)
