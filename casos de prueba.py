import unittest
import numpy as np
from funcionalidad import Encryptor

class TestEncryptor(unittest.TestCase):
    
    def test_works_well_1(self):
        key = [[2, 3], [1, 4]]
        original_message = "Hola"
        encryptor = Encryptor(key)
        encrypted_message = encryptor.encrypt(original_message)
        decrypted_message = encryptor.decrypt(encrypted_message)
        self.assertEqual(decrypted_message, original_message)

    def test_works_well_2(self):
        key = [[1, 0], [0, 1]]
        original_message = "Mundo"
        encryptor = Encryptor(key)
        encrypted_message = encryptor.encrypt(original_message)
        decrypted_message = encryptor.decrypt(encrypted_message)
        self.assertEqual(decrypted_message, original_message)

    def test_works_well_3(self):
        key = [[4, 1], [2, 2]]
        original_message = "Python"
        encryptor = Encryptor(key)
        encrypted_message = encryptor.encrypt(original_message)
        decrypted_message = encryptor.decrypt(encrypted_message)
        self.assertEqual(decrypted_message, original_message)

    def test_limit_1(self):
        key = [[1, 0], [0, 0]]
        original_message = "A"
        with self.assertRaises(ValueError):
            encryptor = Encryptor(key)

    def test_limit_2(self):
        key = [[0, 0], [0, 1]]
        original_message = "B" * 1000
        with self.assertRaises(ValueError):
            encryptor = Encryptor(key)

    def test_limit_3(self):
        key = [[114534455, -1454545], [4545451, 15454545]]
        original_message = ""
        encryptor = Encryptor(key)
        encrypted_message = encryptor.encrypt(original_message)
        decrypted_message = encryptor.decrypt(encrypted_message)
        self.assertEqual(decrypted_message, original_message)

    def test_fail_1(self):
        key = [[1, 1], [1, 1]]
        original_message = "Hola"
        with self.assertRaises(ValueError):
            encryptor = Encryptor(key)

    def test_fail_2(self):
        key = [[2, 3], [1, 4]]
        encryptor = Encryptor(key)
        encrypted_message = np.array([1, 2, 3])  # Incorrect length
        with self.assertRaises(ValueError):
            encryptor.decrypt(encrypted_message)

    def test_fail_3(self):
        key = [[1, 2, 3], [4, 5, 6]]  # Not a square matrix
        with self.assertRaises(ValueError):
            encryptor = Encryptor(key)

    def test_fail_4(self):
        key = [[1, 2], [3, 4, 5]]
        original_message = "Código"
        with self.assertRaises(ValueError):
            encryptor = Encryptor(key)

if __name__ == '__main__':
    unittest.main()
