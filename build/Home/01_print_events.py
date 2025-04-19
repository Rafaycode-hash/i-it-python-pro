def print_event(age):
    if age >= 18:
        print("You are eligible to vote!")
    else:
        print("You are too young to vote.")

def main():
    age = int(input("Enter your age: "))
    print_event(age)

if __name__ == "__main__":
    main()
