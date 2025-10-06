# Caesar Cipher

# import art
# print(art.logo)


print("Welcome to the Caesar Cipher Encoder/Decoder!")
alphabet = 'abcdefghijklmnopqrstuvwxyz'
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        if letter not in alphabet:
            cipher_text += letter
            continue
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_amount):
    plain_text = ""
    for letter in cipher_text:
        if letter not in alphabet:
            plain_text += letter
            continue
        shifted_position = alphabet.index(letter) - shift_amount
        shifted_position %= len(alphabet)
        plain_text += alphabet[shifted_position]
    print(f"The decoded text is {plain_text}")
    

if direction == "encode":
    encrypt(plain_text=text, shift_amount=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_amount=shift)
