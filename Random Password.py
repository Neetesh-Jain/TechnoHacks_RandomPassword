import random
import string
import sys

def generate_password(length, use_letters=True, use_digits=True, use_special=True, exclude_similar=False):
    # Validate the length of the password
    if length < 4:
        print("Password length should be at least 4 to include all character types.")
        sys.exit(1)  # Exit the program with an error code

    # Define character pools
    letters = string.ascii_letters
    digits = string.digits
    special_chars = string.punctuation
    similar_chars = 'oO0l1I|'

    # Initialize the character set
    characters = ''
    if use_letters:
        characters += letters
    if use_digits:
        characters += digits
    if use_special:
        characters += special_chars
    
    # Exclude similar looking characters if needed
    if exclude_similar:
        characters = ''.join(ch for ch in characters if ch not in similar_chars)

    if not characters:
        print("At least one character type must be selected.")
        sys.exit(1)

    # Ensure the password contains at least one of each required character type
    password = []
    if use_letters:
        password.append(random.choice(letters))
    if use_digits:
        password.append(random.choice(digits))
    if use_special:
        password.append(random.choice(special_chars))
    
    # Fill the remaining length of the password
    password += [random.choice(characters) for _ in range(length - len(password))]
    
    # Shuffle to avoid predictable patterns
    random.shuffle(password)
    
    return ''.join(password)

# User input for password settings
try:
    length = int(input("Enter the password length (minimum 4): "))
    if length < 4:
        print("Password length should be at least 4.")
        sys.exit(1)  # Exit if length is less than 4
    
    exclude_similar = input("Exclude similar characters (y/n): ").lower() == 'y'
    use_letters = input("Include letters (y/n): ").lower() == 'y'
    use_digits = input("Include digits (y/n): ").lower() == 'y'
    use_special = input("Include special characters (y/n): ").lower() == 'y'

    password = generate_password(length, use_letters, use_digits, use_special, exclude_similar)
    print(f"Generated password: {password}")

except ValueError:
    print("Invalid input! Please enter a valid number for password length.")
    sys.exit(1)
