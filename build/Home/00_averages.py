def calculate_average(numbers):
    if len(numbers) == 0:
        return 0
    return sum(numbers) / len(numbers)

def main():
    try:
        user_input = input("Enter numbers separated by commas: ")
        number_list = [float(num.strip()) for num in user_input.split(",")]
        avg = calculate_average(number_list)
        print(f"The average is: {avg}")
    except ValueError:
        print("Please enter valid numbers separated by commas.")

if __name__ == "__main__":
    main()
