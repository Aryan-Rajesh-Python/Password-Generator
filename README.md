# Password Generator

A Python-based password generator that creates secure passwords using a combination of letters, digits, and special characters. The generator uses the `secrets` module for improved security and shuffles the password characters for better randomness.

## Features

- Generates a password with a mix of uppercase letters, lowercase letters, digits, and special characters.
- Uses Python's `secrets` module for cryptographic-grade randomness.
- Shuffles the password to make the order of characters unpredictable.
- Validates user input to ensure positive values for password components.
- Ensures the generated password meets a minimum length for better security.

## Requirements

- Python 3.x
- `pyfiglet` library for text art display

To install the necessary libraries, you can run:

```bash
pip install pyfiglet
