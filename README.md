# Lakers Encryption Program

A simple Python-based encryption and decryption tool inspired by the Los Angeles Lakers. This program applies multiple layers of text transformation using jersey number-based shifting, substitution ciphers, and chunk reversal techniques to secure your data, with an added fun twist: a random Lakers quote is included in every encrypted file.

## Features

- **Encryption:**  
  - Character shifting based on a fixed jersey number key.
  - Substitution cipher for both vowels and selected consonants.
  - Chunk reversal of text segments.
  - Checksum validation to ensure data integrity.
  - Random Lakers quote header on encrypted files.

- **Decryption:**  
  - Reverses the encryption process to retrieve the original text.
  - Validates file integrity using checksum comparison.

## Usage

1. **Run the Program:**  
   Open a terminal, navigate to the directory containing `main.py`, and run:
   ```bash
   python3 main.py
