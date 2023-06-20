"""
Implement the classic game of Hangman, where players guess letters to reveal a hidden word. 
where you will use the words from a list. use strings to represent the hidden words, a list for player’s guess and another list to track incorrect guess.
choose a random word from the list. prompt user for a letter, check if it matches with the hidden word and the list accordingly.
Show the partially revealed word and the incorrect guesses. Set conditions to determine if the player wins or loses.
"""


import random

words = ['apple', 'banana', 'orange', 'mango']  # List of words

def select_word():
    return random.choice(words)

def play_hangman(word):
    guesses = []
    incorrect_guesses = []
    attempts = 6

    while attempts > 0:
        print("\\nAttempts left:", attempts)
        for letter in word:
            if letter in guesses:
                print(letter, end=' ')
            else:
                print('_', end=' ')
        print()

        guess = input("Enter a letter: ")

        if guess in guesses or guess in incorrect_guesses:
            print("You already guessed that letter!")
        elif guess in word:
            guesses.append(guess)
            if len(guesses) == len(set(word)):
                print("Congratulations! You won!")
                return
        else:
            incorrect_guesses.append(guess)
            attempts -= 1
            print("Incorrect guess!")

    print("Sorry, you lost! The word was:", word)

def main():
    word = select_word()
    play_hangman(word)

if __name__ == '__main__':
    main()
