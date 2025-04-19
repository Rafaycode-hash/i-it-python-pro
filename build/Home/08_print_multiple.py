def print_multiples(number, count):
    multiples = [number * i for i in range(1, count + 1)]
    return multiples

def main():
    try:
        num = int(input("Enter a number to find its multiples: "))
        count = int(input("How many multiples do you want to print? "))
        
        multiples = print_multiples(num, count)
        print(f"The first {count} multiples of {num} are: {', '.join(map(str, multiples))}")
    
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()