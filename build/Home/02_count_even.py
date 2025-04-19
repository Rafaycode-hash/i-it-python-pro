def count_even_numbers(start, end):
    even_count = 0
    for number in range(start, end + 1):
        if number % 2 == 0:
            even_count += 1
    return even_count

def main():
    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        
        if start > end:
            print("Start number should be less than or equal to end number.")
            return
        
        even_count = count_even_numbers(start, end)
        print(f"There are {even_count} even numbers between {start} and {end}.")
    
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
