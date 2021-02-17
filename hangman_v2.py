import string
from words import list_of_words
import random

def in_word(guess, word_to_guess, to_guess):
    if guess in word_to_guess:
        for indx, let in enumerate(word_to_guess):
            if let == guess:
                to_guess[indx] = guess
        return to_guess

def is_word(guess, word_to_guess):
    if guess == word_to_guess:
        return True

def hangman(players_name):

    tries = 7
    alphabet = string.ascii_uppercase
    word_to_guess = random.choice(list_of_words).upper() 
    to_guess = list('_' * len(word_to_guess))
    let_available = list(alphabet)
    let_used = []

    while tries != 0:

        print(f"You have {tries} tries left")
        print(f"\nThe word to guess is {to_guess}")
        print(f"Use these letters for your guess: {let_available}.")
        print(f"You have tried these letters so far: {let_used}.")
        player_guess = str(input("\nChoose a letter from above: ")).upper()

        if is_word(player_guess, word_to_guess):
            print(f"Congratulations you have guess the word!")
            print(f"Word to guess was: {word_to_guess}.")
            break

        elif player_guess in word_to_guess:
            to_guess = in_word(player_guess, word_to_guess, to_guess)
            print(f"\nYou were right '{player_guess}' is in the word.")
            #NEED TO CHECK IF THE WORD IS NOT COMPLETE AND CONGRATULATE THE PLAYER
        else:
            print(f"\nLetter '{player_guess}' is not in the word, try again.")
            tries -= 1

        let_available.remove(player_guess)
        let_used.append(player_guess)
        
 
players_name = input("\nPlease enter your name: ").title()
print(f"Shall we begin {players_name}?\n")

hangman(players_name)
