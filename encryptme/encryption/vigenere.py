import re

max_num = 26
ordinal_A = 65

# Vigenere cipher implementation
def vigenere_cipher(s, key):
    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    diff_symbols = re.sub(r'[^\W]', ' ', s)
    diff_symbols_int = [ord(i) for i in diff_symbols]

    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]  # ordinal numbers for the letters in key
    plaintext_int = [ord(i) for i in s.upper()]  # ordinal numbers for the letters in string
    ciphertext = ''

    for i in range(len(plaintext_int)):
        value = (plaintext_int[i] + key_as_int[i % key_length]) % max_num
        if plaintext_int[i] != diff_symbols_int[i]:
            ciphertext += chr(value + ordinal_A)
        else:
            ciphertext += chr(diff_symbols_int[i])
    return ciphertext

def vigenere_cipher_decoder(s, key):
    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    diff_symbols = re.sub(r'[^\W]', ' ', s)
    diff_symbols_int = [ord(i) for i in diff_symbols]

    key_length = len(key)
    key_as_int = [ord(i) for i in key.upper()]
    ciphertext_int = [ord(i) for i in s.upper()]
    plaintext = ''
    for i in range(len(ciphertext_int)):
        value = (ciphertext_int[i] - key_as_int[i % key_length]) % max_num
        if ciphertext_int[i] != diff_symbols_int[i]:
            plaintext += chr(value + ordinal_A)
        else:
            plaintext += chr(diff_symbols_int[i])
    return plaintext