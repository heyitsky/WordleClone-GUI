#implement error handling (can only use letters)
from string import ascii_letters
import random

ASCII = str(ascii_letters)
MAX_NUMBER_OF_GUESSES = 5
GUESSES = {"incorrect": "🔴", "correct": "🟢", "partially": "🟠", "unknown": "?"}

class Game:
    """A simple wordle clone"""

    def __init__(self):
        """Random word selected, gues_list set to empty, set game word, set guesses to 0"""
        self.guesses = 0
        self.guess_list = []
        self.current_word = "test"
        self.guess_pattern = ["-----"]
        self.game_over = False
    
    def guess(self):
        """Gets user input and validates it"""
        guess = input('\nGuess #{}: Enter a 5 letter word: '.format(self.guesses))
        guess.toLower()
        letters = guess.split()
        for letter in letters:
            if letter not in ASCII:
                raise ValueError("Invalid letter '{}'".format(letter))
        
        if guess in self.guess_list:
            raise ValueError("Word already guessed! Try again")
        else:
            self.guess_list.append(guess)
            return guess

    def play(self):
        if not self.game_over:
            self.reset()
        self.current_word = self.get_game_word()
        print(self.current_word)
        self.start_message()

    def start_message(self):
        input("Ready to play a new game, press ENTER/RETURN to start..!")
    
    def reset(self):
        self.guesses = 0
        self.guess_list = []
        self.guess_pattern = ["-----"]
        self.game_over = False

    def get_game_word(self):
        with open('wordbank.txt', 'r') as wordbank:
            word = random.choice(wordbank.read().split(','))
            return word
    
    def display_state(self):
        print('Guesses:')
        print('------------')
        for i in len(self.guesses):
            print(' '.join(self.guess_list[i]))
            print(self.guess_pattern[i])

if __name__ == "__main__":
    game = Game()
    game.play()