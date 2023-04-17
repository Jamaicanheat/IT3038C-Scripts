import re


# Function to determine password strength
def check_password_strength(password):
    # Define regex patterns and weights for different password strength criteria
    pattern_lower = r'[a-z]'
    pattern_upper = r'[A-Z]'
    pattern_digit = r'\d'
    pattern_special = r'[\W_]'
    pattern_length = r'.{8,}'

    weight_lower = 1
    weight_upper = 2
    weight_digit = 2
    weight_special = 3
    weight_length = 1

    # Initialize strength score to 0
    strength = 0

    # Check for lowercase letters and update strength score
    if re.search(pattern_lower, password):
        strength += weight_lower

    # Check for uppercase letters and update strength score
    if re.search(pattern_upper, password):
        strength += weight_upper

    # Check for digits and update strength score
    if re.search(pattern_digit, password):
        strength += weight_digit

    # Check for special characters and update strength score
    if re.search(pattern_special, password):
        strength += weight_special

    # Check for minimum length and update strength score
    if re.search(pattern_length, password):
        strength += weight_length

    return strength


# Function to compare passwords and call password strength function
def compare_passwords():
    password1 = input("Enter your password: ")
    password2 = input("Re-enter your password: ")

    if password1 == password2:
        strength = check_password_strength(password1)
        if strength == 5:
            print("Password strength: Strongest (5/5)")
        elif strength >= 3:
            print("Password strength: Strong ({}/5)".format(strength))
        elif strength >= 1:
            print("Password strength: Weak ({}/5)".format(strength))
        else:
            print("Password strength: Weakest (0/5)")
    else:
        print("Passwords do not match.")


# Call the function to compare passwords and check password strength
compare_passwords()
