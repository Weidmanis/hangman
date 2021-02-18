import string
from words import list_of_words
import random


print("\nI see you wanna play a game! Let's get on with it then!\n")
# Ask for players name
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

# Get the word from words.py, list_of_words
word_to_guess = random.choice(list_of_words).upper()
# A list at len of the word to be guessed
to_guess = list('_' * len(word_to_guess))
# Add alphabet letters to a list to show later
letters_available = list(alphabet)

print(f"\nTime for your first guess {name}!")
# Show the word that needs to be guessed as a lsit of lines
print(f'This is the word that you need to guess: {to_guess}!\n')
# Show the available letters for the guess
print(f"Choose one from the letter presented:\n {letters_available}")

# Set tries for the game
tries = 7

while tries!= 0:

    # Ask for users first guess
    user_guess = str(input("\nWhich letter would you like to try?: ")).upper()


    if user_guess == word_to_guess: # checks if the entered word is correct

        print(f"Congratulations, you have guessed the right word! ")
        print(f"The word to guess was: {word_to_guess}")
        break

    elif user_guess in word_to_guess: # check if a letter is in the word

        print(f"You were right, '{user_guess}' is in the word!\n")
        # find the index/es of the letter in the word
        for indx , letter in enumerate(word_to_guess):
            if letter == user_guess:
                to_guess[indx] = user_guess
        
        # check if the word has not been guessed
        if word_to_guess == "".join(to_guess):
            print(f"Congratulations, you have guessed the right word! ")
            print(f"The word to guess was: {word_to_guess}")
            break
               
    else: # exectues if the word or letter was wrong
        print(f"\nUnfortunately letter '{user_guess}' is not in the word")
        tries -= 1

    if tries == 0:
        print(f"\nUnfortunately you have lost {name}")
        print(f"The word to guess was: {word_to_guess}")


    letters_available.remove(user_guess) # removes the guessed letter from list
    letters_used.append(user_guess) # adds to the list of tried letters
    
    # Print stats for the game so far
    print(f"You have got {tries} attempts left")
    print(f"To guess: {to_guess}")
    print(f"\nThese are letter that you have available: {letters_available}")
    print(f"These are letters that you have already tried/used: {letters_used}")

    