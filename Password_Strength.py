import re

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("➤ Password must be at least 8 characters long.")

    # 2. Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("➤ Add at least one UPPERCASE letter.")

    # 3. Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("➤ Add at least one lowercase letter.")

    # 4. Digit check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("➤ Include at least one digit (0-9).")

    # 5. Special character check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        feedback.append("➤ Include at least one special character (!@#$%^&*).")

    # Strength level
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Moderate"
    else:
        strength = "Strong"

    return score, strength, feedback

# Main program
user_password = input("Enter your password: ")
score, strength, feedback = check_password_strength(user_password)

print(f"\nPassword Strength: {strength} (Score: {score}/5)")

if strength != "Strong":
    print("Suggestions to improve your password:")
    for f in feedback:
        print(f)
else:
    print("✅ Your password is strong and secure!")
