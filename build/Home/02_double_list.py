def double_list(numbers):
    return [num * 2 for num in numbers]

def main():
    numbers = []
    n = int(input("How many numbers do you want to enter? "))

    for i in range(n):
        number = float(input(f"Enter number {i+1}: "))
        numbers.append(number)

    doubled_numbers = double_list(numbers)

    print(f"\nOriginal list: {numbers}")
    print(f"Doubled list: {doubled_numbers}")

if __name__ == "__main__":
    main()
