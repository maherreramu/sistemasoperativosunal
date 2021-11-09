import socket, sys
from time import sleep

host = 'localhost'
port = 21

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
def coneccion():
    print('conectando...')
    try:
        s.connect((host, port))
        print('Se realizo coneccion con el servidor')
    except:
        print('No se pudo realizar coneccion con el sevidor')

def listar():
    print('solicitando lista...\n')
    try:
        s.send('LIST'.encode())
    except:
        raise Exception('No se pudo realizar peticion al sevidor')

    lista = ''
    while True:
        try:
            data = s.recv(1024).decode()
            lista += data
            if data[len(data)-1] == chr(1):
                break
            if len(data) < 1:
                raise Exception
        except Exception:
            print('No se recibió confirmación de finalización de envío por el servidor')
            return
    lista = lista.split('\r\n\r\n')
    print(lista[0])
    return

def cargar(dir: str):
    print('Cargando archivo...')
    ldir = dir.split('/')
    name = ldir[len(ldir)-1]
    print('nombre del archivo: ',name)

    try:
        handler = open(dir, 'rb')
    except:
        print('Archivo no encontrado')
        return

    try:
        s.send('UPLD'.encode())
    except:
        print('No se pudo realizar peticion al sevidor')
        return
        
        
    name = name+'\r\n\r\n'+chr(1)
    try:
        s.send(name.encode())
        print('Informacion del archivo enviada')
    except:
        print('No se pudo enviar informacion del archivo')
        return

    try:
        data = handler.read(1024)
    except:
        print('No se pudo leer el archivo')
        handler.close()
        return

    try:
        while data:
            s.send(data)
            data = handler.read(1024)
        print('Archivo enviado')
    except:
        print('No se pudo enviar el archivo')
        handler.close()
        return
    handler.close

    try:
        flag = s.recv(35).decode()
    except socket.timeout as e:
        err = e.args[0]
        if err == 'timed out':
            print(err,'- No se recibio confirmacion del servidor')
    if flag == '1':
        print('Archivo cargado staisfactoriamente')
    else:
        print('El archivo no pudo cargarse')
    return

def descargar(name: str):
    try:
        s.send('DWLD'.encode())
    except:
        print('No se pudo realizar la peticion al sevidor')
        return

    n = name+'\r\n\r\n'+chr(1)
    try:
        s.send(n.encode())
        print('Nombre del archivo enviado')
    except:
        print('No se pudo enviar nombre del archivo')
        return

    try:
        flag = s.recv(35).decode()
    except socket.timeout as e:
        err = e.args[0]
        if err == 'timed out':
            print(err,'- No se recibio confirmacion del servidor')
    if flag == '1':
        print('Archivo encontrado')
    else:
        print('Archivo no encontrado')
        return
    
    print('Descargando...')

    file = b''
    er = False
    flag = ''
    while True:
        try:
            data = s.recv(1024)
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
        s.send(flag.encode())
        return

    try:
        handler = open(name, 'wb')
        handler.write(file)
        print('Archivo recibido y guardado')
    except:
        flag = '-1'
        print('No se pudo escribir el archivo')
    handler.close()

    s.send(flag.encode())
    return

def salir():
    try:
        s.send('QUIT'.encode())
    except:
        print('salgo pero no estoy conectado')
        pass
    print('saliendo...')
    sys.exit(0)

def comandos():
    comands = {
        'CONN': '-Realiza coneccion con el servidor con servidor',
        'LIST': '-Solicitar listado de archivos en el servidor',
        'UPLD': 'UPLD *dir archivo* -Carga archivo ubicado en dir al servidor',
        'DWLD': 'DWLD *nombre archivo* -Descarga archivo del servidor',
        'QUIT': '-Salir del sistema'
    }
    print('comandos')
    for key in comands:
        print(key,': ',comands[key] )
    return

comandos = {
    'COMD': comandos,
    'CONN': coneccion,
    'LIST': listar,
    'UPLD': cargar,
    'DWLD': descargar,
    'QUIT': salir
}

while True:
        intrc = input('\nIngrese un comando o COMD para ver lista de comandos\n').strip()
        try:
            if len(intrc) > 4:
                comandos[intrc[:4].upper()](intrc[4:].lstrip())
            elif intrc:
                comandos[intrc.upper()]()
            else:
                print('Por favor escriba un comando')
        except SystemExit:
            sys.exit(0)
        except:
            print('Comando no reconocido')