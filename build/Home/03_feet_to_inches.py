def feet_to_inches(feet):
    return feet * 12

def main():
    try:
        feet = float(input("Enter length in feet: "))
        inches = feet_to_inches(feet)
        print(f"{feet} feet is equal to {inches} inches.")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
