import random
import string

def generate_password(length=8):
    """Generate a random password with the specified length."""
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    numbers = string.digits
    symbols = string.punctuation
    characters = uppercase_letters + lowercase_letters + numbers + symbols
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Example usage:
password = generate_password(12)
print(password)
