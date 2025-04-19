def main():
    n = int(input("How many Fibonacci numbers do you want? "))
    a, b = 0, 1
    count = 0

    while count < n:
        print(a, end=" ")
        a, b = b, a + b
        count += 1

if __name__ == "__main__":
    main()
