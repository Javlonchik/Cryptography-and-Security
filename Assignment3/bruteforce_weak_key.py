'''
Write a python code that breaks the following using brute force attack:
Assume you got a ciphertext (in hexa) that  is  b'1525053514291239',  as a result of XOR encryption.
Additionally, assume that the unknown plaintext is an 8-letter word and among the most common words in English
You know that a very weak key is used that consists of a repeated character followed by @ sign. For example, if the word is an 8 letter word, then the key will be: ?@?@?@?@
Your task is to brute force this ciphertext based on the above information.
Output any successful decrypted plaintext, if you have found it among the most common words in English.
'''

#SOLUTION:

# Open the file and read the words into a set
def read_words(filename):
    with open(filename, 'r') as file:
        return set(file.read().split())

# Define the XOR function
def xor_strings(string1, string2):
    return "".join([chr(ord(c1) ^ ord(c2)) for (c1,c2) in zip(string1, string2)])

# Define the cipher text and key generation functions
CIPHER_HEX = '1525053514291239'

def generate_key(char):
    return (chr(char) + '@') * 4

# Convert the hex cipher text to plaintext
ciphertext = bytes.fromhex(CIPHER_HEX).decode('utf-8')

# Try all possible keys and check if the decrypted plaintext is a common word
def crack_cipher(words):
    for i in range(128):
        key = generate_key(i)
        plaintext = xor_strings(key, ciphertext)
        if plaintext.isalpha() and plaintext.lower() in words:
            return plaintext.lower()
    return 'Not found'

# Call the functions
words = read_words('common_words.txt')
plaintext = crack_cipher(words)
print("Decrypted plaintext: " + plaintext)
