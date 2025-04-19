import random
import string

def generate_password(length):
    if length < 4:
        return "❌ Password length should be at least 4"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User input
try:
    user_length = int(input("Enter password length: "))
    password = generate_password(user_length)
    print("🔐 Your Password is:", password)
except ValueError:
    print("❌ Please enter a valid number.")
