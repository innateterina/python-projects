# players attempt to guess a randomly selected word within a limited number of tries.
import random
name = input("What is your name? ")
print(f"Good luck, {name}!")
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']
word = random.choice(words)
print("Guess the characters")
guesses = ''
turns = 12
while turns > 0:
    wrong_try = 0
    for i in word:
        if i in guesses:
            print(i, end=" ")
        else:
            print("_")
            wrong_try += 1
    if wrong_try == 0:
        print("You win")
        print("The word is:  ", word)
        break
    print()
    guess = input("guess a character:")
    guesses += guess
    if guess not in word:

        turns -= 1
        print("Wrong")
        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("You Loose")
