
def vigenere(message, key, direction=1):
    key_index = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    final_message = ''

    for char in message.lower():

        # Append any non-letter character to the message
        if not char.isalpha():
            final_message += char
        else:        
            # Find the right key character to encode/decode
            key_char = key[key_index % len(key)]
            key_index += 1

            # Define the offset and the encrypted/decrypted letter
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset*direction) % len(alphabet)
            final_message += alphabet[new_index]
    
    return final_message

def encrypt(message, key):
    return vigenere(message, key)
    
def decrypt(message, key):
    return vigenere(message, key, -1)


custom_key = input("Enter custom key for encoding/decoding:")

while(True):
    choice=int(input("Press 1 for encryption\nPress 2 for decryption\nenter ur choice:"))
    if (choice == 1):
        text = input("Enter any text to encrypt: ")
        print(f"Encrypted text: {encrypt(text, custom_key)}")
    elif(choice==2):
        text = input("Enter any text to decrypt: ")
        print(f"Encrypted text: {decrypt(text, custom_key)}")
    else:
        print("Please enter right choice")
