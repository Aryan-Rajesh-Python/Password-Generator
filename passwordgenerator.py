import secrets
import string
import pyfiglet
import os
import re
import logging
from cryptography.fernet import Fernet

# Ensure the logging directory exists
log_dir = os.path.expanduser('~/passwords')
os.makedirs(log_dir, exist_ok=True)

# Configure logging
log_file = os.path.join(log_dir, 'password_generator.log')
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Generate or load encryption key
key_file = os.path.expanduser("~/passwords/secret.key")
if not os.path.exists(key_file):
    key = Fernet.generate_key()
    with open(key_file, 'wb') as kf:
        kf.write(key)
else:
    with open(key_file, 'rb') as kf:
        key = kf.read()
fernet = Fernet(key)

def password_generator(num_letters, num_digits, num_specials, min_length=12):
    """
    Generates a secure password with letters, digits, and special characters.
    """
    letters = string.ascii_letters
    digits = string.digits
    specials = "!@#$%^&*()-_=+<>?/"

    # Validate inputs
    if num_letters < 0 or num_digits < 0 or num_specials < 0:
        logging.error("Negative values provided for character counts.")
        return "Error: Inputs must be non-negative integers."

    num_letters, num_digits, num_specials = adjust_lengths(num_letters, num_digits, num_specials, min_length)

    try:
        password = (
            ''.join(secrets.choice(letters) for _ in range(num_letters)) +
            ''.join(secrets.choice(digits) for _ in range(num_digits)) +
            ''.join(secrets.choice(specials) for _ in range(num_specials))
        )
        return ''.join(secrets.SystemRandom().sample(password, len(password)))
    except Exception as e:
        logging.error(f"Password generation failed: {e}")
        return f"Error: Failed to generate password. {e}"

def adjust_lengths(num_letters, num_digits, num_specials, min_length):
    """
    Adjust the lengths of the different character types to meet the minimum length requirement.
    """
    total_length = num_letters + num_digits + num_specials
    if total_length < min_length:
        remaining = min_length - total_length
        num_letters += remaining // 2
        num_digits += remaining // 4
        num_specials += remaining - (remaining // 2 + remaining // 4)
    return num_letters, num_digits, num_specials

def password_strength(password):
    """
    Evaluates password strength with stricter criteria.
    """
    score = 0
    length_criteria = [12, 16, 20]
    if len(password) >= length_criteria[0]:
        score += 1
    if len(password) >= length_criteria[1]:
        score += 1
    if len(password) >= length_criteria[2]:
        score += 1
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        score += 1
    if re.search(r'\d', password):
        score += 1
    if re.search(r'[!@#$%^&*()-_=+<>?/]', password):
        score += 1

    strengths = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong", "Extremely Strong"]
    return strengths[min(score, len(strengths) - 1)]

def get_user_input(min_length=12):
    """
    Prompts the user to enter the number of letters, digits, and special characters for the password.
    Ensures input validity and minimum password length.
    """
    while True:
        try:
            print("\nEnter the number of each type of character for your password:")
            num_letters = int(input("Number of letters (a-z, A-Z): "))
            num_digits = int(input("Number of digits (0-9): "))
            num_specials = int(input("Number of special characters (!@#$%^&*): "))

            total_length = num_letters + num_digits + num_specials
            if total_length > 100:
                print("Error: Password length is too large. Please keep it under 100.")
                logging.warning("User attempted to create an excessively large password.")
            elif total_length < min_length:
                print(f"Error: Password length must be at least {min_length}.")
                logging.warning("User attempted to create a password shorter than the minimum length.")
            else:
                return num_letters, num_digits, num_specials
        except ValueError:
            print("Error: Please enter valid integers.")
            logging.warning("User entered invalid input.")

def save_password_to_file(password):
    """
    Saves the generated password to a file in the user's home directory.
    Encrypts the password before saving.
    """
    try:
        encrypted_password = fernet.encrypt(password.encode())
        file_path = os.path.expanduser('~/passwords/generated_passwords.txt')
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, "ab") as file:
            file.write(encrypted_password + b"\n")
        print(f"Password saved to {file_path}.")
        logging.info("Password saved successfully.")
    except Exception as e:
        print(f"Error saving password: {e}")
        logging.error(f"Failed to save password: {e}")

def confirm(prompt):
    """
    Prompts the user for a yes/no confirmation and validates the input.
    """
    while True:
        choice = input(f"{prompt} (yes/no): ").strip().lower()
        if choice in {"yes", "no"}:
            return choice == "yes"
        print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    """
    Main function that runs the password generator program.
    Includes options for generating, evaluating, and saving passwords.
    """
    try:
        print(pyfiglet.figlet_format("Password Generator"))
    except Exception as e:
        logging.warning(f"Pyfiglet failed: {e}")
        print("Password Generator")

    min_length = 12
    while True:
        print("\n1. Generate a Password\n2. Exit")
        choice = input("Enter your choice: ").strip()
        if choice == "1":
            # Directly proceed with password generation instead of asking again
            num_letters, num_digits, num_specials = get_user_input(min_length)
            password = password_generator(num_letters, num_digits, num_specials, min_length)

            if "Error" in password:
                print(password)
            else:
                print(f"\nGenerated Password: {password}")
                print(f"Password Strength: {password_strength(password)}")

                if confirm("Would you like to save this password to a file?"):
                    save_password_to_file(password)
                else:
                    print("Password not saved.")
        elif choice == "2":
            print("Thank you for using the Password Generator. Goodbye!")
            logging.info("User exited the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
