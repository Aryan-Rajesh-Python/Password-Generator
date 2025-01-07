import secrets
import string
import pyfiglet

def password_generator(num_letters, num_digits, num_specials):
    """Generates a secure password with specified numbers of letters, digits, and special characters."""
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    specials = string.punctuation

    # Validate inputs
    if num_letters < 0 or num_digits < 0 or num_specials < 0:
        return "Error: Please enter non-negative values for all inputs."

    total_length = num_letters + num_digits + num_specials
    if total_length < 12:
        return "Error: Password length must be at least 12 characters for better security."
    if total_length == 0:
        return "Error: At least one character must be included in the password."

    # Generate password components
    password = (
        [secrets.choice(letters) for _ in range(num_letters)] +
        [secrets.choice(digits) for _ in range(num_digits)] +
        [secrets.choice(specials) for _ in range(num_specials)]
    )

    # Shuffle and return the password
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def get_user_input():
    """Handles user input for password generation."""
    try:
        print("\nEnter the number of each type of character for your password:")
        num_letters = int(input("Number of letters (a-z, A-Z): "))
        num_digits = int(input("Number of digits (0-9): "))
        num_specials = int(input("Number of special characters (!@#$%&*): "))
        return num_letters, num_digits, num_specials
    except ValueError:
        print("Error: Please enter valid integer numbers.")
        return None

def save_password_to_file(password):
    """Appends the password to a file."""
    try:
        with open("generated_passwords.txt", "a") as file:
            file.write(password + "\n")
        print("Password appended to 'generated_passwords.txt'.")
    except Exception as e:
        print(f"Error saving password to file: {e}")

def main():
    """Main application loop for the Password Generator."""
    print(pyfiglet.figlet_format("Password Generator"))
    while True:
        choice = input("Do you want to generate a password (yes/no)? ").strip().lower()
        if choice == "yes":
            user_input = get_user_input()
            if user_input:
                num_letters, num_digits, num_specials = user_input
                password = password_generator(num_letters, num_digits, num_specials)

                # Display the result or error
                if password.startswith("Error"):
                    print(password)
                else:
                    print(f"\nGenerated Password: {password}")
                    save_choice = input("Would you like to save this password to a file (yes/no)? ").strip().lower()
                    if save_choice == "yes":
                        save_password_to_file(password)
        elif choice == "no":
            print("Thank you for using the Password Generator. Goodbye!")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
