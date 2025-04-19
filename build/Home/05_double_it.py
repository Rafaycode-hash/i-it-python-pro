def main():
    number = int(input("Enter a number to start doubling: "))
    while number < 100:
        number *= 2
        print(f"Doubled: {number}")

    print("Done! Number has reached 100 or more.")

if __name__ == "__main__":
    main()
