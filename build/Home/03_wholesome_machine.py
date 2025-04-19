def main():
    while True:
        word = input("Enter a word (type 'stop' to end): ")
        if word.lower() == "stop":
            break
        print(f"You are awesome for saying: {word}")

if __name__ == "__main__":
    main()
