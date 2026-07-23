# Advanced Tic Tac Toe

A modern desktop implementation of the classic Tic Tac Toe game built entirely in **Python**. This project is designed as both a polished game and a learning experience, focusing on object-oriented programming, algorithms, modular software design, and GUI development using **Tkinter**.

The primary goal of this project is to strengthen Python fundamentals while creating a clean, well-structured application that demonstrates practical software engineering skills.

---

# Features

## Gameplay

* Classic 3×3 Tic Tac Toe
* Player vs Player mode
* Player vs Computer mode
* Three AI difficulty levels:

  * Easy
  * Medium
  * Impossible (Minimax Algorithm)
* Move validation
* Automatic win detection
* Draw detection
* Restart game
* Score tracking

---

## User Interface

* Modern desktop interface built with Tkinter
* Clean and responsive layout
* Dark and Light themes
* Animated game interactions
* Custom icons and game assets
* Sound effects
* Simple and intuitive navigation

---

## Statistics

* Total games played
* Wins
* Losses
* Draws
* Win percentage
* Statistics automatically saved between sessions

---

## Settings

* Theme selection
* Sound toggle
* AI difficulty selection
* Player names
* Settings saved automatically

---

# Technologies Used

* Python 3
* Tkinter
* JSON
* Object-Oriented Programming (OOP)

---

# Project Structure

```
Advanced-TicTacToe/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── assets/
│   ├── audio/
│   ├── fonts/
│   ├── icons/
│   ├── images/
│   └── logo/
│
├── data/
│   ├── settings.json
│   └── statistics.json
│
├── game/
│   ├── __init__.py
│   ├── app.py
│   ├── game.py
│   ├── board.py
│   ├── player.py
│   ├── ai.py
│   ├── minimax.py
│   ├── statistics.py
│   ├── settings.py
│   ├── file_manager.py
│   ├── constants.py
│   ├── validator.py
│   └── helpers.py
│
├── ui/
│   ├── __init__.py
│   ├── main_window.py
│   ├── game_board.py
│   ├── menu.py
│   ├── dialogs.py
│   ├── animations.py
│   └── themes.py
│
└── docs/
    ├── architecture.md
    └── screenshots/
```

---

# How to Run

## 1. Clone the repository

```bash
git clone https://github.com/yourusername/Advanced-TicTacToe.git
```

---

## 2. Move into the project directory

```bash
cd Advanced-TicTacToe
```

---

## 3. Install the required packages

```bash
pip install -r requirements.txt
```

---

## 4. Launch the application

```bash
python game/app.py
```

---

# AI Difficulty Levels

### Easy

The computer selects moves randomly from the available spaces, making it suitable for beginners.

### Medium

The computer uses simple strategies, such as blocking obvious wins and taking winning moves when available.

### Impossible

The AI uses the **Minimax Algorithm**, allowing it to play optimally and making it impossible to beat under standard Tic Tac Toe rules.

---

# Skills Demonstrated

This project showcases the following programming concepts:

* Object-Oriented Programming
* Classes and Objects
* Encapsulation
* Modular Programming
* Python Packages
* File Handling
* JSON Data Management
* Error Handling
* Algorithms
* Minimax Search
* Recursion
* GUI Development with Tkinter
* Software Architecture
* Git and GitHub Workflow

---

# Future Improvements

Potential features that can be added in future versions include:

* Custom board sizes
* Additional game modes
* Undo move
* Replay system
* Keyboard shortcuts
* Achievement system
* Improved animations
* Additional themes
* Better AI heuristics
* Localization and multiple language support

---

# Learning Goals

This project was created to improve practical Python development skills through building a complete desktop application from scratch.

Some of the main learning objectives include:

* Designing larger Python projects
* Organizing code into modules
* Practicing object-oriented design
* Implementing game algorithms
* Building graphical interfaces
* Working with persistent data
* Writing clean, maintainable code

---

# Screenshots

Screenshots of the application will be added to the `docs/screenshots/` folder as development progresses.

---

# License

This project is intended for educational and portfolio purposes.

Feel free to explore, learn from, or modify the code for your own personal use.

---

# Author

Developed as a personal Python learning project to strengthen programming fundamentals, software design, and problem-solving skills.
