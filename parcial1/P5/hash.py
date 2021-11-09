import hashlib, json

def hasher(name: bytes):
    fhash = hashlib.sha256()
    with open(name, 'rb') as handler:
        file = handler.read()
        fhash.update(file)
        return fhash.hexdigest()

archivos = {
    'P1': 'P1/punto1.py',
    'P2': 'P2/punto2.py',
    'P3': 'P3/punto3.py',
    'P4': 'P4/server.py'
}

hashes ={}

for p in archivos:
    hashes[archivos[p][3:]] = hasher(archivos[p])

js = json.dumps(hashes,  indent=4, sort_keys=True)

with open('P5/hash_archivos.txt', 'w') as h:
    h.write(js)

