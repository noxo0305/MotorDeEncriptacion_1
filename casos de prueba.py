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
clave = [[1, 0], [0, 1]]
encriptador = Encriptador(clave)
mensaje = "Mundo"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #3")
clave = [[4, 1], [2, 2]]
encriptador = Encriptador(clave)
mensaje = "Python"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #4")
clave = [[3, 2], [5, 1]]
encriptador = Encriptador(clave)
mensaje = "Código"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #5")
clave = [[2, 2], [1, 3]]
encriptador = Encriptador(clave)
mensaje = "Prueba"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #6")
clave = [[1, 3], [4, 2]]
encriptador = Encriptador(clave)
mensaje = "Mensaje"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #7")
clave = [[3, 1], [2, 4]]
encriptador = Encriptador(clave)
mensaje = "Encriptar"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #8")
clave = [[2, 4], [1, 3]]
encriptador = Encriptador(clave)
mensaje = "Desencriptar"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #9")
clave = [[1, 2], [3, 3]]
encriptador = Encriptador(clave)
mensaje = "Clave"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba #10")
clave = [[4, 1], [2, 3]]
encriptador = Encriptador(clave)
mensaje = "Seguridad"
mensaje_encriptado = encriptador.encriptar(mensaje)
print("Mensaje encriptado:", mensaje_encriptado)
mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
print("Mensaje desencriptado:", mensaje_desencriptado)

print("caso de prueba fallido #1")
clave = [[1, 2], [3, 4, 5]]  # Clave no es una matriz 2x2
try:
    encriptador = Encriptador(clave)
    mensaje = "Error"
    mensaje_encriptado = encriptador.encriptar(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)
except ValueError as e:
    print("Error: La clave debe ser una matriz 2x2.")

print("caso de prueba fallido #2")
clave = [[1, 2], [3, 4]]
encriptador = Encriptador(clave)
mensaje = "Mensaje demasiado largo para la clave"  # Mensaje demasiado largo
try:
    mensaje_encriptado = encriptador.encriptar(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)
except ValueError as e:
    print("Error: El mensaje es demasiado largo para la clave proporcionada.")

print("caso de prueba fallido #3")
clave = [[0, 0], [0, 0]]  # Clave no invertible
try:
    encriptador = Encriptador(clave)
    mensaje = "Hola"
    mensaje_encriptado = encriptador.encriptar(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)
except np.linalg.LinAlgError as e:
    print("Error: La clave no es invertible. Proporcione una clave válida.")

print("caso de prueba fallido #4")
clave = [[1, 2], [3, 4]]
encriptador = Encriptador(clave)
mensaje = "Hola"
mensaje_encriptado = encriptador.encriptar(mensaje)
mensaje_encriptado[0][0] += 1  # Modificación del mensaje encriptado
try:
    mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)
except ValueError as e:
    print("Error: El mensaje encriptado ha sido modificado y no puede ser desencriptado correctamente.")

print("caso de prueba fallido #5")
clave = [[1, 2], [3, 4]]
encriptador = Encriptador(clave)
mensaje = "Hola"
mensaje_encriptado = encriptador.encriptar(mensaje)
mensaje_encriptado = mensaje_encriptado + 1  # Operación inválida en el mensaje encriptado
try:
    mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)
except TypeError as e:
    print("Error: Operación inválida en el mensaje encriptado.")
