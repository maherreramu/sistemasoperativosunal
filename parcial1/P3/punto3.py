import socket
import asyncio as asy

host = 'localhost'
port = 9000
htmldir = 'html.html'

async def handler(dir):
    try:
        f = open(dir, 'r')
        html = f.read()
        return html
    except Exception:
        print('Direccion de archivo no encontrada')

async def server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        try:
            sock.bind((host,port))
            sock.listen()
            conn, addr = sock.accept()
            print('Connected by: ', addr)
            while True:
                with conn:
                    read = conn.recv(1024).decode()
                    pread = read.split('\n')
                    if len(pread) > 0: 
                        for line in pread: print(line)

                    data = 'HTTP/1.1 200 OK\r\n'
                    data += 'Content-Type: html; charset=utf-8\r\n'
                    data += '\r\n'
                    data += await handler(htmldir)
                    conn.sendall(data.encode())
        except KeyboardInterrupt:
            print('\nApagando por teclado...\n')
            sock.close()
        '''except Exception as e:
            print('Error: ')'''
    
asy.run(server())