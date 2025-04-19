def get_remainder(dividend, divisor):
    return dividend % divisor

def main():
    try:
        dividend = int(input("Enter the dividend: "))
        divisor = int(input("Enter the divisor: "))
        
        if divisor == 0:
            print("Division by zero is not allowed.")
        else:
            remainder = get_remainder(dividend, divisor)
            print(f"The remainder when {dividend} is divided by {divisor} is: {remainder}")
    
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
