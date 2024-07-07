import re

def check_password_strength(password):
    length_criteria = len(password) >= 12 # Keeping 14 or more is better.
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[@#$%^&+=!]', password) is not None
    
    # Strength Evaluation
    strength = 0
    feedback = []

    if length_criteria:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
        
    if uppercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one uppercase letter.")
        
    if lowercase_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one lowercase letter.")
        
    if number_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one number.")
        
    if special_char_criteria:
        strength += 1
    else:
        feedback.append("Password should include at least one special character (e.g., @, #, $, etc.).")

    # Strength Level
    if strength <= 2:
        strength_level = "Weak"
    elif strength == 3:
        strength_level = "Moderate"
    elif strength == 4:
        strength_level = "Strong"
    else:
        strength_level = "Very Strong"

    return strength_level, feedback

password = input("Enter a password to check its strength: ")
strength_level, feedback = check_password_strength(password)

print(f"Password Strength: {strength_level}")
for suggestion in feedback:
    print(suggestion)
