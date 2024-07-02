# README

## Description

This Python script provides functions to encrypt and decrypt text using the Caesar Cipher technique. The Caesar Cipher is a type of substitution cipher where each letter in the plaintext is shifted a certain number of places down the alphabet.

## Functions

### `caesar_cipher_encrypt(text, key)`

Encrypts a given text using the Caesar Cipher with a specified key.

- **Parameters:**
  - `text` (str): The plaintext to be encrypted.
  - `key` (int): The number of positions to shift each character.

- **Returns:**
  - `str`: The encrypted text.

### `caesar_cipher_decrypt(text, key)`

Decrypts a given text that was encrypted using the Caesar Cipher with a specified key.

- **Parameters:**
  - `text` (str): The encrypted text to be decrypted.
  - `key` (int): The number of positions to shift each character back.

- **Returns:**
  - `str`: The decrypted text.

### `caesar_cipher_decrypt_all(text)`

Decrypts a given text by trying all possible keys (1 through 25) and prints the decrypted text for each key.

- **Parameters:**
  - `text` (str): The encrypted text to be decrypted.

### `caesar_cipher_decrypt_most_likely(text)`

Decrypts a given text by trying all possible keys (1 through 25) and returns the most likely decrypted text and its corresponding key. The likelihood is determined by counting the number of common French words in the decrypted text.

- **Parameters:**
  - `text` (str): The encrypted text to be decrypted.

- **Returns:**
  - `tuple`: A tuple containing the most likely decrypted text and the key used for decryption.

## Usage

1. **Encrypting Text**

```python
from caesar_cipher import caesar_cipher_encrypt

plaintext = "Bonjour, comment ça va?"
key = 3
encrypted_text = caesar_cipher_encrypt(plaintext, key)
print("Encrypted Text:", encrypted_text)
```

2. **Decrypting Text**

```python
from caesar_cipher import caesar_cipher_decrypt

encrypted_text = "Erqmrxu, frpphqw gd yd?"
key = 3
decrypted_text = caesar_cipher_decrypt(encrypted_text, key)
print("Decrypted Text:", decrypted_text)
```

3. **Decrypting Text with All Possible Keys**

```python
from caesar_cipher import caesar_cipher_decrypt_all

encrypted_text = "Erqmrxu, frpphqw gd yd?"
caesar_cipher_decrypt_all(encrypted_text)
```

4. **Finding the Most Likely Decryption**

```python
from caesar_cipher import caesar_cipher_decrypt_most_likely

encrypted_text = "Erqmrxu, frpphqw gd yd?"
most_likely_text, most_likely_key = caesar_cipher_decrypt_most_likely(encrypted_text)
print("Most Likely Decrypted Text:", most_likely_text)
print("Key Used:", most_likely_key)
```

## Dependencies

This script requires Python 3 and no additional libraries.

## License

This project is licensed under the MIT License.

## Author

Your Name (your.email@example.com)

Feel free to modify and improve this script as needed. If you have any questions or suggestions, please contact the author.