# Guess The Number

A simple number-guessing game built with **Python** and **Tkinter**.  
The game generates a random number and gives the player feedback until they guess correctly.  
It demonstrates clean separation between game logic and UI code.

---
## Authors

- Hasti Abbasi Kenarsari
- Mayela Ancheta
- Sarah Huynh
  
---

## Purpose

- Practice Python fundamentals  
- Learn how to build a graphical interface using **Tkinter**  
- Demonstrate clean project structure using:
  - `game_logic.py` for the core game rules  
  - `game_UI.py` for the application interface  

---

## How to Run

Make sure Python 3 is installed, then run:

```bash
python3 game_UI.py
```

## How to Play

Enter a number in the input box.

The game will tell you if your guess is:

- Higher!
- Lower!
- You got it! (Correct)

Keep guessing until you find the secret number.

Click **New Game** or **Play Again** to restart.

---

## Project Structure
```
├── game_logic.py     # Handles number generation and guess checking
├── game_UI.py        # Tkinter interface (run this file)
└── README.md         # Project documentation
```


