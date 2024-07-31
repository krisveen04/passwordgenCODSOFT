import random
import string

# Define the character sets
letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

alphabet = letters + digits + special_chars

password = ''.join(random.choice(alphabet) for _ in range(8))
print("Generated password:", password)