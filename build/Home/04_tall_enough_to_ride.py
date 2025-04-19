def check_height(height):
    if height >= 140:
        print("You are tall enough to ride the rollercoaster!")
    else:
        print("Sorry, you are not tall enough to ride the rollercoaster.")

def main():
    height = int(input("Enter your height in cm: "))
    check_height(height)

if __name__ == "__main__":
    main()
