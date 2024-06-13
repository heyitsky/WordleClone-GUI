# A Simple Wordle Clone
This project is a simple wordle clone, implmemented in python, currently run in the command line.

Wordle - A random 5 letter word will be selected each game, the user will have 5 chances to correctly guess the word. If the user guesses a word that is not correct, the game will check each individual letter. A guess pattern will be displayed, outlining the status of each letter. If the letter is in the correct location of the selected word a 🟢 will appear in that part of the guess pattern. If the letter is not in the correct location of the selected word, but that letter appears somewhere in the word a 🟠 will appear in that position. If the letter is not in the word at all, a 🔴 will appear in that place in the guess pattern. 

## Installation:
1. Download either the project folder OR **game.py** & **wordbank.txt**
2. Run *game.py* and the program will start (make sure *wordbank.txt* is in the same directory).

## Features:
- The game will ensure only a 5 letter word is guessed (it will re-prompt the user to guess if not)
- The game will check if you have already guessed a word (it will re-prompt the user to guess again if the same word is used)

## Customisation:
The wordbank can be changed as you want; removing words, adding words etc. however the following rules must be followed in order for the program to read and select a word correctly.
- Words **must** be 5 letters long
- Words need to be separated by a **comma** (i.e. test1,test2,test3...)

