import string
import sys
alphabet = []
alphabet.extend(string.ascii_lowercase)

def encrypt(message, shift):
    message_list = []
    message_list.extend(list(message))
    new_list = []
    
    for i in message_list:
        if i in alphabet:
            i = alphabet.index(i) + shift
            i = i % len(alphabet)
            letter = alphabet[i]
            new_list.extend(letter)
        else: 
            new_list.extend(i)
    
    print(f"Here's the encoded result: ")
    print(*new_list, sep = '')
    go_again()

def decrypt(message, shift):
    message_list = []
    message_list.extend(list(message))
    new_list = []
    
    for i in message_list:
        if i in alphabet:
            i = alphabet.index(i) - shift
            i = i % len(alphabet)
            letter = alphabet[i]
            new_list.extend(letter)
        else:
            new_list.extend(i)
    
    print(f"Here's the encoded result:")
    print(*new_list, sep = '')
    go_again()

def go_again():

    question = input("'yes' to go again 'no' to stop.\n")
    if question == 'yes':
        choose = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
        message = input("Type your message:\n")
        shift = input("Type your shift number:\n")
    else:
        sys.exit()
    
    new_shift = int(shift)
    start(choose, message, new_shift)

def start(choose, message, new_shift):

    if choose == 'encode':
        encrypt(message, new_shift)
    if choose == 'decode':
        decrypt(message, new_shift)

choose = input("Type 'encode' to encrypt or 'decode' to decrypt:\n")
message = input("Type your message:\n")
shift = input("Type your shift number:\n")

new_shift = int(shift)

start(choose, message, new_shift)