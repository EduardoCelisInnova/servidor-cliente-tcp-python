# Configuracion del servidor para conectarse.

print("Configuracion del servidor para conexion.")

import socket

# Crear socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#server.settimeout(5)

# Asociar Ip y Puerto
server.bind(("127.0.0.1", 8888))

# Escuchar ( maximo 1 conexion en espera)
server.listen(1)

print("Servidor esperando conexion en el port 8888...")

# Esperar a que el cliente se conecte (Se bloquea aqui)
cliente, direccion = server.accept()

print(f"Cliente conectado desde: {direccion}")

#Enviar mensaje
cliente.send(b"Hola, Cliente")

#cierre
cliente.close()
server.close()

