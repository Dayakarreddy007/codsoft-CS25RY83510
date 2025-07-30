import random
import string

def generate_password(length):
    # Define character pools
    characters = string.ascii_letters + string.digits + string.punctuation

    # Ensure the password is at least 4 characters long
    if length < 4:
        return "Password length should be at least 4 characters."

    # Generate a random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        # Get user input
        length = int(input("Enter the desired password length: "))
        
        # Generate and display the password
        password = generate_password(length)
        print(f"Generated Password: {password}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
