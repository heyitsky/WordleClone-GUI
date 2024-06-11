#implement error handling (can only use letters)
from string import ascii_letters
import random
import pdb

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
        self.guess_pattern = []
        self.game_over = False
    
    def guess(self):
        """Gets user input and validates it"""
        valid_guess = False
        while valid_guess == False:
            guess = input('\nGuess #{}: Enter a 5 letter word: '.format(self.guesses+1))
            guess.lower()
            for letter in guess:
                if letter not in ASCII:
                    print("Invalid letter '{}'".format(letter))
            
            # can add validation to check through list of words for a 'valid' word
            if guess in self.guess_list:
                print("Word already guessed! Try again")
            elif len(guess) != 5:
                print("Please enter a 5 letter word!")
            else:
                valid_guess = True

        self.guess_list.append(guess)
        self.guesses += 1
        return guess

    def play(self):
        if self.game_over:
            self.reset()
        self.current_word = self.get_game_word()
        # print(self.current_word)                        #DEBUG
        self.start_message()

        while self.game_over != True:           
            word = self.guess()
            if word == self.current_word:
                self.game_over = True
            else:                
                self.guess_pattern.append(self.determine_word_pattern(word))
                self.display_state()
                if not self.guesses < MAX_NUMBER_OF_GUESSES:
                    self.game_over = True

        if self.guesses < MAX_NUMBER_OF_GUESSES:
            print('Correct!!!')
            print(f'Congratulations, you won in {len(self.guesses)} attempt/s.')
            
        else:
            print(f'Better like next time, the correct word was {self.current_word.upper()}.')

    def determine_word_pattern(self, word):
        temp_pattern = ""
        for index, char in enumerate(word):
            if char == self.current_word[index]:
                temp_pattern += GUESSES['correct']
            elif char in self.current_word:
                temp_pattern += GUESSES["partially"]
            else:
                temp_pattern += GUESSES['incorrect']
        return temp_pattern

    def start_message(self):
        text = input("Ready to play a new game, press ENTER/RETURN to start..!")
        while text != "":
            text = input("Ready to play a new game, press ENTER/RETURN to start..!")
    
    def reset(self):
        self.guesses = 0
        self.guess_list = []
        self.guess_pattern = []
        self.game_over = False

    def get_game_word(self):
        with open('wordbank.txt', 'r') as wordbank:
            word = random.choice(wordbank.read().split(','))
            return word.lower()
    
    def display_state(self):
        print('\nGuesses so far:')
        print('-----------------')
        for i in range(len(self.guess_list)):
            print(" " + ' '.join(self.guess_list[i]))
            print(self.guess_pattern[i])

if __name__ == "__main__":
    game = Game()
    game.play()
    newGame = input('Do you want to play again? Y/N ')
    newGame.strip()
    if newGame == "Y" or newGame == "y":
        game.play()
    else:
        print('Thanks for playing, goodbye!')
        exit()