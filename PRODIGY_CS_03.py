import re

def assess_password_strength(password):
    # Initialize the score
    score = 0

    # Check the password length
    if len(password) < 8:
        print("Password should be at least 8 characters.")
    else:
        score += 1

    # Check for uppercase letters
    if re.search("[A-Z]", password):
        score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    # Check for lowercase letters
    if re.search("[a-z]", password):
        score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    # Check for numbers
    if re.search("[0-9]", password):
        score += 1
    else:
        print("Password should contain at least one number.")

    # Check for special characters
    if re.search("[^A-Za-z0-9]", password):
        score += 1
    else:
        print("Password should contain at least one special character.")

    # Calculate the password strength
    if score == 5:
        print("Password strength: Strong")
    elif score >= 3:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

def main():
    password = input("Enter a password: ")
    assess_password_strength(password)

if __name__ == "__main__":
    main()