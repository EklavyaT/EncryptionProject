import numpy as np



def caesar_encrypt_python(word, shift):
    encrypted_word = ""
    for i in word:
        if i.isalpha():
            character = chr(((ord(i) + shift - 97) % 26) + 97)
            encrypted_word += character
        else:
            encrypted_word += i
    return encrypted_word

def caesar_decrypt_python(encrypted_word, shift):
    decrypted_word = ""
    for i in encrypted_word:
        if i.isalpha():
            character = chr(((ord(i) - shift - 97) % 26) + 97)
            decrypted_word += character
        else:
            decrypted_word += i
    return decrypted_word

def caesar_decrypt(ciphertext):
    
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    
    ciphertext = ciphertext.lower()

    
    decrypted_message = ''

    
    for shift in range(len(alphabet)):
        
        decrypted_text = ''

       
        for char in ciphertext:
            if char in alphabet:
                
                char_index = alphabet.index(char)

                
                decrypted_index = (char_index - shift) % len(alphabet)

                
                decrypted_text += alphabet[decrypted_index]
            else:
                
                decrypted_text += char

      
        if 'the' in decrypted_text or 'and' in decrypted_text:
            
            decrypted_message = decrypted_text
            break

 
    return decrypted_message




def atbash_encrypt_python(sentence):
    encrypted_sentence = ""
    for i in sentence:
        ascii_val = ord(i)
        if 65 <= ascii_val <= 90:
            current_index = ascii_val - 65
            new_index = 25 - current_index
            new_ascii = new_index + 65
            encrypted_letter = chr(new_ascii)
        elif 97 <= ascii_val <= 122:
            current_index = ascii_val - 97
            new_index = 25 - current_index
            new_ascii = new_index + 97
            encrypted_letter = chr(new_ascii)
        else:
            encrypted_letter = i
        encrypted_sentence += encrypted_letter
    return encrypted_sentence

def atbash_decrypt_python(encrypted_sentence):
    return atbash_encrypt_python(encrypted_sentence)




def vigenere_encrypt_python(message, keyword):
    encrypted_message = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    message_length = len(message)

    for i in range(message_length):
        if message[i].isalpha():
            char = message[i].lower()
            keyword_char = keyword[i % keyword_length]
            keyword_code = ord(keyword_char) - 97
            shift = ord(char) + keyword_code + 1
            encrypted_char = chr((shift - 97) % 26 + 97)
            encrypted_message += encrypted_char.upper() if message[i].isupper() else encrypted_char
        else:
            encrypted_message += message[i]

    return encrypted_message

def vigenere_decrypt_python(encrypted_message, keyword):
    decrypted_message = ""
    keyword = keyword.lower()
    keyword_length = len(keyword)
    message_length = len(encrypted_message)

    for i in range(message_length):
        if encrypted_message[i].isalpha():
            char = encrypted_message[i].lower()
            keyword_char = keyword[i % keyword_length]
            keyword_code = ord(keyword_char) - 97
            shift = ord(char) - keyword_code - 1
            decrypted_char = chr((shift - 97) % 26 + 97)
            decrypted_message += decrypted_char.upper() if encrypted_message[i].isupper() else decrypted_char
        else:
            decrypted_message += encrypted_message[i]

    return decrypted_message





def playfair_encrypt_python(message, keyword):
    def generate_playfair_table(keyword):
        keyword = keyword.replace('j', 'i')  # Replace 'j' with 'i'
        keyword += 'abcdefghiklmnopqrstuvwxyz'  # Add the remaining letters
        table = [['' for _ in range(5)] for _ in range(5)]
        used_letters = set()

        row = 0
        col = 0
        for letter in keyword:
            if letter not in used_letters:
                table[row][col] = letter
                used_letters.add(letter)
                col += 1
                if col == 5:
                    col = 0
                    row += 1
                    if row == 5:
                        break

        return table

    def find_position(table, letter):
        for row in range(5):
            for col in range(5):
                if table[row][col] == letter:
                    return row, col

    def encrypt_pair(table, pair):
        a_row, a_col = find_position(table, pair[0])
        b_row, b_col = find_position(table, pair[1])

        if a_row == b_row:
            return table[a_row][(a_col + 1) % 5] + table[b_row][(b_col + 1) % 5]
        elif a_col == b_col:
            return table[(a_row + 1) % 5][a_col] + table[(b_row + 1) % 5][b_col]
        else:
            return table[a_row][b_col] + table[b_row][a_col]

    message = message.lower().replace('j', 'i')  # Replace 'j' with 'i'
    message_length = len(message)
    encrypted_message = ""
    table = generate_playfair_table(keyword)

    i = 0
    while i < message_length:
        pair = message[i:i+2]
        if len(pair) < 2 or pair[0] == pair[1]:
            pair = pair[0] + 'x'
            i -= 1  # Process the same pair in the next iteration

        encrypted_pair = encrypt_pair(table, pair)
        encrypted_message += encrypted_pair

        i += 2

    return encrypted_message.upper()

def playfair_decrypt_python(encrypted_message, keyword):
    def generate_playfair_table(keyword):
        keyword = keyword.replace('j', 'i')  # Replace 'j' with 'i'
        keyword += 'abcdefghiklmnopqrstuvwxyz'  # Add the remaining letters
        table = [['' for _ in range(5)] for _ in range(5)]
        used_letters = set()

        row = 0
        col = 0
        for letter in keyword:
            if letter not in used_letters:
                table[row][col] = letter
                used_letters.add(letter)
                col += 1
                if col == 5:
                    col = 0
                    row += 1
                    if row == 5:
                        break

        return table

    def find_position(table, letter):
        for row in range(5):
            for col in range(5):
                if table[row][col] == letter:
                    return row, col

    def decrypt_pair(table, pair):
        a_row, a_col = find_position(table, pair[0])
        b_row, b_col = find_position(table, pair[1])

        if a_row == b_row:
            return table[a_row][(a_col - 1) % 5] + table[b_row][(b_col - 1) % 5]
        elif a_col == b_col:
            return table[(a_row - 1) % 5][a_col] + table[(b_row - 1) % 5][b_col]
        else:
            return table[a_row][b_col] + table[b_row][a_col]

    encrypted_message = encrypted_message.lower().replace('j', 'i')  # Replace 'j' with 'i'
    message_length = len(encrypted_message)
    decrypted_message = ""
    table = generate_playfair_table(keyword)

    i = 0
    while i < message_length:
        pair = encrypted_message[i:i+2]
        if len(pair) < 2 or pair[0] == pair[1]:
            pair = pair[0] + 'x'
            i -= 1  # Process the same pair in the next iteration

        decrypted_pair = decrypt_pair(table, pair)
        decrypted_message += decrypted_pair

        i += 2

    return decrypted_message.upper()






# Function to convert a text string to a matrix
def text_to_matrix(text, size):
    matrix = []
    for char in text:
        matrix.append(ord(char) - ord('A'))  # Convert characters to numbers (0-25)
    while len(matrix) % size != 0:
        matrix.append(0)  # Padding with zeros if necessary
    return np.array(matrix).reshape(-1, size)

# Function to convert a matrix to a text string
def matrix_to_text(matrix):
    text = ""
    for row in matrix:
        for element in row:
            text += chr(element + ord('A'))  # Convert numbers to characters
    return text

# Function to encrypt a text using the Hill cipher
def hill_encrypt(plaintext, key):
    size = key.shape[0]
    plaintext_matrix = text_to_matrix(plaintext, size)
    encrypted_matrix = np.matmul(plaintext_matrix, key) % 26  # Matrix multiplication modulo 26
    return matrix_to_text(encrypted_matrix)

# Function to decrypt an encrypted text using the Hill cipher
def hill_decrypt(ciphertext, key):
    size = key.shape[0]
    ciphertext_matrix = text_to_matrix(ciphertext, size)
    key_inverse = np.linalg.inv(key)  # Inverse of the key matrix
    key_inverse = np.round(key_inverse * np.linalg.det(key) % 26).astype(int)  # Modulo 26 and rounding
    decrypted_matrix = np.matmul(ciphertext_matrix, key_inverse) % 26  # Matrix multiplication modulo 26
    return matrix_to_text(decrypted_matrix)
