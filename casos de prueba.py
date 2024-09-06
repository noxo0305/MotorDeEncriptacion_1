import unittest
import numpy as np
from funcionalidad import Encriptador

class TestEncriptador(unittest.TestCase):
    
    def test_funciona_bien_1(self):
        clave = [[2, 3], [1, 4]]
        mensaje_original = "Hola"
        encriptador = Encriptador(clave)
        mensaje_encriptado = encriptador.encriptar(mensaje_original)
        mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
        self.assertEqual(mensaje_desencriptado, mensaje_original)

    def test_funciona_bien_2(self):
        clave = [[1, 0], [0, 1]]
        mensaje_original = "Mundo"
        encriptador = Encriptador(clave)
        mensaje_encriptado = encriptador.encriptar(mensaje_original)
        mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
        self.assertEqual(mensaje_desencriptado, mensaje_original)

    def test_funciona_bien_3(self):
        clave = [[4, 1], [2, 2]]
        mensaje_original = "Python"
        encriptador = Encriptador(clave)
        mensaje_encriptado = encriptador.encriptar(mensaje_original)
        mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
        self.assertEqual(mensaje_desencriptado, mensaje_original)

    def test_limite_1(self):
        clave = [[1, 0], [0, 0]]
        mensaje_original = "A"
        with self.assertRaises(ValueError):
            encriptador = Encriptador(clave)

    def test_limite_2(self):
        clave = [[0, 0], [0, 1]]
        mensaje_original = "B" * 1000
        with self.assertRaises(ValueError):
            encriptador = Encriptador(clave)

    def test_limite_3(self):
        clave = [[114534455, -1454545], [4545451, 15454545]]
        mensaje_original = ""
        encriptador = Encriptador(clave)
        mensaje_encriptado = encriptador.encriptar(mensaje_original)
        mensaje_desencriptado = encriptador.desencriptar(mensaje_encriptado)
        self.assertEqual(mensaje_desencriptado, mensaje_original)

    def test_falla_1(self):
        clave = [[1, 1], [1, 1]]
        mensaje_original = "Hola"
        with self.assertRaises(ValueError):
            encriptador = Encriptador(clave)

    def test_falla_2(self):
        clave = [[2, 3], [1, 4]]
        encriptador = Encriptador(clave)
        mensaje_encriptado = np.array([1, 2, 3])  # Longitud incorrecta
        with self.assertRaises(ValueError):
            encriptador.desencriptar(mensaje_encriptado)



    def test_falla_3(self):
        clave = [[1, 2, 3], [4, 5, 6]]  # No es una matriz cuadrada
        with self.assertRaises(ValueError):
            encriptador = Encriptador(clave)


    def test_falla_4(self):
        clave = [[1, 2], [3, 4, 5]]
        mensaje_original = "Código"
        with self.assertRaises(ValueError):
            encriptador = Encriptador(clave)

if __name__ == '__main__':
    unittest.main()

