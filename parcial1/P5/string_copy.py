
#Fue necesario buscar la variable destino dentro el listado de variables globales
#ya que al reasignar la variable destino de forma directa se realiza localmente.
#Es decir, unicamente dentro de la función.
#Para lograr encontrar la variable destino dentro de el listado de variables globales
#fue necesario hacer una comparación por el id de la variable destino
def str_copy(str1, str2):
    lglobals = globals()
    s2 = ''
    for var in lglobals:
        if id(var) == id(str2):
            s2 = var
            break
    if s2 == '':
        print('Variable destino no creada globalmente')
        return
    lglobals[s2] = ''
    for i in range(len(str1)):
        lglobals[s2] += str1[i]
    return 

str1 = 'Hola mundo'
str2 = ''

str_copy(str1, 'str2')
print(str2)
