import random
import string

def generate_password(length):
    # Combine character sets
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate the password
    password = ''.join(random.choices(characters, k=length))
    return password

def main():
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print(f"Generated password: {password}")
    except ValueError:
        print("Invalid input. Please enter a valid integer for password length.")

if __name__ == "__main__":
    main()
