print("Welcome to the password generator!")
import random
import string

letters = string.ascii_letters
numbers = string.digits
symbols = string.punctuation

nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
# Easy Level

# Hard Level
password_list = []
for char in range(0, nr_letters):
    password_list.append(random.choice(letters))
for char in range(0, nr_symbols):
    password_list.append(random.choice(symbols))
for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
random.shuffle(password_list) # This will shuffle the password list
password = ""
for char in password_list:
    password += char
print("Your password is: ", password)
# The code above generates a random password based on user input for the number of letters, symbols, and numbers. It uses both easy and hard levels of password generation. The easy level simply concatenates the characters, while the hard level shuffles the characters before creating the final password.