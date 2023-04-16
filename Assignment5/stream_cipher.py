# Write a python code that implement the following scenario:
# 1) Read a stream of data from (data_stream.txt) file, one character at a time.
# 2) Generate the required number of bits using LFSR (generates 8-bit at a time for each character)
# 3) Perform the xor encryption.
# 4) In a separate function perform the xor decryption. Note: during decryption the sequence of key can be generated using the seed and mask value
# 5) OPTIONAL: this is an optional step. Try to crack the LFSR, by knowing the original data stream and the ciphertext.

# code here: 
import sys

class LFSR:
    def __init__(self, seed, mask):
        self.state = seed
        self.mask = mask

    def get_bit(self):
        next_bit = (self.state & 1) ^ ((self.state & self.mask) > 0)
        self.state >>= 1
        self.state |= (next_bit << 7)
        return next_bit

    def generate_key(self, length):
        key = 0
        for _ in range(length):
            key = (key << 1) | self.get_bit()
        return key


def xor_encrypt(data, lfsr):
    encrypted_data = []
    for char in data:
        key = lfsr.generate_key(8)
        encrypted_char = chr(ord(char) ^ key)
        encrypted_data.append(encrypted_char)
    return ''.join(encrypted_data)


def xor_decrypt(encrypted_data, seed, mask):
    lfsr = LFSR(seed, mask)
    decrypted_data = []
    for char in encrypted_data:
        key = lfsr.generate_key(8)
        decrypted_char = chr(ord(char) ^ key)
        decrypted_data.append(decrypted_char)
    return ''.join(decrypted_data)


def read_data_stream(file_path):
    with open(file_path, 'r') as file:
        while True:
            char = file.read(1)
            if not char:
                break
            yield char


def main():
    file_path = 'data_stream.txt'
    seed = 0b01100110
    mask = 0b10101010
    lfsr = LFSR(seed, mask)

    data = ''.join(list(read_data_stream(file_path)))
    encrypted_data = xor_encrypt(data, lfsr)
    decrypted_data = xor_decrypt(encrypted_data, seed, mask)

    print('Original data:', data)
    print('Encrypted data:', encrypted_data)
    print('Decrypted data:', decrypted_data)


if __name__ == '__main__':
    main()
