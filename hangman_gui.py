import tkinter as tk
from tkinter import messagebox
import random

# List of words
words = ["python", "alpha", "hangman", "code", "game"]

# Choose a random word
word = random.choice(words)
guessed = ["_"] * len(word)
chances = 6

# Function to check the letter
def guess_letter():
    global chances
    letter = entry.get().lower()
    entry.delete(0, tk.END)
    if letter in word:
        for i, char in enumerate(word):
            if char == letter:
                guessed[i] = letter
        word_label.config(text=" ".join(guessed))
    else:
        chances -= 1
        chances_label.config(text=f"Chances left: {chances}")
    if "_" not in guessed:
        messagebox.showinfo("Hangman", f"You Win! The word was: {word}")
        root.destroy()
    elif chances == 0:
        messagebox.showinfo("Hangman", f"You Lose! The word was: {word}")
        root.destroy()

# Tkinter GUI
root = tk.Tk()
root.title("Hangman Game")

word_label = tk.Label(root, text=" ".join(guessed), font=("Helvetica", 20))
word_label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

guess_button = tk.Button(root, text="Guess", command=guess_letter)
guess_button.pack(pady=10)

chances_label = tk.Label(root, text=f"Chances left: {chances}")
chances_label.pack(pady=10)

root.mainloop()