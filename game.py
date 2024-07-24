#implement error handling (can only use letters)
from string import ascii_letters
import random
import tkinter as tk

ASCII = str(ascii_letters)
MAX_NUMBER_OF_GUESSES = 5
GUESSES = {"incorrect": "🔴", "correct": "🟢", "partially": "🟡", "unknown": "?"}

class Game:
    """A simple wordle clone"""

    def __init__(self, window):
        """Random word selected, gues_list set to empty, set game word, set guesses to 0"""
        self.window = window
        self.window.title("Wordle")
        self.window.geometry("400x500")
        
        self.guesses = 0
        self.guess_list = []
        self.current_word = ""
        self.guess_pattern = []
        self.game_over = False
    
        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.window, text="Welcome to Wordle! Click start to begin...")
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.window, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.entry = tk.Entry(self.window, font=('Helvetica', 24))
        self.entry.pack(pady=10)

        self.message_label = tk.Label(self.window, text='', font=('Helvetica', 14))
        self.message_label.pack(pady=10)
    
    def start_game(self):
        self.reset()
        self.current_word = self.get_game_word()
        self.label.config(text='Guess the 5 letter word!')
    
    def guess(self):
        """Gets user input, validates it and returns word"""
        valid_guess = False
        while valid_guess == False:
            guess = input('\nGuess #{}: Enter a 5 letter word: '.format(self.guesses+1))
            guess = guess.lower()
            for letter in guess:
                if letter not in ASCII:
                    print("Invalid letter '{}'".format(letter))
            
            # can add validation to check through list of words for a 'valid' word
            if guess in self.guess_list:
                self.message_label.config(text="Word already guessed! Try again")
                # print("Word already guessed! Try again")
            elif len(guess) != 5:
                self.message_label.config(text="Please enter a 5 letter word!")
                # print("Please enter a 5 letter word!")
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

                self.entry.delete(0, tk.END)
                
                if not self.guesses < MAX_NUMBER_OF_GUESSES:
                    self.game_over = True

        if self.guesses < MAX_NUMBER_OF_GUESSES:
            
            # print('------------------------')
            # print('Correct!!!')
            won_message = f'Congratulations, you won in {self.guesses} '
            if self.guesses > 1:
                won_message += "guesses."
            else:
                won_message += "guess."
            self.message_label.config(text=won_message)
            # print(won_message)
        else:
            # print('------------------------')
            self.message_label.config(text=f'Better like next time, the correct word was {self.current_word.upper()}.')
            # print(f'Better like next time, the correct word was {self.current_word.upper()}.')

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
        for widget in self.guesses_frame.winfo_children():
            widget.destroy()

    def get_game_word(self):
        with open('wordbank.txt', 'r') as wordbank:
            word = random.choice(wordbank.read().split(','))
            return word.lower()
    
    def display_state(self):
        print('\nGuesses so far:')
        print('-----------------')
        for i in range(len(self.guess_list)):
            print(" " + ' '.join(self.guess_list[i].upper()))
            print(self.guess_pattern[i])

if __name__ == "__main__":
    game = Game()
    game.play()
    newGame = input('Do you want to play again? Y/N ')
    newGame.strip()
    while newGame != "":
        if newGame == "Y" or newGame == "y":
            game.play()
            newGame = input('Do you want to play again? Y/N ')
            newGame.strip()
        else:
            print('Thanks for playing, goodbye!')
            exit()

# TO DO: display_guess function, or ask gpt to make it in the same sdtyle as my current code
        # figure out how the play method works with this new version - tie into gameloop?