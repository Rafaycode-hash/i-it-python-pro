def get_ones_digit(number):
    return abs(number) % 10  # Using abs to handle negative numbers

def main():
    try:
        num = int(input("Enter a number: "))
        ones_digit = get_ones_digit(num)
        print(f"The ones digit of {num} is: {ones_digit}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()