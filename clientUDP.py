import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

mensaje = input("Mensaje: ")
remitente = input("Nombre: ")

cadena = f"{mensaje}:{remitente}"

try:
    client.sendto(cadena.encode(), ('127.0.0.1', 9999))
    data, _ = client.recvfrom(1024)
    print("\nRespuesta del servidor:")
    print(data.decode())

except Exception as e:
    print("ERROR:", e)
finally:
    client.close()
