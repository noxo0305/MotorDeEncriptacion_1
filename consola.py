from funcionalidad import *

def receive_matrix():
    """
    Receives a 2x2 matrix from the user.
    """
    key = []
    for _ in range(2):
        row = []
        for _ in range(2):
            value = int(input("Ingrese un valor de la clave (total de 4 valores): "))
            row.append(value)
        key.append(row)
    print("The entered key is:", key)
    return key

def main():
    key = receive_matrix()
    while not matrix_size(key):
        key = receive_matrix()
    encryptor = Encryptor(key)
    option = int(input("Ingrese 1 si desea encriptar y 2 si desea desencriptar: "))
    while option not in [1, 2]:
        print("Enter a valid option.")
        option = int(input("Ingrese 1 si desea encriptar y 2 si desea desencriptar: "))

    if option == 1:
        message = input("Ingrese el mensaje a encriptar: ")
        encrypted_message = encryptor.encrypt(message)
        print("Encrypted message:", encrypted_message)
    elif option == 2:
        encrypted_message = np.array(eval(input("Ingrese el mensaje encriptado (como lista de listas): ")))
        decrypted_message = encryptor.decrypt(encrypted_message)
        print("Decrypted message:", decrypted_message)

main()
