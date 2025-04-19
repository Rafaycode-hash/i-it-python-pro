# Step 1: Import random and define word list
import random

word_list = ["python", "hangman", "game", "program", "developer"]
secret_word = random.choice(word_list)
guessed_letters = []
chances = 6

print("🎯 Welcome to Hangman!")
print(f"The word has {len(secret_word)} letters.\n")

# Step 2: Game loop
while chances > 0:
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"
    
    print("Word:", display_word)
    
    if display_word == secret_word:
        print("🎉 Congratulations! You guessed the word correctly!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single valid letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        chances -= 1
        print(f"❌ Wrong guess! You have {chances} chances left.\n")
    else:
        print("✅ Good guess!\n")

# Step 3: Game Over
if chances == 0:
    print("😞 Game Over! The word was:", secret_word)
