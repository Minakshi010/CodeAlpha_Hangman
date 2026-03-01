import tkinter as tk
import random

# Predefined word list
words = ["python", "java", "apple", "tiger", "ocean"]
secret_word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_wrong = 6

# Function to update word display
def update_display():
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_label.config(text=display_word)

# Function to handle guess
def guess_letter():
    global wrong_guesses
    
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        message_label.config(text="Enter a single letter!", fg="#ffcc00")
        return

    if letter in guessed_letters:
        message_label.config(text="Already guessed!", fg="#ffcc00")
        return

    guessed_letters.append(letter)

    if letter in secret_word:
        message_label.config(text="Correct Guess! ✅", fg="#00ff99")
    else:
        wrong_guesses += 1
        message_label.config(text=f"Wrong Guess! ❌ ({wrong_guesses}/6)", fg="#ff4d4d")

    update_display()

    if wrong_guesses == max_wrong:
        message_label.config(text=f"You Lost! Word was '{secret_word}'", fg="red")
        guess_button.config(state="disabled")

    if all(letter in guessed_letters for letter in secret_word):
        message_label.config(text="You Won! 🎉", fg="#00ff99")
        guess_button.config(state="disabled")

# Function to restart game
def restart_game():
    global secret_word, guessed_letters, wrong_guesses
    secret_word = random.choice(words)
    guessed_letters = []
    wrong_guesses = 0
    guess_button.config(state="normal")
    message_label.config(text="")
    update_display()

# GUI Window
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x400")
root.config(bg="#1e1e2f")

# Title
title_label = tk.Label(root, text="🎮 Hangman Game", 
                       font=("Arial", 20, "bold"), 
                       bg="#1e1e2f", fg="#ffffff")
title_label.pack(pady=15)

# Word Display
word_label = tk.Label(root, text="", 
                      font=("Consolas", 22, "bold"), 
                      bg="#1e1e2f", fg="#00ffff")
word_label.pack(pady=20)

# Entry Box
entry = tk.Entry(root, font=("Arial", 16), 
                 justify="center", bg="#2b2b3c", fg="white")
entry.pack(pady=10)

# Guess Button
guess_button = tk.Button(root, text="Guess", 
                         font=("Arial", 14, "bold"),
                         bg="#4CAF50", fg="white",
                         activebackground="#45a049",
                         command=guess_letter)
guess_button.pack(pady=10)

# Restart Button
restart_button = tk.Button(root, text="Restart", 
                           font=("Arial", 12, "bold"),
                           bg="#2196F3", fg="white",
                           activebackground="#1e88e5",
                           command=restart_game)
restart_button.pack(pady=5)

# Message Label
message_label = tk.Label(root, text="", 
                         font=("Arial", 12),
                         bg="#1e1e2f")
message_label.pack(pady=15)

update_display()

root.mainloop()