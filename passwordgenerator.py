import secrets
import string
import pyfiglet

def password_generator(n, a, b):
    """Generates a password with specified number of letters, digits, and special characters."""
    # Define character sets
    letters = string.ascii_letters  # a-zA-Z
    digits = string.digits          # 0-9
    punctuation = string.punctuation  # Special characters

    # Validate inputs
    if n < 0 or a < 0 or b < 0:
        return "Error: Negative values are not allowed."
    
    total_length = n + a + b
    if total_length < 12:
        return "Error: For better security, the password should be at least 12 characters long."

    # Generate password parts
    password = (
        [secrets.choice(letters) for _ in range(n)] +
        [secrets.choice(digits) for _ in range(a)] +
        [secrets.choice(punctuation) for _ in range(b)]
    )
    
    # Shuffle and combine
    secrets.SystemRandom().shuffle(password)
    return ''.join(password)

def main():
    # Display the application header
    print(pyfiglet.figlet_format("Password Generator"))

    while True:
        choice = input("Do you want to generate passwords (yes/no)? ").strip().lower()
        if choice == "yes":
            try:
                n = int(input("Enter the number of letters: "))
                a = int(input("Enter the number of digits: "))
                b = int(input("Enter the number of special characters: "))
                password = password_generator(n, a, b)
                if "Error" in password:
                    print(password)  # Display error message
                else:
                    print(f"Generated Password is: {password}")
            except ValueError:
                print("Error: Please enter valid numbers.")
        elif choice == "no":
            print("Thank you for using our application!")
            break
        else:
            print("Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()
