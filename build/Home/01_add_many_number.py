def main():
    numbers = []

    print("Enter numbers to add. Type 'done' when finished.")

    while True:
        user_input = input("Enter a number: ")

        if user_input.lower() == 'done':
            break

        try:
            number = float(user_input)
            numbers.append(number)
        except ValueError:
            print("Please enter a valid number or 'done' to finish.")

    total = sum(numbers)
    print(f"\nYou entered: {numbers}")
    print(f"Total sum: {total}")

if __name__ == "__main__":
    main()
