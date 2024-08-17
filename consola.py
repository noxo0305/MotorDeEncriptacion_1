from funcionalidad import *

clave = recibir_matriz()
while not tamaño_matriz(clave):
    print("la matriz ingresada no cumple los requerimentos")
    clave = recibir_matriz()
encriptador = Encriptador(clave)
print("ingrese 1 si desea encriptar y 2 si deseea desencriptar")
control = int(input("ingrese una opcion:"))
while control != 1 and control != 2:
    print("ingresa una opcion valida")
    print("ingrese 1 si desea encriptar y 2 si deseea desencriptar")
    control = int(input("ingrese una opcion:"))
if control == 1:
    mensaje = str(input("ingrese el mesnaje a incriptar:"))
    mensaje_encriptado = encriptador.encriptar(mensaje)
    print("Mensaje encriptado:", mensaje_encriptado)
if control == 2:
    mensaje = str(input("ingrese el mesnaje a incriptar:"))
    mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
    print("Mensaje desencriptado:", mensaje_desencriptado)