import numpy as np
import time
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
from pathlib import Path
from Crypto.Util.Padding import unpad

def generate_key(length):
    """
    Generate a random key of the specified length.

    Parameters:
    length (int): The length of the key in bits.

    Returns:
    numpy.ndarray: The generated key as a numpy array of 0s and 1s.
    """
    return np.random.randint(2, size=length)

def measure_in_basis(state, basis):
    """
    Measure the state in the specified basis.

    Parameters:
    state (int): The state to be measured (0 or 1).
    basis (int): The basis in which to measure the state (0 for Z basis, 1 for X basis).

    Returns:
    int: The measurement result.
    """
    if basis == 0: # Z basis
        return state
    else: # X basis
        return 1 - state

def encrypt_message(message, key):
    """
    Encrypt the message using AES encryption.

    Parameters:
    message (str): The message to be encrypted.
    key (bytes): The encryption key.

    Returns:
    tuple: A tuple containing the initialization vector (IV) and the ciphertext.
    """
    # Create an AES cipher object
    cipher = AES.new(key, AES.MODE_CBC)
    
    # Encrypt the message
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    
    return cipher.iv, ciphertext

def save_encrypted_message(iv, ciphertext, key, file_path):
    """
    Save the encrypted message, IV, and key to a file.

    Parameters:
    iv (bytes): The initialization vector (IV).
    ciphertext (bytes): The encrypted message.
    key (bytes): The encryption key.
    file_path (str): The path to the file where the encrypted message will be saved.
    """
    with open(file_path, "wb") as file:
        file.write(key)
        file.write(iv)
        file.write(ciphertext)
    print(f"The message has been successfully encrypted and saved to '{file_path}'.")

def print_animation(message):
    """
    Print a message with an animated effect.

    Parameters:
    message (str): The message to be printed.
    """
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.1)
    print()  # New line at the end

def main():
    """
    Main function for the message encryption program.
    """
    print("Welcome to the quantum message encryptor.")
    print("""

 █████╗ ███╗   ███╗██████╗ 
██╔══██╗████╗ ████║██╔══██╗
███████║██╔████╔██║██████╔╝
██╔══██║██║╚██╔╝██║██╔══██╗
██║  ██║██║ ╚═╝ ██║██║  ██║
╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝
                           
""")
    
    while True:
        print("Select an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        
        choice = input("Enter the option number: ")
        
        if choice == "1":
            message = input("Enter the message to encrypt: ")
            
            # Key length
            key_length = len(message) * 8
            
            # Alice generates a key and a basis
            alice_key = generate_key(key_length)
            alice_bases = generate_key(key_length)
            
            # Bob generates a basis
            bob_bases = generate_key(key_length)
            
            # Alice measures her qubits in her basis
            alice_measurements = [measure_in_basis(alice_key[i], alice_bases[i]) for i in range(key_length)]
            
            # Bob measures the qubits in his basis
            bob_measurements = [measure_in_basis(alice_key[i], bob_bases[i]) for i in range(key_length)]
            
            # Both discard the measurements where their bases do not match
            final_key = [alice_measurements[i] for i in range(key_length) if alice_bases[i] == bob_bases[i]]
            
            # Make sure the key length is valid for AES
            if len(final_key) > 32:
                final_key = final_key[:32]
            elif len(final_key) < 24:
                final_key = final_key + [0] * (24 - len(final_key))

            # Convert the key to bytes
            key = bytes(final_key)
            
            # Encrypt the message
            iv, ciphertext = encrypt_message(message, key)
            
            # Current directory path
            current_directory = Path.cwd()

            # File path in the current directory
            file_path = current_directory / "encrypted_message.txt"

            # Save the encrypted message and key to a file
            save_encrypted_message(iv, ciphertext, key, file_path)
            break
        elif choice == "2":
            # Current directory path
            current_directory = Path.cwd()

            # File path in the current directory
            file_path = current_directory / "encrypted_message.txt"

            # Read the encrypted message and key from the file
            with open(file_path, "rb") as file:
                key = file.read(32)  # The key has a length of 32 bytes
                iv = file.read(16)  # The IV has a length of 16 bytes
                ciphertext = file.read()  # The rest of the file is the encrypted message

            # Create an AES cipher object with the key and IV
            cipher_dec = AES.new(key, AES.MODE_CBC, iv=iv)

            # Decrypt the message and remove the padding
            plaintext = unpad(cipher_dec.decrypt(ciphertext), AES.block_size)

            print("The decrypted message is:", plaintext.decode())
            break
    else:
        print("Invalid option. Please select a valid option.")

if __name__ == "__main__":
    main()