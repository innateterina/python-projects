import tkinter as tk
import random

# List of words to guess
words = ['apple', 'banana', 'cherry', 'date', 'grape']

# Choose a random word
word = random.choice(words)
guessed = ['_' for _ in word]  # List to keep track of guessed letters


def guess(letter):
    if letter in word:
        update_guessed(letter)
    update_display()


def update_guessed(letter):
    for index, char in enumerate(word):
        if char == letter:
            guessed[index] = letter


def update_display():
    label.config(text=' '.join(guessed))
    if '_' not in guessed:
        label.config(text='You win!')


# Create the main window
root = tk.Tk()
root.title("Hangman Game")

# Create a label to show the word to guess
label = tk.Label(root, text=' '.join(guessed), font=('Helvetica', 24))
label.pack(pady=20)

# Create a frame to hold the buttons
frame = tk.Frame(root)
frame.pack()

# Create buttons for each letter
for ascii_code in range(97, 123):  # ASCII codes for a-z
    letter = chr(ascii_code)
    btn = tk.Button(frame, text=letter.upper(),
                    command=lambda l=letter: guess(l))
    btn.pack(side='left')

# Run the application
root.mainloop()
