from funcionalidad import *

print("caso de prueba #1")
clave = [[2, 3], [1, 4]]
encriptador = Encriptador(clave)

mensaje = "Hola"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #2")

clave = [[3, 4], [6, 5]]
encriptador = Encriptador(clave)

mensaje = "mundo"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #3")

clave = [[7, 11], [45, 0]]
encriptador = Encriptador(clave)

mensaje = "salon"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #4")

clave = [[1, 5], [4, 6]]
encriptador = Encriptador(clave)

mensaje = "contraseña"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #5")

clave = [[7, 9], [8, 5]]
encriptador = Encriptador(clave)

mensaje = "alcaldia"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)

mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)