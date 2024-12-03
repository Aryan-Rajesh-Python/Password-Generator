import secrets
import string
import pyfiglet

def password_generator():
    app = pyfiglet.figlet_format("Password Generator")
    print(app)

    # Define the character sets for password generation
    lst1 = string.ascii_letters  # a-zA-Z
    lst2 = string.digits          # 0-9
    lst3 = string.punctuation     # Special characters
    
    # Take user input for the total length and other password parameters
    n = int(input("Enter the number of letters: "))
    a = int(input("Enter the number of digits: "))
    b = int(input("Enter the number of special characters: "))
    
    total_length = n + a + b
    if total_length < 12:  # Password length check
        print("For better security, the password should be at least 12 characters long.")
        return

    # Generate the password parts
    password = [
        secrets.choice(lst1) for _ in range(n)
    ] + [
        secrets.choice(lst2) for _ in range(a)
    ] + [
        secrets.choice(lst3) for _ in range(b)
    ]
    
    # Shuffle the password to make it more secure
    secrets.SystemRandom().shuffle(password)

    # Join the list into a string
    final_password = ''.join(password)

    print(f"Generated Password is: {final_password}")

while True:
    choice = input("Do you want to continue generating passwords (yes/no)? ").strip().lower()
    if choice == "yes":
        password_generator()
    elif choice == "no":
        print("Thank you for using our application!")
        break
    else:
        print("Please enter 'yes' or 'no'.")
