import socket

mensajes = []

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('0.0.0.0', 9999))

print("Servidor UDP escuchando en el puerto 9999...")

while True:
    try:
        data, direccion = server.recvfrom(1024)
        recibido = data.decode()

        partes = recibido.split(":", 1)
        mensaje = partes[0]
        remitente = partes[1] if len(partes) > 1 else "desconocido"

        for fila in range(1):
            mensajes.append([])
            for columna in range(2):
                if columna == 0:
                    mensajes[len(mensajes)-1].append(mensaje)
                else:
                    mensajes[len(mensajes)-1].append(remitente)

        print("\n--- Mensajes almacenados ---")
        for f in mensajes:
            for c in f:
                print(c)
            print()

        respuesta = (
            f"Mensajes almacenados: {len(mensajes)}\n"
            f"Último mensaje: {mensaje}\n"
            f"Remitente: {remitente}"
        )

        server.sendto(respuesta.encode(), direccion)

    except Exception as e:
        print("Error en el servidor:", e)
