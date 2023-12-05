import numpy as np
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from pathlib import Path
from Crypto.Util.Padding import unpad

def generate_key(length):
    return np.random.randint(2, size=length)

def measure_in_basis(state, basis):
    if basis == 0: # Z basis
        return state
    else: # X basis
        return 1 - state

def encrypt_message(message, key):
    # Crear un objeto AES
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Encriptar el mensaje
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    
    return cipher.iv, ciphertext

def save_encrypted_message(iv, ciphertext, key, file_path):
    with open(file_path, "wb") as file:
        file.write(key)
        file.write(iv)
        file.write(ciphertext)
    print(f"El mensaje se ha encriptado con éxito y se ha guardado en '{file_path}'.")

def print_animation(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  # Nueva línea al final

def main():
    print("Bienvenido al encriptador cuántico de mensajes.")
    print("""

 █████╗ ███╗   ███╗██████╗ 
██╔══██╗████╗ ████║██╔══██╗
███████║██╔████╔██║██████╔╝
██╔══██║██║╚██╔╝██║██╔══██╗
██║  ██║██║ ╚═╝ ██║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
                           
""")
    
    while True:
        print("Seleccione una opción:")
        print("1. Encriptar un mensaje")
        print("2. Desencriptar un mensaje")
        
        choice = input("Ingrese el número de opción: ")
        
        if choice == "1":
            message = input("Ingrese el mensaje que desea encriptar: ")
            
            # Longitud de la clave
            key_length = len(message) * 8
            
            # Alice genera una clave y una base
            alice_key = generate_key(key_length)
            alice_bases = generate_key(key_length)
            
            # Bob genera una base
            bob_bases = generate_key(key_length)
            
            # Alice mide sus qubits en su base
            alice_measurements = [measure_in_basis(alice_key[i], alice_bases[i]) for i in range(key_length)]
            
            # Bob mide los qubits en su base
            bob_measurements = [measure_in_basis(alice_key[i], bob_bases[i]) for i in range(key_length)]
            
            # Ambos descartan las mediciones donde sus bases no coinciden
            final_key = [alice_measurements[i] for i in range(key_length) if alice_bases[i] == bob_bases[i]]
            
            # Asegurarse de que la longitud de la clave es válida para AES
            if len(final_key) > 32:
                final_key = final_key[:32]
            elif len(final_key) < 24:
                final_key = final_key + [0] * (24 - len(final_key))

            # Convertir la clave a bytes
            key = bytes(final_key)
            
            # Encriptar el mensaje
            iv, ciphertext = encrypt_message(message, key)
            
            # Ruta al directorio actual
            current_directory = Path.cwd()

            # Ruta al archivo en el directorio actual
            file_path = current_directory / "encrypted_message.txt"

            # Guardar el mensaje encriptado y la clave en un archivo
            save_encrypted_message(iv, ciphertext, key, file_path)
            break
        elif choice == "2":
            # Ruta al directorio actual
            current_directory = Path.cwd()

            # Ruta al archivo en el directorio actual
            file_path = current_directory / "encrypted_message.txt"

            # Leer el mensaje encriptado y la clave desde el archivo
            with open(file_path, "rb") as file:
                key = file.read(32)  # La clave tiene una longitud de 32 bytes
                iv = file.read(16)  # El IV tiene una longitud de 16 bytes
                ciphertext = file.read()  # El resto del archivo es el mensaje encriptado

            # Crear un objeto de cifrado AES con la clave y el IV
            cipher_dec = AES.new(key, AES.MODE_CBC, iv=iv)

            # Desencriptar el mensaje y eliminar el relleno
            plaintext = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

            print("El mensaje desencriptado es:", plaintext.decode())
            break
    else:
        print("Opción inválida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()