# Password Generator

This is a Python-based **Password Generator** application that allows users to generate strong and secure passwords. The generated passwords can include a combination of letters, digits, and special characters. Additionally, the program evaluates the strength of the generated password and offers the option to save it securely in an encrypted file.

## Features

- **Password Generation**: Generate passwords with a customizable number of letters, digits, and special characters.
- **Password Strength Evaluation**: Evaluate the strength of the generated password based on length, and character variety (uppercase, lowercase, digits, special characters).
- **Password Encryption**: Encrypt the generated passwords using `cryptography.fernet.Fernet` before saving them.
- **Logging**: Log errors, warnings, and important events in the password generation process.
- **File Handling**: Save encrypted passwords securely in a file, preventing plain-text storage.
- **Input Validation**: Ensure valid user inputs and provide helpful error messages.
- **Customizable Lengths**: Set the minimum length for generated passwords.

## Requirements

- Python 3.x
- Libraries:
  - `secrets`
  - `string`
  - `pyfiglet`
  - `os`
  - `re`
  - `logging`
  - `cryptography`

You can install the necessary dependencies using pip:

```bash
pip install cryptography pyfiglet
```

## Installation

```bash
git clone https://github.com/Aryan-Rajesh-Python/Password-Generator.git
python passwordgenerator.py
```
