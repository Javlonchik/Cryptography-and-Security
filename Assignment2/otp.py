'''
TASK DESCRIPTION
Write a python code that combine the one time pad (OTP) with Caesar encryption.
one time pad (OTP) in Caesar means that each key is used once with one letter, compared to the original Caesar that a single key is used for the whole message
'''

# SOLUTION
#This code is a program that encrypts a message using a one-time pad.
#The program generates a random key for each letter in the message.
#The key is then used to encrypt the message.
#The encrypted message and the key are then printed.
#The key is then used to decrypt the message. The decrypted message is then printed.

import random

alphabet = "abcdefghijklmnopqrstuvwxyz, "

def letterWithIndex(i):
    return alphabet[i]

def indexWithLetter(letter):
    return alphabet.find(letter)

def shiftChar(char, shift):
    i = indexWithLetter(char)
    new = (i + shift) % 28
    return letterWithIndex(new)

def generateKeys(message):
    random_list = []

    for i in range(len(message)):
        random_list.append(random.randint(0, 27))

    return random_list

def encrypt(message):
    keys = generateKeys(message)
    encrypted = ""
    for i in range(len(message)):
        char = message[i]
        shift = keys[i]
        encrypted += shiftChar(char, shift)
    return encrypted, keys

def decrypt(ciphertext, keys):
    decrypted = ""
    for i in range(len(ciphertext)):
        char = ciphertext[i]
        shift = keys[i]
        decrypted += shiftChar(char, -shift)
    return decrypted


def main():
    plaintext = input("Enter a message to encrypt: ")
    ciphertext, keys = encrypt(plaintext)
    print("Encrypted message:", ciphertext)
    print("Decrypted message:", decrypt(ciphertext, keys))


main()
