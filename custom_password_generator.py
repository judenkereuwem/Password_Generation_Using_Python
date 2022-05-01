#custom random password generator using python
#October 2021

import string
import random

alphabets = list(string.ascii_letters)
digits = list(string.digits)
special_characters = list("!@#$%^&*()")
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")


def generate_random_password():
    length = int(input("Enter password length: "))
    digits_count = int(input("Enter digit count: "))
    alphabets_count = int(input("Enter alphabet count: "))
    special_characters_count = int(input("Enter special character count: "))

    characters_count = alphabets_count + digits_count + special_characters_count

    if characters_count > length:
        print("Total Character count greater than password length")
        return
    password = []

    for i in range(alphabets_count):
        password.append(random.choice(alphabets))

    for i in range(digits_count):
        password.append(random.choice(digits))

    for i in range(special_characters_count):
        password.append(random.choice(special_characters))

    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    random.shuffle(password)

    print("")
    print("Password: " + "".join(password))

generate_random_password()
    
                          
