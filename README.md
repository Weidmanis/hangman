# Hangman game

## A simple Hangman game that can be played in terminal

#There are two version hangman, and hangman_v2.
- First verison is a simpler script for the game that has been constructed using only if statements.
- Second version is written using fucntions for the smaller parts of the code.

#Words are randomly picked from list of words in words.py script.
  - Don't be surprised of how tough to guess those words are

#Couple of pointers for the players:
- Letters available are printed before each guess
- Letters that have been used in previous guesses are also shown so that the player does not reuse them
- Game can be played guessing the word letter-by-letter or the word can be entered once you feel confident that you know what it is


#Further work:
- Manage the error if the letter that has been used is used as a guess again.
- Make a pygames GUI for a more interactive gameplay
- Extend the list of words for the game
- Add a hint if the player is on the last try
