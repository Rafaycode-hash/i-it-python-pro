def chaotic_count(start, end, step):
    print("Chaotic Counting Begins!")
    for number in range(start, end + 1, step):
        print(number)

def main():
    try:
        start = int(input("Enter the start number: "))
        end = int(input("Enter the end number: "))
        step = int(input("Enter the step (chaos factor): "))
        
        if step == 0:
            print("Step cannot be zero!")
            return
        
        chaotic_count(start, end, step)

    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
