# If you want to read more about the Cipher used check out: https://pages.mtu.edu/~shene/NSF-4/Tutorial/VIG/Vig-Base.html
# They have a great explanation of how the cipher works.

#import tkinter as tk
#from tkinter import *

from tkinter import messagebox, simpledialog, Tk

#This will run first and ask the user if they wish to encrypt or decrypt.
def get_task():
    task = simpledialog.askstring('Task', 'Do you want to encrypt or decrypt?')
    return task

#Then the program will ask the user to provoide an encryption key.
def get_key():
    key = simpledialog.askstring('key', 'Please enter encryption key: ')
    return key

#Then the program will ask the user for the message they want to encrypt.
def get_message():
    message = simpledialog.askstring('Message', 'Enter the secret message: ')
    return message

#This function takes the user messages and swap the letter in the message using polyalphabetic subsitution
#Fancy way of saying it uses multiple subsitution alphabets to encrypt/decrypt
def vignere_Cipher_Encryption():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    inputString = ""

    encryptionKey = ""

    encryptString = ""

    encryptKey = get_key()
    encryptKey = encryptKey.lower()
    
    inputString = get_message()
    inputString = inputString.lower()
    stringLength = len(inputString)

    # you need the key to be longer than the string so you can fully encrypt the text/
    #and this does it

    expandedKey = encryptKey

    expandedKeyLength = len(expandedKey)

    while expandedKeyLength < stringLength:

        expandedKey = expandedKey + encryptKey

        expandedKeyLength = len(expandedKey)

    keyPosition = 0

    for letter in inputString:

        if letter in alphabet:

            position = alphabet.find(letter)

            characterKey = expandedKey[keyPosition]

            keyCharacterPosition = alphabet.find(characterKey)

            keyPosition += 1

            newPosition = keyCharacterPosition + position

            if newPosition >= 26:

                newPosition -= 26

            newCharacter = alphabet[newPosition]

            encryptString  += newCharacter

        else:
            
            encryptString += letter

    return encryptString

#Should be obvious what this does... (hint: decrypt)
def vignere_Cipher_Decryption():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    inputString = ""

    decryptionKey = ""

    decryptString = ""

    decryptKey = get_key()
    decryptKey = decryptKey.lower()
    
    inputString = get_message()
    inputString = inputString.lower()
    stringLength = len(inputString)

    expandedKey = decryptKey

    expandedKeyLength = len(expandedKey)

    while expandedKeyLength < stringLength:

        expandedKey = expandedKey + decryptKey

        expandedKeyLength = len(expandedKey)

    keyPosition = 0

    for letter in inputString:

        if letter in alphabet:

            position = alphabet.find(letter)

            characterKey = expandedKey[keyPosition]

            keyCharacterPosition = alphabet.find(characterKey)

            keyPosition += 1

            newPosition = position - keyCharacterPosition

            if newPosition >= 26:

                newPosition += 26

            newCharacter = alphabet[newPosition]

            decryptString += newCharacter

        else:
            
            decryptString += letter

    return decryptString

#This while loop will check if the user aksed for the user to encrypt or decrypt then run the corresponding method. 
root = Tk()
while True:
    task = get_task()
    if task == 'encrypt':
        encrypted = vignere_Cipher_Encryption()
        messagebox.showinfo('The ciphertext of the secret message is:', encrypted)
        
    elif task == 'decrypt':
        decrypted = vignere_Cipher_Decryption()
        messagebox.showinfo('The plaintext of the secret message is:', decrypted)
    else:
        break

root.mainloop()






