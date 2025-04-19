# Step 1: Initial range
low = 1
high = 100
attempts = 0

print("🤖 Think of a number between 1 and 100 (don't tell me!)")
print("I'll try to guess it. You just tell me if it's too high, too low, or correct.")

while True:
    guess = (low + high) // 2
    attempts += 1
    print(f"My guess is: {guess}")
    feedback = input("Enter feedback (high/low/correct): ").lower()

    if feedback == "low":
        low = guess + 1
    elif feedback == "high":
        high = guess - 1
    elif feedback == "correct":
        print(f"🎉 Yay! I guessed your number in {attempts} attempts.")
        break
    else:
        print("Please enter only: high, low, or correct.")
