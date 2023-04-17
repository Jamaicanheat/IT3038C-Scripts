# Password Strength Checker

This Python script checks the strength of a password based on a scoring system that includes different criteria such as lowercase letters, uppercase letters, digits, special characters, and minimum length. It uses regex to match the password against predefined patterns and assigns weights to each criteria to calculate the strength score.

## Requirements

This script requires Python 3.x to be installed on your system. No additional third-party libraries are needed.

## Usage

1. Run the script using a Python interpreter.
2. Enter your password when prompted.
3. Re-enter your password for verification.
4. The script will compare the two passwords for a match and then calculate the strength score based on the predefined scoring system.
5. The script will display the password strength as "Strongest (5/5)", "Strong (x/5)", "Weak (x/5)", or "Weakest (0/5)".

## Scoring System

The script uses the following scoring system to determine password strength:

- Lowercase letters: 1 point
- Uppercase letters: 2 points
- Digits: 2 points
- Special characters: 3 points
- Minimum length (8 characters or more): 1 point

The total strength score can range from 0 to 5, with 5 being the strongest and 0 being the weakest.

## Error Handling

The script includes error handling for cases where the regex patterns fail to compile, or the entered passwords do not match. In such cases, appropriate error messages will be displayed.



