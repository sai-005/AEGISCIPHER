import random
import string

def generate_random_key():
    """Generate a random substitution key."""
    letters = list(string.ascii_uppercase)
    shuffled = letters[:]
    random.shuffle(shuffled)
    key_map = dict(zip(letters, shuffled))
    return key_map

def encrypt_with_key(plaintext, key_map):
    """Encrypt using substitution key."""
    plaintext = plaintext.upper()
    ciphertext = ''.join([key_map.get(char, char) for char in plaintext if char in string.ascii_uppercase])
    return ciphertext

def decrypt_with_key(ciphertext, key_map):
    """Decrypt by reversing the substitution key."""
    ciphertext = ciphertext.upper()
    reverse_map = {v: k for k, v in key_map.items()}
    decrypted = ''.join([reverse_map.get(char, char) for char in ciphertext if char in string.ascii_uppercase])
    return decrypted
