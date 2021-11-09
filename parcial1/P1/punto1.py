
import os
import pandas as pd

def writer(funciones):
    frame_f = pd.DataFrame.from_dict(funciones,)
    st = frame_f.to_string().encode()

    f = os.open('funciones.txt', os.O_RDWR|os.O_CREAT)
    txt = os.write(f, st)
    os.close(f)
    with pd.ExcelWriter('funciones.xlsx') as ex:
        frame_f.to_excel(ex)
    frame_f.to_excel('funciones.xlsx')


chdir = 'El metodo os.chdir(path) solicita como argumento un str con la ruta a la cual se cambiará el espacio de tranajo'
environ = 'El metodo os.environ mapea las varibles del entorno retornando un diccionario de estas'
fs_encode = 'El metodo os.fsencode(filename) codifica el nombre del archivo retornando bytes. El proceso inverso lo realiza os.fsdecode(filename)'
get_exec = 'El metodo os.get_exec_path() retorn una lista de directorios donde se puede buscar un ejecutable por nombre'
get_cwd = 'El metodo os.getcwd() retorna un string con la ruta al directorio de trabajo actual'

description = {
    'Función':['os.chdir', 'os.environ', 'os.fsencode', 'os.get_exec_path', 'os.getcwd'],
    'Descripción':[chdir, environ, fs_encode, get_exec, get_cwd]
}

writer(description)