# Password Generator

A **secure, customizable, and interactive password generator** built in Python. This application enables users to generate strong passwords by specifying the desired number of letters, digits, and special characters, ensuring compliance with modern security standards. It also provides options to save generated passwords to a file for future reference.

## Features

### 🔒 Secure Password Generation
- Utilizes Python's `secrets` module to generate cryptographically strong random passwords.
- Ensures a minimum password length of 12 characters for enhanced security.

### 🎨 Fully Customizable
- Choose the number of:
  - **Letters**: Uppercase and lowercase alphabet characters.
  - **Digits**: Numbers (0-9).
  - **Special Characters**: Symbols like `@, #, $, %`, etc.
  
### 📁 Save Passwords
- Option to save the generated password to a text file (`generated_passwords.txt`) for future use.

### 🖥️ User-Friendly Interface
- Interactive command-line interface with clear prompts for user input.
- Dynamic feedback for errors (e.g., invalid input, insufficient password length).

### 🛠️ Error Handling
- Validates user inputs to prevent negative values or invalid numbers.
- Provides clear error messages for invalid entries or password generation requirements.

## Requirements

The script requires Python 3.6 or later and the following Python libraries:

- **Standard Libraries**:
  - `secrets`
  - `string`
- **Third-party Library**:
  - `pyfiglet` (for ASCII art headers)
