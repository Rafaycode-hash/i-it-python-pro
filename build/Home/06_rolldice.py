import random

def roll_dice():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    return dice1, dice2, total

def main():
    input("🎲 Press Enter to roll the dice...")
    d1, d2, total = roll_dice()
    print(f"You rolled a {d1} and a {d2}. Total: {total}")

if __name__ == "__main__":
    main()
