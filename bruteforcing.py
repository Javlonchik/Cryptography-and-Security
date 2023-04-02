#TASK DESCRIPTION:

#Write python code that does a brute force attack against Caesar encryption.
#Brute force attack means trying all possible keys for a given cipher.
#In other words, if there are 10 possible keys, then the result of brute force attack will be 10 possible plain texts, 9 of which are invalid texts. You need to do the following:


#SOLUTION:

alphabet = 'abcdefghijklmnopqrstuvwxyz, '
def indexOfLetter(letter):
    for i in range(len(alphabet)):
        if letter == alphabet[i]:
            return i

def shiftChar_right(letter, shift):
    index = indexOfLetter(letter)
    new_index = (index + shift) % 26
    return alphabet[new_index]

encrypted = input("Write an encrypted string: ")
for i in range(0, 26):
    decrypted = ""
    for char in encrypted:
        if char == ',' or char == ' ':
            decrypted += char
        else:
            decrypted += shiftChar_right(char, i)
    print(decrypted)
