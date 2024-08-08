import argparse
from cryptography.fernet import Fernet
import os

def generate_key(key_file):
    """Generate a key and save it to a file."""
    key = Fernet.generate_key()
    with open(key_file, "wb") as key_file:
        key_file.write(key)

def load_key(key_file):
    """Load the key from the specified key file."""
    try:
        with open(key_file, "rb") as file:
            return file.read()
    except FileNotFoundError:
        print(f"Key file '{key_file}' not found. Please generate a key first.")
        exit()

def encrypt_file(file_name, key):
    """Encrypt the file with the provided key."""
    fernet = Fernet(key)
    with open(file_name, "rb") as file:
        original = file.read()
    encrypted = fernet.encrypt(original)
    with open(file_name + ".encrypted", "wb") as encrypted_file:
        encrypted_file.write(encrypted)

def decrypt_file(file_name, key):
    """Decrypt the file with the provided key."""
    fernet = Fernet(key)
    with open(file_name, "rb") as enc_file:
        encrypted = enc_file.read()
    decrypted = fernet.decrypt(encrypted)
    output_file = file_name.replace(".encrypted", "")
    with open(output_file, "wb") as dec_file:
        dec_file.write(decrypted)
    return output_file

def display_file_contents(file_name):
    """Display the contents of the file."""
    try:
        with open(file_name, "r") as file:
            content = file.read()
        print(f"\nContenu du fichier '{file_name}':\n")
        print(content)
    except Exception as e:
        print(f"Could not read the file '{file_name}': {e}")

parser = argparse.ArgumentParser(description='Encrypt or decrypt a file.')
parser.add_argument('mode', choices=['encrypt', 'decrypt'], help='Select whether to encrypt or decrypt the file.')
parser.add_argument('file_name', help='The name of the file to encrypt or decrypt.')
parser.add_argument('--key_file', help='Specify a key file to use. If not provided, "secret.key" will be used.', default="secret.key")

args = parser.parse_args()

if args.mode == 'encrypt':
    if not os.path.exists(args.key_file):
        generate_key(args.key_file)
    key = load_key(args.key_file)
    encrypt_file(args.file_name, key)
    print(f"File '{args.file_name}' has been encrypted.")
elif args.mode == 'decrypt':
    key = load_key(args.key_file)
    decrypted_file = decrypt_file(args.file_name, key)
    print(f"File '{args.file_name}' has been decrypted.")
    display_file_contents(decrypted_file)
