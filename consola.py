from funcionalidad import *
if __name__ == "__main__":
    clave = recibir_matriz()
    while not tamaño_matriz(clave):
        print("La matriz ingresada no cumple los requerimientos.")
        clave = recibir_matriz()

    encriptador = Encriptador(clave)
    opcion = int(input("Ingrese 1 si desea encriptar y 2 si desea desencriptar: "))
    while opcion not in [1, 2]:
        print("Ingrese una opción válida.")
        opcion = int(input("Ingrese 1 si desea encriptar y 2 si desea desencriptar: "))

    if opcion == 1:
        mensaje = input("Ingrese el mensaje a encriptar: ")
        mensaje_encriptado = encriptador.encriptar(mensaje)
        print("Mensaje encriptado:", mensaje_encriptado)
    elif opcion == 2:
        mensaje_encriptado = np.array(eval(input("Ingrese el mensaje encriptado (como lista de listas): ")))
        mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
        print("Mensaje desencriptado:", mensaje_desencriptado)