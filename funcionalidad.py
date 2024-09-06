import numpy as np

class Encriptador:
    def __init__(self, clave):
        """
        Inicializa el encriptador con una clave y calcula su inversa.
        """
        self.clave = np.array(clave)
        self.inversa_clave = np.linalg.inv(self.clave)

    def encriptar(self, mensaje):
        """
        Encripta un mensaje utilizando la clave.
        """
        mensaje_vector = self._convertir_a_vector(mensaje)
        mensaje_encriptado = np.dot(self.clave, mensaje_vector)
        return mensaje_encriptado

    def desencriptar(self, mensaje_encriptado):
        """
        Desencripta un mensaje encriptado utilizando la inversa de la clave.
        """
        mensaje_vector = np.dot(self.inversa_clave, mensaje_encriptado)
        mensaje_desencriptado = self._convertir_a_texto(mensaje_vector)
        return mensaje_desencriptado

    def _convertir_a_vector(self, mensaje):
        """
        Convierte un mensaje de texto a un vector numérico.
        """
        mensaje_vector = [ord(char) for char in mensaje]
        while len(mensaje_vector) % self.clave.shape[0] != 0:
            mensaje_vector.append(0)
        return np.array(mensaje_vector).reshape(-1, self.clave.shape[0]).T

    def _convertir_a_texto(self, mensaje_vector):
        """
        Convierte un vector numérico a un mensaje de texto.
        """
        mensaje_vector = mensaje_vector.T.flatten()
        mensaje = ''.join(chr(int(round(num))) for num in mensaje_vector if num != 0)
        return mensaje

def tamaño_matriz(matriz):
    """
    Verifica si la matriz es de tamaño 2x2.
    """
    return len(matriz) == 2 and all(len(fila) == 2 for fila in matriz)

def recibir_matriz():
    """
    Recibe una matriz 2x2 del usuario.
    """
    clave = []
    for _ in range(2):
        fila = []
        for _ in range(2):
            valor = int(input("Ingrese un valor de la clave (total de 4 valores): "))
            fila.append(valor)
        clave.append(fila)
    print("La clave ingresada es:", clave)
    return clave

def verificar_caso(clave, mensaje_original, mensaje_esperado):
    encriptador = Encriptador(clave)
    mensaje_encriptado = encriptador.encriptar(mensaje_original)
    mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
    
    if mensaje_encriptado == mensaje_esperado and mensaje_desencriptado == mensaje_original:
        print(f"Prueba con clave {clave} y mensaje '{mensaje_original}' PASÓ.")
    else:
        print(f"Prueba con clave {clave} y mensaje '{mensaje_original}' FALLÓ.")
        print(f"Mensaje encriptado: {mensaje_encriptado}")
        print(f"Mensaje desencriptado: {mensaje_desencriptado}")
