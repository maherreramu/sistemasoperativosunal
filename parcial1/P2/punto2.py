import socket, json, ssl
import asyncio as asy

#Se define host y puerto
host = 'www.buda.com'
port = 443

#Funcion para recibir datos del servidor. Retorna un string con todos los datos
def rcv(socket) -> str:
    all_data = ''
    while True:
        data = socket.recv(512)
        if len(data) < 1:
            break
        all_data += data.decode()
        #print(data.decode())
    return all_data

#Realiza conección al servidor y sulicitud get. Retorna tupla con datos y api usada
async def get_buda(req: int) -> str:
    requests = ['markets', 'markets/BTC-CLP', 'markets/btc-clp/ticker', 'markets/btc-cop/ticker', 'markets/eth-btc/ticker']
    get = 'GET /api/v2/{} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(requests[req], host).encode()

    ctx = ssl.create_default_context()

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(15)
        
        with ctx.wrap_socket(sock, server_hostname=host) as ssock:
            ssock.connect((host, port))
            ssock.send(get)
            return rcv(ssock), requests[req]

#Extrae el json de interes de todos los datos y lo indenta retornando un string
def get_json(data: str) -> str:
    js = data.split('\r\n\r\n')
    js = js[1]
    idt_js = json.dumps(json.loads(js), indent=4, sort_keys=True)
    return idt_js

#Escribe un archivo de texto con los datos de interes y lo nombra referenciando la api
async def write(tupla: tuple):
    task = asy.create_task(tupla)
    data, title = await task
    handler = open(title.replace('/', '_')+'.txt', 'w')
    handler.write(get_json(data))

#Main principal
async def main():
    #Mediante la librería asyncio se crean corutinas para acceder a los datos solicitados y escribirlos
    await asy.create_task(write(get_buda(2)))
    await asy.create_task(write(get_buda(3)))
    await asy.create_task(write(get_buda(4)))

asy.run(main())