# 04_multiple_returns.py

import math

def calculate_values(number):
    square = number ** 2
    cube = number ** 3
    square_root = math.sqrt(number)
    return square, cube, square_root

def main():
    try:
        num = float(input("Enter a number: "))
        sq, cu, sqrt = calculate_values(num)
        print(f"Square: {sq}")
        print(f"Cube: {cu}")
        print(f"Square Root: {sqrt:.2f}")
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
