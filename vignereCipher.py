#Nathan Lawson
#encrpt Exercise / All work is my own
#September 23, 2023

"""
This program uses Vigenere Cipher that takes a user input encrypts the message/
and then prints the encrypted message back out to the user.
"""

def vignereCipherEncryption():

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    inputString = ""

    encryptKey = ""

    encryptString = ""


    encryptKey = input("Please enter an encryption key: ")

    encryptKey = encryptKey.lower()

    inputString = input("Please enter a sentence to encrypt: ")
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

            encryptString = newCharacter + encryptString

        else:

            encryptString = letter + encryptString

    return(encryptString)

print(vignereCipherEncryption())


    
