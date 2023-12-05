# Quantum Message Encryption

Este repositorio contiene un programa de encriptación de mensajes que utiliza conceptos de la criptografía cuántica para generar una clave segura. El programa permite a los usuarios encriptar un mensaje y guardarlo en un archivo, y luego desencriptar el mensaje desde el archivo.

## ¿Qué es la criptografía cuántica?

La criptografía cuántica es un enfoque de la criptografía que utiliza los principios de la mecánica cuántica. En particular, se basa en el hecho de que medir un sistema cuántico puede cambiar el estado de ese sistema. Esto significa que cualquier intento de interceptar la comunicación será detectado por los participantes legítimos.

## ¿Cómo funciona este programa?

Este programa simula un protocolo de distribución de claves cuánticas. Primero, el usuario introduce un mensaje que desea encriptar. Luego, el programa genera una clave cuántica y la utiliza para encriptar el mensaje utilizando el algoritmo de encriptación AES. El mensaje encriptado y la clave se guardan en un archivo.

Cuando el usuario desea desencriptar el mensaje, el programa lee el mensaje encriptado y la clave del archivo, luego utiliza la clave para desencriptar el mensaje.

## Requisitos

Este programa requiere Python 3 y la biblioteca `pycryptodome`. Puedes instalar `pycryptodome` con el siguiente comando:

```bash
pip install pycryptodome
```

## Uso

Para ejecutar el programa, navega hasta el directorio que contiene el archivo `message-encryption.py` y ejecuta el siguiente comando:

```bash
python message-encryption.py
```

El programa te pedirá que elijas entre encriptar un mensaje o desencriptar un mensaje. Si eliges encriptar un mensaje, el programa te pedirá que introduzcas el mensaje, luego lo encriptará y guardará el mensaje encriptado y la clave en un archivo llamado `encrypted_message.txt`.

Si eliges desencriptar un mensaje, el programa leerá el mensaje encriptado y la clave desde el archivo `encrypted_message.txt`, luego desencriptará el mensaje y lo imprimirá en la consola.

## Advertencia

Este programa es solo un ejemplo y no debe utilizarse para encriptar información sensible en un entorno real. La criptografía cuántica es un campo de investigación activo y este programa no implementa un protocolo de criptografía cuántica seguro. Además, este programa guarda la clave de encriptación en el mismo archivo que el mensaje encriptado, lo cual no es seguro en un entorno real.# Message-Encryption