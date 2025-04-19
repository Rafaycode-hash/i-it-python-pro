def print_divisors(number):
    divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            divisors.append(i)
    return divisors

def main():
    try:
        num = int(input("Enter a number to find its divisors: "))
        divisors = print_divisors(num)
        print(f"The divisors of {num} are: {', '.join(map(str, divisors))}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()