
import re


def analyze_password(password):

    # Check password length
    length_check = len(password) >= 8
    long_length_check = len(password) >= 12

    # Check uppercase letters
    uppercase_check = bool(re.search(r"[A-Z]", password))

    # Check lowercase letters
    lowercase_check = bool(re.search(r"[a-z]", password))

    # Check numbers
    number_check = bool(re.search(r"[0-9]", password))

    # Check special characters
    special_check = bool(re.search(r"[^A-Za-z0-9]", password))

    # Store all checks
    checks = {
        "At least 8 characters": length_check,
        "At least 12 characters": long_length_check,
        "Uppercase letter (A-Z)": uppercase_check,
        "Lowercase letter (a-z)": lowercase_check,
        "Number (0-9)": number_check,
        "Special character (@, #, !)": special_check
    }

    # Calculate password score
    score = sum(checks.values())

    # Check for common weak passwords
    common_passwords = [
        "password",
        "password123",
        "123456",
        "12345678",
        "qwerty",
        "admin",
        "abc123"
    ]

    is_common = password.lower() in common_passwords

    # Determine password strength
    if is_common or score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    elif score == 5:
        strength = "Strong"

    else:
        strength = "Very Strong"

    # Generate improvement suggestions
    suggestions = []

    if not length_check:
        suggestions.append("Use at least 8 characters.")

    if not long_length_check:
        suggestions.append("Use 12 or more characters for better security.")

    if not uppercase_check:
        suggestions.append("Add at least one uppercase letter.")

    if not lowercase_check:
        suggestions.append("Add at least one lowercase letter.")

    if not number_check:
        suggestions.append("Add at least one number.")

    if not special_check:
        suggestions.append("Add a special character like @, #, or !.")

    if is_common:
        suggestions.append("Avoid common passwords. Choose a unique password.")

    # Return analysis results
    return {
        "score": score,
        "strength": strength,
        "checks": checks,
        "suggestions": suggestions
    }
