def double_number(number):
    return number * 2

def main():
    try:
        num = float(input("Enter a number to double: "))
        result = double_number(num)
        print(f"The double of {num} is: {result}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()