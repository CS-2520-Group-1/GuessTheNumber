'''
Group Members: 
Hasti Abbasi Kenarsari
Sarah Huynh
Mayela Ancheta 
'''

import random

class GuessTheNumber:

    def __init__(self, min_val: int = 1, max_val: int = 100):
        # minimum value for the secret number
        self.min_val = min_val
        # maximum value for the secret number
        self.max_val = max_val
        # the secret number
        self.secret_num = None

    def reset_game(self) -> None:
        """Reset/start the game by generating a random number (secret)."""
        self.secret_num = random.randint(self.min_val, self.max_val)

    def check(self, guess: int) -> str:
        """Check the player's guess & provide feedback."""
        if guess < self.secret_num: 
            return "Higher!"
        elif guess > self.secret_num:
            return "Lower!"
        else:
            return "You guessed the number!"