# List that stores the letters needed. Alphabet was inputted twice in order to account for the Invalid Range error that occured.
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


# Variable used for the while loop below

cipher_complete = False
while cipher_complete == False:
# Inputs which will be called later in the code to sort through the list above and either encode/decode the 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    

# Function to encrypt the message
    def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")

# Function to decrypt the message
    def decrypt(textmsg, secondshift):
        decoded_text = ""
        for items in textmsg:
            secposition = alphabet.index(items)
            newest_position = secposition - secondshift
            decoded_text += alphabet[newest_position]
        print(f"The decoded text is {decoded_text}") 
    
# Function to either exit/continue in the loop
    def choice():
        global cipher_complete # Global specifies the variable outside this for loop. This is needed to escape the cipher
        choice = input("Would you like to run this cipher again? Type 'yes' or 'no':\n").lower()
        if choice == "no":
            print("The cipher program has now completed.")
            cipher_complete = True
            

# Calls the appropriate functions to execute the cipher program and exit loop if neeeded.
    if direction == "encode":
        encrypt(plain_text=text, shift_amount=shift)
        choice()   
    else:
        decrypt(textmsg=text, secondshift=shift)
        choice()
