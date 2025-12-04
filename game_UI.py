import tkinter as tk
from game_logic import GuessTheNumber


class GuessTheNumberUI:
    def __init__(self, root):

        self.root = root
        self.root.title("Guess the Number")

        # fixed window size
        self.root.geometry("700x500")

        # pastel theme
        self.bg_color = "#FFEAF4"      # very light pink
        self.card_color = "#FFFFFF"    # white
        self.text_color = "#5A4A57"    # warm mauve
        self.accent_color = "#F4A9C6"  # rosy pink
        self.success_color = "#C4E3D5" # mint

        self.root.configure(bg=self.bg_color)

        # import game logic
        self.game = GuessTheNumber()
        self.game.reset_game()
        self.attempts = 0

        # centered container as a white card
        self.container = tk.Frame(self.root, bg=self.card_color, padx=40, pady=30)
        self.container.pack(expand=True)

        # build UI
        self.create_widgets()
        self.root.bind("<Return>", lambda event: self.submit_guess())

    def create_widgets(self):

        self.title_label = tk.Label(
            self.container,
            text="Guess The Number!",
            font=("Helvetica", 28, "bold"),
            bg=self.card_color,
            fg=self.text_color
        )
        self.title_label.pack(pady=(10, 10))

        self.subtitle_label = tk.Label(
            self.container,
            text=f"Guess the number between {self.game.min_val} and {self.game.max_val}.",
            font=("Helvetica", 13),
            bg=self.card_color,
            fg="#555555"
        )
        self.subtitle_label.pack(pady=(0, 15))

        input_frame = tk.Frame(self.container, bg=self.card_color)
        input_frame.pack(pady=10)

        self.input_label = tk.Label(
            input_frame,
            text="Enter your guess:",
            font=("Helvetica", 14),
            bg=self.card_color,
            fg=self.text_color
        )
        self.input_label.grid(row=0, column=0, padx=(0, 8))

        # User input
        self.guess_entry = tk.Entry(
            input_frame,
            font=("Helvetica", 18),
            width=12,
            justify="center",
            bd=0,
            highlightthickness=3,
            highlightbackground="#F7C1D7",
            highlightcolor="#F4A9C6",
			bg="#FFFFFF",
			fg="#333333",
			insertbackground="#333333"
        )
        self.guess_entry.grid(row=0, column=1)
        self.guess_entry.focus()

        # Submit button
        self.submit_button = self.make_button(
            input_frame,
            text="Submit",
            command=self.submit_guess,
            bg=self.accent_color,
            fg="#000000"
        )
        self.submit_button.grid(row=0, column=2, padx=(8, 0))
        self.add_hover(self.submit_button, self.accent_color, "#F7C1D7")

        # higher / lower feedback
        self.feedback_label = tk.Label(
            self.container,
            text="Make a guess to start!",
            font=("Helvetica", 16, "bold"),
            bg=self.card_color,
            fg=self.accent_color
        )
        self.feedback_label.pack(pady=(20, 5))

        self.attempts_label = tk.Label(
            self.container,
            text="Attempts: 0",
            font=("Helvetica", 14),
            bg=self.card_color,
            fg=self.text_color
        )
        self.attempts_label.pack(pady=(0, 20))

        # reset game button
        self.new_game_button = self.make_button(
            self.container,
            text="New Game",
            command=self.new_game,
            bg=self.success_color,
            fg="#000000"
        )
        self.new_game_button.pack(pady=(0, 10))
        self.add_hover(self.new_game_button, self.success_color, "#C8E6C9")

    def make_button(self, parent, text, command, bg, fg="#000000", padx=14, pady=6):
        return tk.Button(
            parent,
            text=text,
            command=command,
            font=("Helvetica", 12, "bold"),
            bg=bg,
            fg=fg,
            activebackground=bg,
            activeforeground=fg,
            bd=0,                
            relief="flat",      
            padx=padx,
            pady=pady,
        )

    def add_hover(self, button, normal_bg, hover_bg):
        button.bind("<Enter>", lambda e: button.config(bg=hover_bg, activebackground=hover_bg))
        button.bind("<Leave>", lambda e: button.config(bg=normal_bg, activebackground=normal_bg))

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
            font=("Helvetica", 28, "bold"),
            bg=self.card_color,
            fg=self.accent_color
        )
        win_label.pack(pady=(40, 20))

        number_label = tk.Label(
            self.container,
            text=f"The number was {self.game.secret_num}.",
            font=("Helvetica", 18),
            bg=self.card_color,
            fg=self.text_color
        )
        number_label.pack(pady=(0, 10))

        attempts_label = tk.Label(
            self.container,
            text=f"You guessed it in {self.attempts} attempts.",
            font=("Helvetica", 16),
            bg=self.card_color,
            fg=self.text_color
        )
        attempts_label.pack(pady=(0, 30))

        # Play again 
        play_again_button = tk.Button(
            self.container,
            text="Play Again",
            font=("Helvetica", 14, "bold"),
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
