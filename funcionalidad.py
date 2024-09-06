imimport numpy as np

class ErrorExepciones(Exception):
    def __init__(self, mensaje="La matriz es singular (no invertible)."):
        self.mensaje = mensaje
        super().__init__(self.mensaje)

class Encriptador:
    def __init__(self, clave):
        """
        Inicializa el encriptador con una clave y calcula su inversa.
        Lanza ValueError si la clave no tiene inversa.
        """
        self.clave = np.array(clave)
        if np.linalg.det(self.clave) == 0:
            raise ValueError("La matriz no tiene inversa por lo que no se puede usar como clave")
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
        Lanza ValueError si el mensaje encriptado no es válido.
        """
        if mensaje_encriptado.shape[0] != self.clave.shape[0]:
            raise ValueError("El mensaje encriptado no es válido para la clave proporcionada")
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
    if len(matriz) == 2 and all(len(fila) == 2 for fila in matriz):
        return True
    else:
        raise ValueError("La matriz debe ser de tamaño 2x2")

def matriz_no_singular(matriz):
    """
    Verifica si la matriz no es singular (es decir, tiene una inversa).
    Lanza una excepción ValueError si la matriz es singular.
    """

    try:
        if np.linalg.det(matriz) != 0:
            return True
        else:
            raise ValueError("La matriz no tiene inversa por lo que no se puede usar como clave")
    except np.linalg.LinAlgError as e:
        raise ValueError(f"Error al calcular el determinante: {e}")
