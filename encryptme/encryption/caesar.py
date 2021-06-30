max_num = 26

def caesar_cipher(s, key):
    # key = int(input())  # Get the cipher shift key
    # if key < 1 or key > max_num:  # Key should be in range of the alphabets
    #     exit(0)  # Exit program if out of range

    ciphered_string = ''  # String to store encrypted result

    for hieroglyph in s:
        # Only letters will be encrypted. Numbers and other symbols stay in the original form
        if hieroglyph.isalpha():  # Check if letter is alphabet
            hold_shift = ord(hieroglyph)  # Get ordinal value of letter
            hold_shift += key  # Shift value by the key

            # Check if letter is uppercase and get ordinal value
            if hieroglyph.isupper():
                if hold_shift < ord('A'):
                    hold_shift += max_num
                elif hold_shift > ord('Z'):
                    hold_shift -= max_num
            # Check if letter is lower case and get ordinal value
            elif hieroglyph.islower():
                if hold_shift < ord('a'):
                    hold_shift += max_num
                elif hold_shift > ord('z'):
                    hold_shift -= max_num
            ciphered_string += chr(hold_shift)  # Put character in encrypted string
        else:
            ciphered_string += hieroglyph  # If position value is not alphabet, return original value
    return ciphered_string  # Return encrypted string