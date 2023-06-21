import numpy as np
import string

def caesar_encrypt(message, shift):
    encrypted = ""
    for char in message:
        if char.isalpha():
            #Trovo l'intero corrispondente il char
            charPos = ord(char.lower()) - ord("a") #Tolgo e successivamento aggiungo ord("a") 
                                                   #poichè essendo il primo char dell'alfabeto 
                                                   #farà da limitatore 
                                                   #quando farò il wrap around
            #Applico lo spostamento e gestisco il wrap-around
            newPos = ((charPos + shift) % 26)
            #Ottengo il nuovo char sapendone l'intero corrispondente
            newChar = chr(newPos + ord("a"))
            #Riporto in maiuscolo la lettera se lo era in precedenza
            if char.isupper():
                newChar = newChar.upper()
            #Aggiungo il char cifrato al testo cifrato
            encrypted += newChar
        else:
            #Mantengo i caratteri non alfabetici come sono
            encrypted += char
    return encrypted

def ceasar_decrypt(crypted, shift):
    decripted = ""
    for char in crypted:
        if char.isalpha():
            # Trovo l'intero corrspondente il char
            charPos = ord(char.lower()) - ord('a')
            # Applico lo spostamento e gestisco il wrap-around
            newPos = (charPos - shift) % 26
            # Ottengo il nuovo char sapendone l'intero corrispondente
            newChar = chr(newPos + ord('a'))
            # Riporto in maiuscolo la lettera se lo wra in precedenza
            if char.isupper():
                newChar = newChar.upper()
            # Aggiungo il char cifrato al testo cifrato
            decripted += newChar
        else:
            # Mantengo i caratteri non alfabetici come sono
            decripted += char
    return decripted
######## Sostituzione
def remove(stringa):
    caratteri_unici = set()
    new_stringa = ''
    for char in stringa:
        if char == " ":
            print("Ciao")
        elif char not in caratteri_unici:
            new_stringa += char
            caratteri_unici.add(char)
    return new_stringa

def alphabet_complete(key):
    for char in string.ascii_lowercase:
        if char not in key:
            key = key + char
    return key

def substitution_encrypt(plaintext, key):
    substitution_map = {}
    for i, char in enumerate(key):
        substitution_map[string.ascii_lowercase[i]] = char

    ciphertext = ""
    for char in plaintext.lower():
        if char in substitution_map:
            ciphertext += substitution_map[char]
        else:
            ciphertext += char

    return ciphertext

def substitution_decrypt(ciphertext, key):
    inverse_substitution_map = {}
    for i, char in enumerate(key):
        inverse_substitution_map[key[i]] = string.ascii_lowercase[i]

    plaintext = ""
    for char in ciphertext.lower():
        if char in inverse_substitution_map:
            plaintext += inverse_substitution_map[char]
        else:
            plaintext += char

    return plaintext



#################
def vigenere_encrypt(plaintext, key):
    encrypted_text = ""
    key_length = len(key)
    for i, c in enumerate(plaintext):
        if c.isalpha():
            # Calcolo l'index della lettera nel testo in chiaro
            p_index = ord(c.upper()) - ord('A')
            # Calcolo l'index della lettera corrispondente nella chiave
            k_index = ord(key[i % key_length].upper()) - ord('A')
            # Calcolo l'index della lettera cifrata
            encrypted_index = (p_index + k_index) % 26
            # Converte l'index nella lettera corrispondente
            encrypted_char = chr(encrypted_index + ord('A'))
            # Aggiungo la lettera cifrata al testo cifrato
            encrypted_text += encrypted_char
        else:
            # Manteniamo i caratteri non alfabetici come sono
            encrypted_text += c
    return encrypted_text


def vigenere_decrypt(ciphertext, key):
    decrypted_text = ""
    key_length = len(key)
    for i, c in enumerate(ciphertext):
        if c.isalpha():
            # Calcolo l'index della lettera nel testo cifrato
            c_index = ord(c.upper()) - ord('A')
            # Calcolo l'index della lettera corrispondente nella chiave
            k_index = ord(key[i % key_length].upper()) - ord('A')
            # Calcolo l'index della lettera decifrata
            decrypted_index = (c_index - k_index) % 26
            # Converto l'index nella lettera corrispondente
            decrypted_char = chr(decrypted_index + ord('A'))
            # Aggiungo la lettera decifrata al testo decifrato
            decrypted_text += decrypted_char
        else:
            # Mantengo i caratteri non alfabetici come sono
            decrypted_text += c
    return decrypted_text