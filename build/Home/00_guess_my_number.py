import random

def main():
    number_to_guess = random.randint(1, 10)
    guess = None

    while guess != number_to_guess:
        guess = int(input("Guess a number between 1 and 10: "))
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print("You guessed it!")

if __name__ == "__main__":
    main()
