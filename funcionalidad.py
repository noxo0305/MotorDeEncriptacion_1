import numpy as np

class CustomException(Exception):
    def __init__(self, message="The matrix is singular (non-invertible)."):
        self.message = message
        super().__init__(self.message)

class Encryptor:
    def __init__(self, key):
        """
        Initializes the encryptor with a key and calculates its inverse.
        Raises ValueError if the key has no inverse.
        """
        self.key = np.array(key)
        if np.linalg.det(self.key) == 0:
            raise ValueError("The matrix has no inverse and cannot be used as a key")
        self.inverse_key = np.linalg.inv(self.key)

    def encrypt(self, message):
        """
        Encrypts a message using the key.
        """
        message_vector = self._convert_to_vector(message)
        encrypted_message = np.dot(self.key, message_vector)
        return encrypted_message

    def decrypt(self, encrypted_message):
        """
        Decrypts an encrypted message using the inverse of the key.
        Raises ValueError if the encrypted message is not valid.
        """
        if encrypted_message.shape[0] != self.key.shape[0]:
            raise ValueError("The encrypted message is not valid for the provided key")
        message_vector = np.dot(self.inverse_key, encrypted_message)
        decrypted_message = self._convert_to_text(message_vector)
        return decrypted_message

    def _convert_to_vector(self, message):
        """
        Converts a text message to a numeric vector.
        """
        message_vector = [ord(char) for char in message]
        while len(message_vector) % self.key.shape[0] != 0:
            message_vector.append(0)
        return np.array(message_vector).reshape(-1, self.key.shape[0]).T

    def _convert_to_text(self, message_vector):
        """
        Converts a numeric vector to a text message.
        """
        message_vector = message_vector.T.flatten()
        message = ''.join(chr(int(round(num))) for num in message_vector if num != 0)
        return message

def matrix_size(matrix):
    """
    Checks if the matrix is of size 2x2.
    """
    if len(matrix) == 2 and all(len(row) == 2 for row in matrix):
        return True
    else:
        raise ValueError("The matrix must be of size 2x2")

def matrix_non_singular(matrix):
    """
    Checks if the matrix is non-singular (i.e., has an inverse).
    Raises a ValueError if the matrix is singular.
    """
    try:
        if np.linalg.det(matrix) != 0:
            return True
        else:
            raise ValueError("The matrix has no inverse and cannot be used as a key")
    except np.linalg.LinAlgError as e:
        raise ValueError(f"Error calculating the determinant: {e}")

