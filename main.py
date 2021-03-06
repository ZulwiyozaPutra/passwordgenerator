#!/Library/Frameworks/Python.framework/Versions/3.6/bin/python3

import os
import random
import string
import time

path = os.path.dirname(os.path.abspath(__file__))

def generate_password():
    characters = string.ascii_letters + string.digits
    DEFAULT_LENGTH = 16
    password = ''
    return password.join(random.choice(characters) for _ in range(DEFAULT_LENGTH))

def generate_date():
    now = time.strftime("%c")
    return now

def create_file(email: string, password: string, date: string):
    file = open(f"{path}/passwords/passwords.txt", "a+")
    file.write(f"Krowd Credential \nEmail: {email}\nPassword: {password}\nCreated: {date}\n\n")
    file.close()
    return "password.txt"

def open_file(file_name: string):
    os.system(f"open {path}/passwords/passwords.txt")

def main():
    email = input("\nWELCOME TO KROWD PASSWORD GENERATOR\n===================================\nCreated by Zulwiyoza Putra on 18/01/18.\nCopyright © 2018 Krowd. All rights reserved.\n\nWhat is the email?\n")
    password = generate_password()
    created = generate_date()
    file_name = create_file(email, password, created)
    open_file(file_name)

if __name__ == "__main__":
    main()
