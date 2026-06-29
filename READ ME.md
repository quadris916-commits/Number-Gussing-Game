Project overview:-

A beginner-friendly Number Guessing game written in Python that demonstrates use of random numbers, loops, conditionals, and basic file I/O. The player guesses a secret number within a range; the game gives feedback (too low / too high) until the correct number is found. Includes difficulty modes, guess counting, and best-score persistence.

Features:-

Choose difficulty (Easy/Medium/Hard) which changes range and allowed hints.

Validates user input and handles invalid entries gracefully.

Counts attempts and displays performance at the end.

Saves and loads best scores to a simple local file.

Modular code for easy extension (GUI, web, or multiplayer).

Getting started:-

Requirements: Python 3.8+ (no external libraries required).

Installation: clone the repo, open a terminal, then run: python main.py.

Configuration: edit settings in config.py to change ranges, max attempts, or enable/disable score saving.

Usage example:-

On launch, choose a difficulty, then enter numeric guesses when prompted. The game prints “Too low” or “Too high” until you guess correctly; it then shows attempts and whether you beat the best score.

Code layout:-

main.py — game entry and CLI loop.

game.py — core game logic (answer generation, guess handling, feedback).

scores.py — save/load best scores.

config.py — adjustable game settings.

tests/ — simple unit tests for input validation and guess logic.

assets/ — optional images or sound files for future GUI features.

