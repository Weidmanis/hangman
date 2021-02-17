import string
from words import list_of_words
import random


print("\nI see you wanna play a game! Let's get on with it then!\n")
name = str(input("What is your name?:  (it better not be Tony or Ezekiel) "))
name = name.title()

if name == 'Tony' or name == 'Ezekiel':
    print("\nOh, We've got a funny guy named {} overhere!".format(name))
else:
    print(f"\nNice to have you here {name}, let's begin the game.")


# Add Alphabet to available letters
alphabet = string.ascii_uppercase
# List for guessed letters
letters_used = []

# Get the word to guess
# word_to_guess = random.choice(list_of_words).upper()
word_to_guess = "ALPHABET"
to_guess = list('_' * len(word_to_guess))
letters_available = list(alphabet)

print(f"\nTime for your first guess {name}!")
print(f'This is the word that you need to guess: {to_guess}!\n')
print(f"Choose one from the letter presented:\n {letters_available}")

lives = 3
tries = 7

while tries!= 0 and lives != 0:

    user_guess = str(input("\nWhich letter would you like to try?: ")).upper()

    if user_guess == word_to_guess:
        print(f"Congratulations, you have guessed the right word! ")
        print(f"The word to guess was: {word_to_guess}")
        break

    elif user_guess in word_to_guess:
        print(f"You were right, '{user_guess}' is in the word!\n")
        for indx , letter in enumerate(word_to_guess):
            if letter == user_guess:
                to_guess[indx] = user_guess
        tries -= 1
               
    else:
        print(f"\nUnfortunately letter '{user_guess}' is not in the word")
        lives -= 1
        tries -= 1
        print(f"You have {lives} lives remaining")

    
    letters_available.remove(user_guess)
    letters_used.append(user_guess)
    

    print(f"You have got {tries} attempts and {lives} lives left")
    print(f"To guess: {to_guess}")
    print(f"\nThese are letter that you have available: {letters_available}")
    print(f"These are letters that you have already tried/used: {letters_used}")

print(f"\nUnfortunately you have lost {name}")
print(f"The word to guess was: {word_to_guess}")