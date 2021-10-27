import os

#Al igual que la función "environ" retorna un mapa de la varables del entorno
#pero en bytes

if os.supports_bytes_environ:
    environb = os.environb()
    print(environb)
else:
    print("función no soportada")