import random

# Step 1: Computer chooses a random number
secret_number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Guess the Number Game!")
print("I'm thinking of a number between 1 and 100... Can you guess it?")

# Step 2: Loop until user guesses correctly
while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"🎉 Correct! The number was {secret_number}.")
        print(f"You guessed it in {attempts} attempts.")
        break
