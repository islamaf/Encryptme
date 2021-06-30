from string import ascii_lowercase, ascii_uppercase
import re
max_num = 26

# Vernam cipher implementation
def vernam_cipher(s, key):
    s_number = []  # List of numbers corresponding to letter for string
    key_number = []  # List of numbers corresponding to letter for key
    ciphered_string = ''

    # Getting the letter:number(index) dictionary
    # Depends also on the cases of the input, either uppercase or lowercase
    LETTERS = {}
    if s == s.lower():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
    if s == s.upper():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=0)}

    remove_symbols = re.sub(r'[^a-zA-Z]', '', s)
    s = remove_symbols

    key_remove_symbols = re.sub(r'[^a-zA-Z]', '', key)
    key = key_remove_symbols

    # Key
    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    for hieroglyph in s:
        if hieroglyph in LETTERS:
            s_number.append(LETTERS[hieroglyph])

    for hieroglyph in key:
        if hieroglyph in LETTERS:
            key_number.append(LETTERS[hieroglyph])

    for i in range(len(s_number)):
        total = int(s_number[i]) + int(key_number[i])  # Add corresponding list position numbers one by one
        if total >= max_num:
            total = total - max_num  # If total > 26, minus 26 from total
            for k, v in LETTERS.items():  # Search for number in dictionary and get corresponding letter
                total = str(total)
                if total in v:
                    total = k
                    ciphered_string = ciphered_string + total
        else:
            total = str(total)
            for k, v in LETTERS.items():
                if total in v:
                    total = k
                    total = str(total)
                    ciphered_string = ciphered_string + total
    return ciphered_string.upper()

def vernam_cipher_decoder(s, key):
    s_number = []  # List of numbers corresponding to letter for string
    key_number = []  # List of numbers corresponding to letter for key
    plaintext = ''

    remove_symbols = re.sub(r'[^a-zA-Z]', '', s)
    s = remove_symbols

    key_remove_symbols = re.sub(r'[^a-zA-Z]', '', key)
    key = key_remove_symbols

    # Key
    if len(key) < len(s):
        for i in range(len(s)):
            key += key[i]  # Generate key from itself if len(key) < len(s)
    if len(key) > len(s):
        key = key[0:len(s)]  # Slice key to the size of string if it is bigger

    # Getting the letter:number(index) dictionary
    # Depends also on the cases of the input, either uppercase or lowercase
    LETTERS = {}
    if s == s.lower():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=0)}
        key = key.lower()
    if s == s.upper():
        LETTERS = {letter: str(index) for index, letter in enumerate(ascii_uppercase, start=0)}
        key = key.upper()

    for hieroglyph in s:
        if hieroglyph in LETTERS:
            s_number.append(LETTERS[hieroglyph])

    for hieroglyph in key:
        if hieroglyph in LETTERS:
            key_number.append(LETTERS[hieroglyph])

    for i in range(len(s_number)):
        total = int(s_number[i]) - int(key_number[i])  # Add corresponding list position numbers one by one
        if total >= max_num:
            total = total - max_num  # If total > 26, minus 26 from total
            for k, v in LETTERS.items():  # Search for number in dictionary and get corresponding letter
                total = str(total)
                if total in v:
                    total = k
                    plaintext = plaintext + total
        elif total < 0:
            total = 26 - ((-1)*total)
            total = str(total)
            for k, v in LETTERS.items():
                if total in v:
                    total = k
                    total = str(total)
                    plaintext = plaintext + total
        else:
            total = str(total)
            for k, v in LETTERS.items():
                if total in v:
                    total = k
                    total = str(total)
                    plaintext = plaintext + total
    return plaintext.upper()