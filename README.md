# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.

It wrote the code, ran away, and now the game is unplayable.

* You can't win.
* The hints lie to you.
* The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" section in the app to see the secret number and test the game.

2. **Find the State Bug.** Investigate how Streamlit session state affects the secret number, attempts, score, and guess history.

3. **Fix the Logic.** Repair the incorrect higher/lower hints and scoring behavior.

4. **Refactor & Test.**

   * Move core game logic into `logic_utils.py`.
   * Run `pytest` in the terminal.
   * Keep testing until all tests pass.

## 📝 Document Your Experience

### Game Purpose

The purpose of the game is to guess a randomly generated secret number. The game tells the player whether the guess is too high or too low while tracking attempts, score, and guess history.

### Bugs Found

* The attempt counter started at 1 instead of 0.
* The higher/lower hints were reversed.
* Incorrect guesses could sometimes increase the score.
* The secret number was converted between an integer and a string, causing incorrect comparisons.
* The attempt counter and guess history appeared one interaction behind in the Developer Debug Info.

### Fixes Applied

* Changed the attempt counter so a new game starts at 0 attempts.
* Corrected the higher/lower hint logic.
* Refactored `check_guess` and `update_score` into `logic_utils.py`.
* Changed incorrect guesses so they subtract 5 points.
* Kept the secret number as an integer during comparisons.
* Moved the Developer Debug Info so the current attempts, score, and history display immediately after a guess.
* Added automated pytest tests to verify the game logic and scoring.

## 📸 Demo Walkthrough

1. The user starts a new game and the attempt counter begins at 0.
2. The secret number is 56 and the user guesses 70.
3. The game correctly reports that the guess is too high and tells the user to go lower. The score decreases by 5 and the attempt counter becomes 1.
4. The user guesses 40 and the game correctly tells the user to go higher. The guess immediately appears in the history.
5. The user enters 56 and the game recognizes the correct answer, displays the win message, and updates the score.

**Screenshot** *(optional)*: A screenshot of the completed winning game can be added here.

## 🧪 Test Results

```text
======================================== test session starts ========================================
platform linux -- Python 3.10.12, pytest-9.1.1, pluggy-1.6.0
collected 136 items

tests/test_game_logic.py ...                                                                  [  2%]
tests/test_scoring.py ....................................................................... [ 54%]
..............................................................                                [100%]

======================================== 136 passed in 0.61s ========================================
```

## 🚀 Stretch Features

* [ ] Enhanced UI or additional stretch features were not completed.

