import random

NUM_ROUNDS = 5

def get_valid_input():
    guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").lower()
    return guess

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0

    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        user_num = random.randint(1, 100)
        comp_num = random.randint(1, 100)

        print(f"Your number is {user_num}")
        guess = get_valid_input()

        # Check game logic
        correct = False
        if guess == "higher" and user_num > comp_num:
            correct = True
        elif guess == "lower" and user_num < comp_num:
            correct = True

        if correct:
            print(f"You were right! The computer's number was {comp_num}")
            score += 1
        else:
            print(f"Aww, that's incorrect. The computer's number was {comp_num}")

        print(f"Your score is now {score}")
        print()  # Blank line for spacing

    # Conditional ending messages
    print("Thanks for playing!")
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    main()
