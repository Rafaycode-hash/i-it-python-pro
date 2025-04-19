def check_password_strength(passwords):
    strength_criteria = {
        "length": lambda p: len(p) >= 8,
        "upper_case": lambda p: any(c.isupper() for c in p),
        "digit": lambda p: any(c.isdigit() for c in p)
    }

    for password in passwords:
        print(f"Checking password: {password}")
        if all(criterion(password) for criterion in strength_criteria.values()):
            print("Password is strong.")
        else:
            print("Password is weak.")

def main():
    passwords = ["password123", "P@ssw0rd", "helloWorld1"]
    check_password_strength(passwords)

if __name__ == "__main__":
    main()
