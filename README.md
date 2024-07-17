# Cipher Encrypter/Decrypter (Caesar Cipher)

This project aimed to replicate the infamous caesar cipher. The program shifts letters in a message to make it unreadable if intercepted. To decrypt, the receiver reverses the shift. 

Python Familiarities:
- Variables
- Data Types
- Functions
- Lists 
- Loops
- Control Statements

## Learn More

Learn more about the [Ceasar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) 

## Version Control

Utilized git for version control and code management. Download for your OS below:

- [Download for Windows](https://git-scm.com/download/win)
- [Download for Mac](https://git-scm.com/download/mac)
- [Download for Linux](https://git-scm.com/download/linux)

## Key Functions Utilized

```python

# Function for Encryption
def encrypt(plain_text, shift_amount):
        cipher_text = ""
        for letter in plain_text:
            position = alphabet.index(letter)
            new_position = position + shift_amount
            cipher_text += alphabet[new_position]
        print(f"The encoded text is {cipher_text}")

# Function for Decryption
def decrypt(textmsg, secondshift):
        decoded_text = ""
        for items in textmsg:
            secposition = alphabet.index(items)
            newest_position = secposition - secondshift
            decoded_text += alphabet[newest_position]
        print(f"The decoded text is {decoded_text}") 

# Function for Re-Execution
def choice():
        global cipher_complete # Global specifies the variable outside this for loop. This is needed to escape the cipher
        choice = input("Would you like to run this cipher again? Type 'yes' or 'no':\n").lower()
        if choice == "no":
            print("The cipher program has now completed.")
            cipher_complete = True

```