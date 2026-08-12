# Advanced Tic Tac Toe – Architecture Documentation

---

# 1. Project Overview

## Introduction

Advanced Tic Tac Toe is a desktop application developed in **Python** using the **Tkinter** GUI framework. While Tic Tac Toe is traditionally a simple game, this project expands it into a fully structured software application by incorporating Artificial Intelligence, persistent data storage, modular architecture, object-oriented programming principles, and a clean graphical user interface

The project was designed with the primary goal of demonstrating good software engineering practices rather than simply implementing the rules of Tic Tac Toe. Every major responsibility has been separated into its own module, making the application easier to understand, maintain, test, and extend 

Unlike small classroom projects that place all logic into a single file, this application follows a modular architecture where each component has a clearly defined responsibility. The game logic, artificial intelligence, graphical interface, data management, helper utilities, validation, and documentation are all separated into dedicated modules 

---

## Project Goals

The objectives of this project are:

- Develop a complete desktop application using Python
- Demonstrate Object-Oriented Programming (OOP) principles
- Separate frontend and backend responsibilities
- Implement an AI opponent using the Minimax algorithm
- Store settings and statistics using JSON files
- Create reusable utility modules
- Produce clean, readable, and maintainable code
- Include documentation and testing similar to a real software project

---

## Technologies Used

| Technology | Purpose |
|------------|---------|
| Python 3 | Primary programming language |
| Tkinter | Graphical User Interface (GUI) |
| JSON | Persistent storage for settings and statistics |
| Minimax Algorithm | Artificial Intelligence opponent |
| pathlib | Cross-platform file handling |
| unittest | Automated testing framework |
| Git & GitHub | Version control and project hosting |

---

## Software Design Philosophy

Several software engineering principles were followed throughout the project:

### Modularity

Every file performs one primary responsibility.

Examples include:

- Game logic
- Artificial intelligence
- Board management
- Settings management
- Statistics management
- User interface
- File operations

Keeping responsibilities separate improves readability and simplifies future modifications.

---

### Separation of Concerns

The graphical interface never performs game calculations directly.

Instead, the UI communicates with backend classes, which perform all computations before returning results to the interface.

This separation allows each component to be modified independently without affecting the rest of the project.

---

### Reusability

Utility functions and reusable components are placed into dedicated modules whenever possible.

Examples include:

- helper functions
- validation methods
- file management
- animation helpers

This minimizes duplicated code throughout the project.

---

### Maintainability

The project was intentionally divided into small, understandable files instead of one extremely large program.

This makes debugging significantly easier while also allowing future features to be added without major restructuring.

---

# 2. Overall System Architecture

The application follows a layered architecture where the user interacts only with the graphical interface. The interface communicates with the backend game engine, which is responsible for processing game logic, managing data, and updating the application state.

```
                User
                  │
                  ▼
        ┌──────────────────┐
        │   Main Window    │
        │   (Tkinter GUI)  │
        └────────┬─────────┘
                 │
        ┌────────┴─────────┐
        ▼                  ▼
  Game Board          Dialog Windows
        │
        ▼
   Game Controller
        │
 ┌──────┼───────────────┐
 ▼      ▼               ▼
Board  AI Player   Settings Manager
 │       │
 │       ▼
 │   Minimax Algorithm
 │
 ▼
Statistics Manager
 │
 ▼
JSON Files
```

---

## High-Level Workflow

The application's execution can be summarized as follows:

1. The user launches the application.
2. `main.py` creates the main application window.
3. The graphical interface initializes all backend components.
4. The player selects a cell on the board.
5. The move is validated.
6. The board state is updated.
7. Win or draw conditions are checked.
8. If AI mode is enabled, the AI calculates its move using Minimax.
9. The interface refreshes automatically.
10. Statistics are updated and saved when a game finishes.

---

## Architectural Layers

### Presentation Layer

Responsible for displaying information to the player.

Contains:

- Main window
- Game board
- Dialog boxes
- Animations

---

### Business Logic Layer

Responsible for implementing the rules of Tic Tac Toe.

Contains:

- Game controller
- Board
- Player
- AI
- Minimax

---

### Data Layer

Responsible for loading and saving persistent information.

Contains:

- Settings manager
- Statistics manager
- File manager
- JSON files

---

# 3. Project Directory Structure

The project is organized into multiple directories, each with a specific purpose.

```
Advanced-TicTacToe/
│
├── assets/
├── data/
├── docs/
├── game/
├── tests/
├── ui/
│
├── README.md
├── requirements.txt
├── .gitignore
└── main.py
```

---

## assets/

Stores all non-code resources used by the application.

Examples include:

- icons
- images
- fonts
- audio files

Although not all asset folders are currently populated, they have been included to make future expansion easier.

---

## data/

Stores persistent application data.

Current files include:

- `settings.json`
- `statistics.json`

This allows user preferences and game statistics to persist between application sessions.

---

## docs/

Contains project documentation.

Examples:

- architecture documentation
- screenshots
- additional reference material

This directory is intended for developers rather than end users.

---

## game/

Contains the complete backend implementation.

This directory is responsible for:

- game rules
- board logic
- AI
- minimax search
- settings
- statistics
- validation
- helper functions
- file management

No graphical code exists inside this folder.

---

## ui/

Contains every graphical component.

Responsibilities include:

- drawing the interface
- displaying the board
- dialogs
- animations
- user interaction

The UI never performs game calculations directly.

---

## tests/

Contains automated unit tests for the project.

Each backend module has a corresponding test file to verify its correctness independently.

Testing ensures that future modifications do not unintentionally break existing functionality.

---

## Root Files

### main.py

Acts as the application's entry point.

It creates the main window and starts the Tkinter event loop.

---

### README.md

Provides installation instructions, project overview, and usage information.

---

### requirements.txt

Lists the project's Python dependencies.

---

### .gitignore

Specifies files and directories that should not be tracked by Git.

---

# 4. Backend Architecture

The backend contains all computational logic required by the application.

Its primary responsibility is to process moves, enforce game rules, calculate AI decisions, manage persistent data, and provide information to the graphical interface.

The backend has been intentionally designed without any dependency on Tkinter, allowing the game logic to remain independent from the graphical interface.

---

## Game Controller (`game.py`)

The `Game` class acts as the central controller of the application.

Rather than storing the board directly inside the interface, all gameplay passes through this class.

Its responsibilities include:

- controlling turns
- validating moves
- switching players
- determining winners
- checking for draws
- resetting games
- communicating with the AI

The `Game` class serves as the bridge between the frontend and all backend modules.

---

## Board (`board.py`)

The `Board` class stores the complete state of the Tic Tac Toe board.

It is responsible for:

- storing cell values
- placing moves
- checking valid positions
- detecting winning combinations
- detecting draws
- resetting the board

Since all board operations occur here, other modules never modify the board directly.

---

## Player (`player.py`)

The `Player` class represents a game participant.

Each player stores information such as:

- player symbol
- player type
- player name

Separating players into their own class allows the project to support both human players and AI players without changing the game engine.

---

## AI Player (`ai.py`)

The `AIPlayer` class manages all computer-controlled gameplay.

Rather than embedding AI logic into the Game class, the AI is isolated into its own module.

Responsibilities include:

- selecting moves
- managing difficulty levels
- generating random moves
- requesting Minimax calculations
- returning the chosen move

Different difficulty levels are implemented by changing the strategy used for move selection.

---

## Minimax (`minimax.py`)

The Minimax module contains the decision-making algorithm used by the AI.

Its purpose is to search every possible game state recursively before selecting the optimal move.

Responsibilities include:

- recursively evaluating future board states
- assigning scores
- maximizing AI outcomes
- minimizing opponent outcomes
- selecting the best available move

The algorithm guarantees optimal play when the highest difficulty level is selected.

---

## Settings Manager (`settings.py`)

The `SettingsManager` handles all configurable application settings.

Examples include:

- AI enabled
- AI difficulty
- theme selection
- animation preferences
- sound settings

Settings are automatically loaded when the application starts and saved whenever changes occur.

---

## Statistics Manager (`statistics.py`)

The `StatisticsManager` records long-term game information.

Stored statistics include:

- games played
- Player X wins
- Player O wins
- AI wins
- draws

These statistics persist between application sessions using JSON files.

---

## File Manager (`file_manager.py`)

Provides reusable methods for reading and writing JSON files.

Centralizing file operations prevents duplicate code while improving consistency throughout the project.

---

## Helper Utilities (`helpers.py`)

Contains reusable utility functions shared across multiple modules.

Examples include:

- formatting functions
- board helper methods
- reusable calculations

Keeping these utilities separate improves code reuse and readability.

---

## Validator (`validator.py`)

Responsible for validating user input and game-related data.

Examples include:

- board positions
- player symbols
- difficulty levels
- configuration values

Centralizing validation helps prevent invalid data from propagating throughout the application.

---

## Constants (`constants.py`)

Stores global constants used across the project.

Examples include:

- board size
- player symbols
- default file locations
- default settings
- application-wide values

Using constants avoids repeated literal values throughout the codebase and makes future modifications significantly easier 

---

# 5. Frontend Architecture

The frontend is responsible for presenting information to the user and collecting user input. Unlike the backend, which contains all of the game's logic, the frontend focuses entirely on displaying information and responding to user interactions.

The interface has been designed so that it never directly modifies the game state. Instead, it communicates with backend classes that perform the required operations before returning updated information to the interface.

Separating the frontend from the backend improves maintainability, simplifies debugging, and allows the user interface to evolve independently of the game's internal logic.

---

## Main Window (`main_window.py`)

The `MainWindow` class is the central controller of the graphical interface.

Its responsibilities include:

- creating the application window
- initializing all graphical components
- creating backend objects
- responding to user interactions
- updating the scoreboard
- displaying status messages
- coordinating communication between the interface and the game engine

Every user action begins inside the main window before being forwarded to the appropriate backend component.

---

## Game Board (`game_board.py`)

The `GameBoard` class is responsible for displaying the Tic Tac Toe board.

Its primary responsibilities include:

- creating the 3×3 grid of buttons
- updating symbols after each move
- enabling and disabling the board
- clearing the board
- highlighting winning combinations
- forwarding user clicks to the main window

The board itself does not determine whether a move is valid. Instead, it simply displays the current game state received from the backend.

---

## Dialog Manager (`dialogs.py`)

The `DialogManager` centralizes all popup windows displayed by the application.

Examples include:

- About dialog
- Statistics dialog
- Confirmation dialogs
- Information messages
- Error messages

Keeping dialog windows in a dedicated module prevents unnecessary clutter inside the main window.

---

## Animation Manager (`animations.py`)

The `AnimationManager` provides lightweight visual effects for the interface.

Current animations include:

- button hover effects
- button press feedback
- winning-cell flashing
- delayed callback execution

These animations improve the user experience while remaining simple enough for a Tkinter desktop application.

---

## Theme Module (`theme.py`)

The theme module stores every visual constant used throughout the graphical interface.

Examples include:

- colors
- fonts
- spacing
- window dimensions
- button sizes
- status messages

By centralizing these values, the appearance of the application can be modified without changing multiple files.

---

## Frontend Communication

The frontend communicates with the backend using the following workflow:

```
User Click
      │
      ▼
GameBoard
      │
      ▼
MainWindow
      │
      ▼
Game Controller
      │
      ▼
Board / AI / Statistics
      │
      ▼
MainWindow
      │
      ▼
Refresh Interface
```

This design ensures that the graphical interface remains independent from the game's computational logic.

---

# 6. Data Management

The application stores persistent information using JSON files.

JSON was selected because it is lightweight, human-readable, built directly into Python, and more than sufficient for a project of this scale.

Using JSON also removes the need for an external database system.

---

## Settings Data

The application stores user preferences inside `settings.json`.

Examples include:

- AI enabled
- AI difficulty
- selected theme
- sound settings
- animation settings

Whenever a setting changes, the file is automatically updated so that the same preferences are restored during the next launch.

---

## Statistics Data

Game statistics are stored inside `statistics.json`.

The application records:

- total games played
- Player X victories
- Player O victories
- AI victories
- draws

Statistics are automatically updated whenever a game finishes.

---

## File Management

All file operations are handled by the `FileManager`.

Instead of allowing each module to open and save files independently, every JSON operation passes through this manager.

This approach provides several advantages:

- reduces duplicate code
- centralizes file handling
- improves maintainability
- simplifies future changes

---

## Why JSON Instead of a Database?

Although databases such as SQLite would work for storing settings and statistics, they would introduce unnecessary complexity.

The project only stores a small amount of structured information, making JSON a more appropriate choice.

Benefits include:

- simple implementation
- easy debugging
- readable file format
- no external dependencies

---

# 7. Game Flow

The following sequence describes a typical game from beginning to end.

---

## Application Startup

1. The user launches the application.
2. `main.py` creates the main window.
3. The graphical interface initializes backend components.
4. Settings and statistics are loaded.
5. The board is displayed.

---

## Player Move

When the player clicks a square:

1. The click is forwarded to the `MainWindow`.
2. The `Game` object validates the move.
3. The board is updated.
4. The interface refreshes.
5. The application checks for a winner or draw.

---

## AI Turn

If AI mode is enabled:

1. The AI receives the current board.
2. The selected difficulty determines the move strategy.
3. On Impossible difficulty, Minimax evaluates every possible move.
4. The AI selects the best move.
5. The board updates automatically.

---

## End of Game

Once a winner or draw is detected:

- the board becomes disabled
- winning cells are highlighted
- statistics are updated
- the status message changes
- the player may begin a new game

---

## Overall Execution Flow

```
Application Starts
        │
        ▼
Main Window
        │
        ▼
Player Click
        │
        ▼
Validate Move
        │
        ▼
Update Board
        │
        ▼
Winner?
   ┌────┴─────┐
   │          │
  No         Yes
   │          │
   ▼          ▼
AI Move   Save Statistics
   │          │
   └────┬─────┘
        ▼
Refresh Interface
```

This workflow repeats until the player exits the application.

---

# 8. Design Decisions

Several design decisions were made during development to improve code quality, readability, and maintainability.

---

## Why Object-Oriented Programming?

Object-Oriented Programming allows related data and functionality to be grouped together.

Each major concept in the project is represented as its own class.

Examples include:

- Game
- Board
- Player
- AIPlayer
- SettingsManager
- StatisticsManager
- FileManager

This organization makes the project easier to understand and extend.

---

## Why Separate the Backend and Frontend?

Mixing graphical code with game logic often results in difficult-to-maintain software.

Separating these responsibilities provides several advantages:

- easier debugging
- improved readability
- independent testing
- simpler future expansion

The user interface displays information, while the backend performs all calculations.

---

## Why Minimax?

Minimax guarantees optimal Tic Tac Toe gameplay.

Rather than relying on predefined moves, the AI evaluates every possible future board state before selecting the best move.

Although computationally expensive for larger games, Tic Tac Toe's small search space makes Minimax an ideal solution.

---

## Why Use Manager Classes?

Several responsibilities have been separated into manager classes.

Examples include:

- SettingsManager
- StatisticsManager
- FileManager
- AnimationManager

Manager classes reduce duplicated code while improving organization and reuse.

---

## Why Use Constants?

All frequently used values are stored inside `constants.py` and `theme.py`.

Examples include:

- colors
- player symbols
- board size
- file paths
- status messages

Centralizing these values makes future modifications significantly easier.

---

## Why Modularize the Project?

Rather than creating one extremely large source file, the application has been divided into multiple small modules.

Benefits include:

- improved readability
- easier debugging
- better scalability
- simpler testing
- easier collaboration

Each module performs one primary responsibility.

---

# 9. Future Improvements

Although the application is fully functional, several additional features could be added in future versions.

---

## Additional Themes

Support multiple visual themes, including:

- Dark Mode
- High Contrast Mode
- Custom Color Themes

---

## Sound Effects

Add optional audio feedback for:

- button clicks
- victories
- draws
- AI moves

---

## Improved Animations

Possible enhancements include:

- smoother button transitions
- animated board reset
- fading highlights
- celebration effects after victories

---

## Undo and Redo

Allow players to undo previous moves or redo moves before the game ends.

This feature would require maintaining a history of previous board states.

---

## Custom Board Sizes

Expand the application beyond the traditional 3×3 board.

Examples include:

- 4×4
- 5×5
- configurable board dimensions

Additional AI optimizations would be required for larger boards.

---

## Online Multiplayer

Introduce online gameplay through client-server networking.

Players could compete against each other over a network while preserving the existing graphical interface.

---

## Player Profiles

Support multiple user profiles with separate:

- statistics
- settings
- achievements
- saved preferences

---

## Achievements

Implement an achievement system rewarding milestones such as:

- first victory
- winning streaks
- undefeated games
- AI victories
- total games played

---

## Enhanced Statistics

Expand statistical tracking to include:

- average game duration
- fastest victory
- longest winning streak
- AI win percentage
- human win percentage
- total moves played

---

# Conclusion

The Advanced Tic Tac Toe project demonstrates the development of a complete desktop application using modern software engineering practices. Through modular architecture, object-oriented programming, artificial intelligence, persistent data storage, reusable utilities, and a clean graphical interface, the project extends a classic game into a maintainable and extensible software system.

By separating responsibilities across dedicated modules, the application remains easy to understand, test, and expand. The architecture encourages code reuse, simplifies maintenance, and provides a strong foundation for future enhancements such as additional themes, online multiplayer, advanced statistics, and richer user interface features.

Overall, this project serves as both a functional game and a practical demonstration of software design principles, showcasing the importance of clean architecture, modular development, and thoughtful organization in real-world Python applications 