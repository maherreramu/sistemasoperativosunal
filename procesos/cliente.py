import socket
import asyncio as asy

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

acciones = '''
0: Convertir primer caracter en mayuscula
1: Convertir todo el texto en minuscula
2: Convertir todo el texto en mayuscula 
3: Convertir el primer caracter de cada palabra en mayuscula
'''

async def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))

        dir = input("Ingrese dirección del archivo que desea modificar: ")
        with open(dir, 'r') as f:
            #data = f.read(1024)
            while True:
                data = f.read(1024)
                if not data:
                    break
                s.send(data.encode())
                
    
        s.send(bytes(chr(1), 'utf-8'))

        print(acciones)

        while True:
            accion = input('Ingrese el número de acción deseada: ')
            try:
                num = int(accion)
                if num < 0 or num >3:
                    print('Ingrese opcion valida')
                    continue
                break
            except Exception:
                print('Ingrese opcion valida')
                continue

        s.send(accion.encode())
        s.send(bytes(chr(1), 'utf-8'))

        async def respuesta():
            text = ''
            while True:
                data = s.recv(1024)
                if not data:
                    break
                text += data.decode()
            return text

        task = asy.create_task(respuesta())

        print('\nEl archivo está siendo procesado en el servidor...\n')
        text = await task
        try:
            writer(text, dir)
            print('Archivo creado satisfacoriamente!')
        except Exception:
            print('No se ha podido crear el archivo')

def writer(text, dir):
    listdir = dir.split('/')
    listdir[len(listdir)-1] = 'Modicado_'+listdir[len(listdir)-1]
    newdir = ''
    for x in listdir: newdir += x + '/'
    f = open(newdir, 'w')
    f.write(text)

asy.run(main())