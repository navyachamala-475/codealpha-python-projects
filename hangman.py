import random

# List of words to guess
words = ["python", "code", "alpha", "task", "hangman"]

# Randomly pick one word
word = random.choice(words)

# Store guessed letters
guesses = ""

# Number of chances
turns = 6

print("🎮 Welcome to Hangman Game!")

# Main game loop
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end=" ")
            failed += 1
    print()

    # If no letters are missing, player wins
    if failed == 0:
        print("🎉 You Win! The word was:", word)
        break

    # Ask player for a guess
    guess = input("Guess a letter: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("❌ Wrong guess. You have", turns, "chances left.")

        if turns == 0:
            print("😢 You Lose. The word was:", word)