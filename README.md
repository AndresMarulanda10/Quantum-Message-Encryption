# Quantum Message Encryption

This repository contains a message encryption program that uses concepts from quantum cryptography to generate a secure key. The program allows users to encrypt a message and save it to a file, and then decrypt the message from the file.

## What is quantum cryptography?

Quantum cryptography is an approach to cryptography that uses the principles of quantum mechanics. In particular, it is based on the fact that measuring a quantum system can change the state of that system. This means that any attempt to intercept the communication will be detected by legitimate participants.

## How does this program work?

This program simulates a quantum key distribution protocol. First, the user enters a message to be encrypted. Then, the program generates a quantum key and uses it to encrypt the message using the AES encryption algorithm. The encrypted message and the key are stored in a file.

When the user wants to decrypt the message, the program reads the encrypted message and the key from the file, then uses the key to decrypt the message.

## Requirements

This program requires Python 3 and the `pycryptodome` library. You can install `pycryptodome` with the following command:

```bash
pip install pycryptodome
```

## Use

To run the program, navigate to the directory containing the `message-encryption.py` file and execute the following command:

```bash
python message-encryption.py
```

The program will ask you to choose between encrypting a message or decrypting a message. If you choose to encrypt a message, the program will ask you to enter the message, then encrypt it and save the encrypted message and the key in a file called `encrypted_message.txt`.

If you choose to decrypt a message, the program will read the encrypted message and key from the `encrypted_message.txt` file, then decrypt the message and print it to the console.

## Warning

This program is only an example and should not be used to encrypt sensitive information in a real environment. Quantum cryptography is an active field of research and this program does not implement a secure quantum cryptography protocol. In addition, this program stores the encryption key in the same file as the encrypted message, which is not secure in a real environment.# Message-Encryption