import socket, json
import asyncio as asy


async def modificador(tipo: int, text: str):
    if tipo > 3 or tipo < 0:
        raise Exception('Opción no encontrada')

    switch = {
        0: text.capitalize(),
        1: text.lower(),
        2: text.upper(),
        3: text.title()
    }
    await asy.sleep(3)
    return switch[tipo]


HOST = '127.0.0.1'
PORT = 65432        

async def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        def captador():
            text = ''
            while True:
                data = conn.recv(1024)
                if data.decode()[0] == chr(1):
                    break
                text += data.decode()
            return text

        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('Connected by', addr)

            text = captador()

            opcion = int(captador())
                
            task = asy.create_task(modificador(opcion, text))
            nuevo = await task
            conn.sendall(nuevo.encode())
asy.run(main()) 