def is_odd(number):
    if number % 2 != 0:
        return True
    else:
        return False

def main():
    try:
        num = int(input("Enter a number: "))
        if is_odd(num):
            print(f"{num} is an odd number.")
        else:
            print(f"{num} is an even number.")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
