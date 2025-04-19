import random

# Step 1: Define options
options = ["rock", "paper", "scissors"]

# Step 2: Initialize scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock, Paper, Scissors Game!")
print("Type 'exit' to quit the game.\n")

# Step 3: Game Loop
while True:
    user_choice = input("Choose rock, paper, or scissors: ").lower()
    
    if user_choice == "exit":
        break
    if user_choice not in options:
        print("❌ Invalid choice. Try again.\n")
        continue

    computer_choice = random.choice(options)
    print(f"🤖 Computer chose: {computer_choice}")

    # Step 4: Compare choices
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        print("✅ You win this round!\n")
        user_score += 1
    else:
        print("❌ Computer wins this round!\n")
        computer_score += 1

# Step 5: Final Scores
print("🏁 Game Over!")
print(f"Your score: {user_score}")
print(f"Computer score: {computer_score}")

if user_score > computer_score:
    print("🎉 You won the game!")
elif user_score < computer_score:
    print("😞 Computer won the game!")
else:
    print("🤝 It's a draw!")
