#random password generator using python
#October 2021

import string
import random

#characters to generate password from
characters = list(string.ascii_letters + string.digits + " !@#$%^&*()")

def generate_random_password():
    #lenght of password from user
    length = int(input("Enter password length: "))

    #shuffling the password
    random.shuffle(characters)

    #picking random characters from the list
    password = []
    for i in range(length):
        password.append(random.choice(characters))

    #shuffling the resultant password
    random.shuffle(password)

    #converting the list to string and printing the list
    print("".join(password))

#calling the function
generate_random_password()
                 
