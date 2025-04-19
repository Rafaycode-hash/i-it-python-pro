import math

def calculate_hypotenuse(a, b):
    return math.sqrt(a ** 2 + b ** 2)

def main():
    try:
        a = float(input("Enter side a: "))
        b = float(input("Enter side b: "))
        c = calculate_hypotenuse(a, b)
        print(f"The hypotenuse (c) is: {c:.2f}")
    except ValueError:
        print("Please enter valid numbers.")

if __name__ == "__main__":
    main()
