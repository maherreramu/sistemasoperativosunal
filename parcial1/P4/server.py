import socket, os, sys, asyncio
from time import sleep

repo = 'parcial1/P4/Repositorio'
host = 'localhost'
port = 21     
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((host,port))
sock.listen(1)
conn, addr = sock.accept()
conn.settimeout(20)
print('Connected by: ', addr, '\n')

def listar():
    print('Enviando lista de archivos...')
    l = os.listdir(repo)
    lista = ''
    if len(l) > 0:
        lista = l[0]
        for i in l[1:]:
            lista += '\n'+i
    else:
        lista = 'Empty'
    lista += '\r\n\r\n'+chr(1)
    try:
        conn.send(lista.encode())
        print('Lista enviada')
    except:
        print('No se pudo enviar la lista')
    return

def cargar():
    print('Recibiendo archivo...')

    try:
        name = conn.recv(1024).decode()
        print(name)
        if name[len(name)-1] == chr(1):
            name = name.split('\r\n\r\n')[0]
            print('nombre de archivo: ',name)
        else:
            raise Exception
    except Exception:
        print('No se pudo recibir informacion del archivo')
        return

    file = b''
    er = False
    flag = ''
    while True:
        try:
            data = conn.recv(1024)
        except socket.timeout as e:
            err = e.args[0]
            if err == 'timed out':
                if er:
                    break
                er = True
                sleep(1)
                continue
        except socket.error as e:
            print(e)
            flag = '-1'
        else:
            if len(data) < 1:
                break        
        file += data
    if len(file)>0: flag = '1'
    else: flag = '-1'
    if flag =='-1':
        print('No se recibio archivo')
        conn.send(flag.encode())
        return

    try:
        handler = open(repo+'/'+name, 'wb')
        handler.write(file)
        print('Archivo recibido y guardado')
    except:
        flag = '-1'
        print('No se pudo escribir el archivo')
    handler.close()

    conn.send(flag.encode())
    return

def descargar():
    print('Esperando nombre del archivo...')
    flag = ''
    try:
        name = conn.recv(1024).decode()
        if name[len(name)-1] == chr(1):
            name = name.split('\r\n\r\n')[0]
            print(name)
            name = repo+'/'+name
            print('nombre de archivo: ',name)
        else:
            raise Exception
    except Exception:
        print('No se pudo recibir informacion del archivo buscado')
        return

    print('Buscando archivo...')
    try:
        handler = open(name, 'rb')
        print('Archivo encontrado')
        data = handler.read(1024)
        flag = '1'
        conn.send(flag.encode())
    except:
        print('Archivo no encontrado')
        handler.close()
        flag = '-1'
        conn.send(flag.encode())
        return    

    print('Enviando archivo...')

    try:
        while data:
            conn.send(data)
            data = handler.read(1024)
        print('Archivo enviado')
    except:
        print('No se pudo enviar el archivo')
        handler.close()
        return
    handler.close()
    
    try:
        flag = conn.recv(35).decode()
    except socket.timeout as e:
        err = e.args[0]
        if err == 'timed out':
            print(err,'- No se recibio confirmacion del cliente')
    if flag == '1':
        print('Archivo cargado staisfactoriamente')
    else:
        print('El archivo no pudo cargarse')
    return

def salir():
    sys.exit(0)

comandos = {
    'LIST': listar,
    'UPLD': cargar,
    'DWLD': descargar,
    'QUIT': salir
}



while True:
    try:
        intrc = conn.recv(1024).decode()
        print('\ninstruccion recibida: '+intrc)
        comandos[intrc]()
    except socket.timeout as e:
        err = e.args[0]
        if err == 'timed out':
            pass
    except:
        print('Saliendo...')
        sys.exit(0)
    intrc = None

        
    
