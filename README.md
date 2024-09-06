# Motor de Encriptación

Este proyecto es una aplicación que permite encriptar y desencriptar mensajes utilizando algoritmos criptográficos simétricos con llave. Se desarrolló con el propósito de facilitar el uso de diferentes métodos de cifrado que son comúnmente utilizados en la industria.

## Autores

- José Manuel Díaz
- Juan Nicolás Ruiz

## Descripción del Proyecto

La aplicación acepta un mensaje y una llave como entradas, y devuelve un mensaje cifrado utilizando uno de los siguientes algoritmos de cifrado simétrico:

- Twofish
- Serpent
- AES (Rijndael)
- Camellia
- Salsa20
- ChaCha20
- Blowfish
- CAST5
- Kuznyechik
- RC4
- DES
- 3DES
- Skipjack
- Safer
- IDEA

El proyecto está diseñado para permitir tanto la **encriptación** como la **desencriptación** de mensajes de manera eficiente y segura.

### Funcionalidades

- **Encriptar:** Acepta un mensaje y una llave, luego utiliza el algoritmo seleccionado para producir un mensaje cifrado.
- **Desencriptar:** Acepta un mensaje cifrado y la llave, y devuelve el mensaje original.

## Requisitos Previos

Para ejecutar este proyecto, necesitas tener instalados los siguientes programas:
- Numpy
- Python 3.x
- Paquetes criptográficos (pueden instalarse con `pip`)

## Instalación

1. Clona el repositorio a tu máquina local:
   ```bash
   git clone https://github.com/usuario/proyecto.git
