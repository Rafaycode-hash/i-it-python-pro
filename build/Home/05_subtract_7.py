# 05_subtract_7.py

def subtract_seven(number):
    return number - 7

def main():
    try:
        num = float(input("Enter a number: "))
        result = subtract_seven(num)
        print(f"{num} minus 7 is: {result}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
