import secrets
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

def password_generator():
    password_length = input("Enter the desired length of the password: ")

    if password_length.isdigit():
        password = generate_password(int(password_length))
        print(f"Generated Password: {password}")
    else:
        print("Error: Please enter a valid numeric value for password length.")

password_generator()
