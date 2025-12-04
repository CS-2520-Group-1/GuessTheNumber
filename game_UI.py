import tkinter as tk
from game_logic import GuessTheNumber


class GuessTheNumberUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Guess the Number")

        # fixed window size
        self.root.geometry("700x500")

        self.bg_color = "#FFFFFF"
        self.text_color = "#000000"
        self.accent_color = "#A488BF"

        self.root.configure(bg=self.bg_color)

        # import game logic
        self.game = GuessTheNumber()
        self.game.reset_game()
        self.attempts = 0

        # centered container
        self.container = tk.Frame(self.root, bg=self.bg_color)
        self.container.pack(expand=True)

        # build UI
        self.create_widgets()
        self.root.bind("<Return>", lambda event: self.submit_guess())

    def create_widgets(self):

        self.title_label = tk.Label(
            self.container,
            text="Guess The Number!",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.title_label.pack(pady=(10, 10))

        self.subtitle_label = tk.Label(
            self.container,
            text=f"Guess the number between {self.game.min_val} and {self.game.max_val}.",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.subtitle_label.pack(pady=(0, 15))

        input_frame = tk.Frame(self.container, bg=self.bg_color)
        input_frame.pack(pady=10)

        self.input_label = tk.Label(
            input_frame,
            text="Enter your guess:",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.input_label.grid(row=0, column=0, padx=(0, 8))

        # User input
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Arial", 14),
            width=10,
            justify="center"
        )
        self.guess_entry.grid(row=0, column=1)
        self.guess_entry.focus()

        self.submit_button = tk.Button(
            input_frame,
            text="Submit",
            font=("Arial", 12, "bold"),
            command=self.submit_guess,
            bg=self.accent_color,
            fg="#000000",
            activebackground=self.accent_color,
            activeforeground="#000000",
            padx=10,
            pady=3
        )
        self.submit_button.grid(row=0, column=2, padx=(8, 0))

        # higher / lower feedback
        self.feedback_label = tk.Label(
            self.container,
            text="Make a guess to start!",
            font=("Arial", 16, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.feedback_label.pack(pady=(20, 5))

        self.attempts_label = tk.Label(
            self.container,
            text="Attempts: 0",
            font=("Arial", 14),
            bg=self.bg_color,
            fg=self.text_color
        )
        self.attempts_label.pack(pady=(0, 20))

        # reset game button
        self.new_game_button = tk.Button(
            self.container,
            text="New Game",
            font=("Arial", 12, "bold"),
            command=self.new_game,
            bg="#77B677",
            fg="#000000",
            activebackground="#84BF73",
            activeforeground="#000000",
            padx=12,
            pady=4
        )
        self.new_game_button.pack(pady=(0, 10))

    def submit_guess(self):
        # no action on no guess 
        if not hasattr(self, "guess_entry"):
            return

        guess_text = self.guess_entry.get().strip()

        # User input validation
        if not guess_text.isdigit():
            self.feedback_label.config(text="Please enter a valid whole number.")
            return

        guess = int(guess_text)

        # 1-100 validation
        if guess < self.game.min_val or guess > self.game.max_val:
            self.feedback_label.config(
                text=f"Please enter a number between {self.game.min_val} and {self.game.max_val}."
            )
            return

        self.attempts += 1
        result = self.game.check(guess)

        self.feedback_label.config(text=result)
        self.attempts_label.config(text=f"Attempts: {self.attempts}")

        # if guessed correctly, display win screen
        if result == "You guessed the number!":
            self.show_win_screen()
            return

        # Clear entry for next guess
        self.guess_entry.delete(0, tk.END)

    def show_win_screen(self):
        # reset screen
        for widget in self.container.winfo_children():
            widget.destroy()

        win_label = tk.Label(
            self.container,
            text="You got it!",
            font=("Arial", 28, "bold"),
            bg=self.bg_color,
            fg=self.text_color
        )
        win_label.pack(pady=(40, 20))


        number_label = tk.Label(
            self.container,
            text=f"The number was {self.game.secret_num}.",
            font=("Arial", 18),
            bg=self.bg_color,
            fg=self.text_color
        )
        number_label.pack(pady=(0, 10))
        attempts_label = tk.Label(
            self.container,
            text=f"You guessed it in {self.attempts} attempts.",
            font=("Arial", 16),
            bg=self.bg_color,
            fg=self.text_color
        )
        attempts_label.pack(pady=(0, 30))

        # Play again 
        play_again_button = tk.Button(
            self.container,
            text="Play Again",
            font=("Arial", 14, "bold"),
            command=self.new_game,
            bg=self.accent_color,
            fg="#000000",
            activebackground=self.accent_color,
            activeforeground="#000000",
            padx=16,
            pady=6
        )
        play_again_button.pack(pady=(0, 10))

    def disable_input(self):
        if hasattr(self, "guess_entry"):
            self.guess_entry.config(state="disabled")
        if hasattr(self, "submit_button"):
            self.submit_button.config(state="disabled")

    def enable_input(self):
        if hasattr(self, "guess_entry"):
            self.guess_entry.config(state="normal")
            self.guess_entry.focus()
        if hasattr(self, "submit_button"):
            self.submit_button.config(state="normal")

    def new_game(self):
        self.game.reset_game()
        self.attempts = 0

        # reset screen
        for widget in self.container.winfo_children():
            widget.destroy()

        # Back to main screen
        self.create_widgets()


if __name__ == "__main__":
    root = tk.Tk()
    app = GuessTheNumberUI(root)
    root.mainloop()
