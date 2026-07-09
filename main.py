import re
import getpass

def check_password_strength(password):
    score = 0
    suggestions = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
        suggestions.append("Make it at least 12 characters long.")
    else:
        suggestions.append("Password is too short. Use at least 8 characters, best is 12+.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        suggestions.append("Add at least one uppercase letter, like A, B, C.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Add at least one lowercase letter, like a, b, c.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        suggestions.append("Add at least one number, like 1, 2, 3.")

    if re.search(r"[!@#$%^&*()_+\-=\[\]{};':\"\\|,.<>/?]", password):
        score += 1
    else:
        suggestions.append("Add at least one special character, like @, #, $, %.")

    common_passwords = ["password", "123456", "qwerty", "admin", "111111", "iloveyou"]

    if password.lower() in common_passwords:
        score = 0
        suggestions.append("Do not use common passwords like password, 123456, qwerty.")

    if " " in password:
        suggestions.append("Avoid spaces in your password.")

    if score >= 6:
        strength = "Strong"
    elif score >= 4:
        strength = "Medium"
    else:
        strength = "Weak"

    return strength, suggestions


password = getpass.getpass("Enter your password: ")

strength, suggestions = check_password_strength(password)

print("\nPassword Strength:", strength)

if suggestions:
    print("\nImprovements needed:")
    for suggestion in suggestions:
        print("-", suggestion)
else:
    print("Your password is strong. No improvement needed.")
