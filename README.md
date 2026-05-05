# Terminal Quiz Game

A fully functional, terminal-based quiz game built in Python.
Developed in week 2 of learning the language,  no frameworks,
no tutorials, just core Python logic.

---

## What It Does

- Presents 10 questions across geography, science, math,
  and general knowledge
- Optional bonus question at the end
- Tracks score in real time
- Displays final score as a percentage
- Accepts multiple valid answer formats per question
- Validates all inputs — handles empty and invalid entries
- Color-coded terminal output via colorama
- Ends with a 0–5 star rating prompt

---

## Tech Stack

- Python 3.x
- colorama — terminal color formatting

---

## Installation

```bash
git clone https://github.com/TanishBhatta/terminal-quiz-game
cd terminal-quiz-game
pip install colorama
```

## Run

```bash
python quiz_game.py
```

---

## What I Learned Building This

Dictionaries drive the entire question engine, each question
is a structured object with a prompt, options list, and a list
of accepted answers. Looping over a list of dictionaries to
generate dynamic program behavior is the same pattern used in
backend API responses.

Input validation via while True loops with conditional breaks
taught me how real software handles unpredictable user behavior.

colorama was my first external library, first real taste of
dependency management and pip.

---

## What Is Next

Refactoring into clean functions with separated concerns.
Next project: a file system CLI tool using os and shutil.

---

## Author

Tanish Bhatta
Building in public from Kathmandu, Nepal.
github.com/TanishBhatta
