import numpy as np


class Encriptador:
    def __init__(self, clave):
        self.clave = np.array(clave)
        self.inversa_clave = np.linalg.inv(self.clave)

    def encriptar(self, mensaje):
        mensaje_vector = self._convertir_a_vector(mensaje)
        mensaje_encriptado = np.dot(self.clave, mensaje_vector)
        return mensaje_encriptado

    def desencriptar(self, mensaje_encriptado):
        mensaje_vector = np.dot(self.inversa_clave, mensaje_encriptado)
        mensaje_desencriptado = self._convertir_a_texto(mensaje_vector)
        return mensaje_desencriptado

    def _convertir_a_vector(self, mensaje):
        mensaje_vector = [ord(char) for char in mensaje]
        while len(mensaje_vector) % self.clave.shape[0] != 0:
            mensaje_vector.append(0)
        return np.array(mensaje_vector).reshape(-1, self.clave.shape[0]).T

    def _convertir_a_texto(self, mensaje_vector):
        mensaje_vector = mensaje_vector.T.flatten()
        mensaje = ''.join(chr(int(round(num))) for num in mensaje_vector if num != 0)
        return mensaje


def tamaño_matriz(matriz):
    if len(matriz) == 2:
        if len(matriz[0]) == 2:
            if len(matriz[1]) == 2:
                return True
    else:
        return False


def recibir_matriz():
    clave = []
    index = 0
    while True:
        index += 1
        i = int(input("ingrese un valor de la clave para un total de 4:"))
        j = int(input("ingrese un valor de la clave para un total de 4:"))
        clave.append([i, j])
        if index == 2:
            break
    print("la clave ingresada es:", clave)
    return clave

