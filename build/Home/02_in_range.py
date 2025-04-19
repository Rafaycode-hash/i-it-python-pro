def check_range():
    print("Check if a number is within the range (1 to 100).")
    try:
        number = int(input("Enter a number: "))
        if 1 <= number <= 100:
            print(f"{number} is within the range.")
        else:
            print(f"{number} is outside the range.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    check_range()
