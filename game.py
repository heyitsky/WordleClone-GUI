from string import ascii_letters
import random
import tkinter as tk

ASCII = str(ascii_letters)
MAX_NUMBER_OF_GUESSES = 5
GUESSES = {"incorrect": "🔴", "correct": "🟢", "partially": "🟡", "unknown": "?"}

class Game:
    """A simple wordle clone"""

    def __init__(self, master):
        """Initialise the game, set up the GUI"""
        self.master = master
        self.master.title("Wordle")
        self.master.geometry("400x500")

        self.guesses = 0
        self.guess_list = []
        self.current_word = ""
        self.guess_pattern = []
        self.game_over = False

        self.create_widgets()

    def create_widgets(self):
        """Create and place widgets in the window"""
        self.label = tk.Label(self.master, text="Welcome to Wordle! Click Start to begin...")
        self.label.pack(pady=10)

        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game)
        self.start_button.pack(pady=10)

        self.entry = tk.Entry(self.master, font=('Helvetica', 24))
        self.entry.pack(pady=10)

        self.submit_button = tk.Button(self.master, text="Submit Guess", command=self.submit_guess)
        self.submit_button.pack(pady=10)

        self.message_label = tk.Label(self.master, text='', font=('Helvetica', 14))
        self.message_label.pack(pady=10)

        self.guesses_frame = tk.Frame(self.master)
        self.guesses_frame.pack(pady=10)

    def start_game(self):
        self.reset()
        self.current_word = self.get_game_word()
        self.label.config(text="Guess the 5-letter word!")

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

    def submit_guess(self):
        guess = self.entry.get().lower()
        if not guess or len(guess) != 5 or any(char not in ASCII for char in guess):
            self.message_label.config(text="Please enter a valid 5-letter word.")
            return

        self.guess_list.append(guess)
        self.guesses += 1

        result = self.determine_word_pattern(guess)
        self.display_guess(guess, result)

        self.entry.delete(0, tk.END)

        if guess == self.current_word:
            self.game_over = True
            if self.guesses == 1:
                self.message_label.config(text=f"Congratulations! You guessed the word in {self.guesses} guess.")
            else:
                self.message_label.config(text=f"Congratulations! You guessed the word in {self.guesses} guesses.")
        elif self.guesses >= MAX_NUMBER_OF_GUESSES:
            self.game_over = True
            self.message_label.config(text=f"Game over! The word was {self.current_word.capitalize()}.")
        else:
            self.message_label.config(text="")

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

    def display_guess(self, guess, pattern):
        frame = tk.Frame(self.guesses_frame)
        frame.pack()
        guess_label = tk.Label(frame, text=' '.join(guess.upper()), font=('Helvetica', 18))
        guess_label.pack(side=tk.LEFT)
        pattern_label = tk.Label(frame, text=pattern, font=('Helvetica', 18))
        pattern_label.pack(side=tk.RIGHT)

if __name__ == "__main__":
    root = tk.Tk()
    game = Game(root)
    root.mainloop()
