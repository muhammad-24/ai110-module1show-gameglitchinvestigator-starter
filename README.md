# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] **What the game does:** It's a number guessing game. You try to guess a secret number 
  between 1 and 100, and the game tells you if you should go higher or lower. It also keeps a score.
- [x] **Bugs I found:** The hints were backwards — it told me to go lower when I should've gone 
  higher. Hard mode was actually easier than Normal (a smaller range). And on some guesses, 
  getting it wrong somehow gave me points instead of taking them away.
- [x] **What I fixed:** I moved all the game logic into logic_utils.py and cleaned it up. I made 
  the hints point the right way, made wrong guesses always lose points, and made Hard mode 
  actually harder. I also fixed the "New Game" button so it properly starts everything over.

## 📸 Demo Walkthrough

1. Pick a difficulty from the sidebar — Easy, Normal, or Hard.
2. Type a number into the guess box and hit "Submit Guess."
3. If you guessed too high, it tells you to go lower.
4. If you guessed too low, it tells you to go higher.
5. Your score drops a little on wrong guesses and only goes up when you win.
6. Guess the right number and you get a win message with your final score.
7. Hit "New Game" anytime to start fresh with a new secret number.

## 🧪 Test Results

```
============================= test session starts =============================
platform win32 -- Python 3.13.14, pytest-9.1.1, pluggy-1.6.0
rootdir: C:\Users\musam\Downloads\pyyy\ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.14.0
collected 6 items

tests\test_game_logic.py ......                                          [100%]

============================== 6 passed in 0.08s ==============================
