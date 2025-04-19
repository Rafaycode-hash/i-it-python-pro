def main():
    print("Let's play Tiny Mad Libs! 😄\n")

    # Getting words from the user
    noun = input("Enter a noun: ")
    adjective = input("Enter an adjective: ")
    verb = input("Enter a verb: ")
    place = input("Enter a place: ")

    # Creating a tiny story using the inputs
    story = f"\nOne day, a {adjective} {noun} decided to {verb} all the way to {place}!"

    print("\nHere's your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    main()
