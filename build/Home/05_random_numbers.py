import random

def check_random_number():
    number = random.randint(1, 100)
    print(f"The random number is: {number}")

    if number % 2 == 0:
        print(f"{number} is an even number.")
    else:
        print(f"{number} is an odd number.")

    if number > 50:
        print(f"{number} is greater than 50.")
    else:
        print(f"{number} is less than or equal to 50.")

def main():
    check_random_number()

if __name__ == "__main__":
    main()
