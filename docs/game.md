# Game Folder Documentation

## 1. Purpose

The `game` folder contains the **core backend logic** of the Advanced Tic Tac Toe application. It is responsible for everything that makes the game function independently of the graphical interface, including the board, players, game flow, AI, settings, statistics, validation, and file management.

The `game` package is intentionally separated from the `ui` package. The game logic should be able to determine moves, winners, draws, scores, and AI decisions without needing to know how those results are displayed on screen.

---

## 2. Role in the Project

The `game` folder acts as the **core engine** of the application.

It contains the components responsible for:

* Representing the game board
* Managing players
* Processing moves
* Detecting wins
* Detecting draws
* Managing turns
* Managing game state
* Implementing AI behavior
* Implementing the Minimax algorithm
* Managing application settings
* Managing persistent statistics
* Managing JSON files
* Validating input and stored data
* Providing reusable helper functions
* Storing shared constants

The UI communicates with this backend rather than implementing game rules itself.

---

## 3. Directory Structure

The `game` directory is structured approximately as follows:

```text
game/
├── __init__.py
├── ai.py
├── board.py
├── constants.py
├── file_manager.py
├── game.py
├── helper.py
├── minimax.py
├── player.py
├── settings.py
├── statistics.py
└── validator.py
```

Each module has a specific responsibility.

---

# 4. `__init__.py`

`__init__.py` identifies `game` as a Python package.

It allows other parts of the project to import modules using package-based paths such as:

```python
from game.board import Board
```

and:

```python
from game.game import Game
```

The file may also expose selected package-level objects if required.

Its primary purpose is package organization rather than game logic.

---

# 5. `constants.py`

`constants.py` contains shared constants used throughout the project.

Instead of repeatedly writing the same values throughout multiple files, the project defines them centrally.

Examples include:

* Board size
* Empty-cell representation
* Player X symbol
* Player O symbol
* Default player names
* AI difficulty values
* Theme names
* File paths
* UI-related constants used by backend components

For example:

```text
BOARD_SIZE
EMPTY_CELL
PLAYER_X
PLAYER_O
```

Centralizing these values reduces duplication and makes the application easier to maintain.

---

## 5.1 Why Constants Are Centralized

Without `constants.py`, multiple modules would need to define their own copies of important values.

That could lead to inconsistencies.

For example, one module might assume:

```text
BOARD_SIZE = 3
```

while another accidentally uses a different value.

By defining the value once, every module can use the same configuration.

---

# 6. `board.py`

`board.py` contains the `Board` class.

The `Board` class represents the actual Tic Tac Toe board and manages operations performed directly on it.

Its responsibilities include:

* Creating an empty board
* Resetting the board
* Reading board contents
* Reading individual cells
* Setting cells
* Clearing cells
* Checking whether cells are empty
* Validating moves
* Placing player moves
* Finding available moves
* Checking whether the board is full
* Detecting winners
* Detecting winning positions
* Detecting draws
* Producing a readable board representation

---

## 6.1 Board Representation

The board is represented internally as a two-dimensional list.

Conceptually:

```text
[
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]
```

A completed board might look like:

```text
[
    ["X", "O", "X"],
    ["O", "X", ""],
    ["", "", "O"]
]
```

Rows and columns use zero-based indexing.

---

## 6.2 Move Validation

`Board.is_valid_move()` determines whether a move can be made.

A move is valid only when:

1. The position is inside the board.
2. The cell is currently empty.

This prevents invalid coordinates and overwriting existing moves.

---

## 6.3 Winner Detection

`Board.check_winner()` checks:

* All rows
* All columns
* Main diagonal
* Secondary diagonal

If a player has completed a winning line, the corresponding symbol is returned.

If nobody has won:

```python
None
```

is returned.

---

## 6.4 Winning Positions

`Board.get_winning_positions()` identifies the exact coordinates belonging to the winning line.

For example:

```text
[(0, 0), (0, 1), (0, 2)]
```

This information is later used by the UI to highlight the winning cells.

---

## 6.5 Draw Detection

A draw occurs when:

* The board is full.
* No player has won.

This is determined by:

```python
Board.is_draw()
```

---

# 7. `player.py`

`player.py` contains the `Player` class.

A `Player` object represents one participant in a game.

Each player stores:

* Name
* Symbol
* AI status
* Score

For example:

```text
Player 1
Symbol: X
AI: False
Score: 3
```

---

## 7.1 Player Validation

The constructor validates:

* Player name
* Player symbol
* AI status

Invalid values result in appropriate exceptions.

This prevents invalid player objects from entering the game system.

---

## 7.2 Score Management

The class provides methods for:

```text
add_point()
reset_score()
```

These allow the game controller to update scores without directly manipulating the internal score whenever possible.

---

## 7.3 Player Information

`get_details()` returns the player's information as a dictionary.

This provides a convenient structured representation of the player.

---

# 8. `game.py`

`game.py` contains the `Game` class.

This is the **main game controller**.

While `Board` manages the physical board state and `Player` represents individual players, `Game` coordinates them into an actual game.

Its responsibilities include:

* Creating players
* Creating the board
* Tracking the current player
* Processing moves
* Switching turns
* Detecting game completion
* Tracking the winner
* Tracking winning positions
* Updating player scores
* Managing resets
* Providing game-state information

---

## 8.1 Game Initialization

When a `Game` object is created, it initializes:

```text
Board
Player X
Player O
Current player
Winner
Game-over state
Winning positions
```

Player X always begins the game.

---

## 8.2 Move Processing

The main gameplay flow is:

```text
Player selects cell
        ↓
Game.make_move()
        ↓
Board validates move
        ↓
Move placed
        ↓
Game state updated
        ↓
Winner/draw checked
        ↓
If game continues → switch player
```

This makes `Game` the central coordinator between the board and players.

---

## 8.3 Game State

`get_game_state()` provides a structured representation of the current game.

It contains information such as:

* Current player
* Winner
* Game-over state
* Board contents
* Winning positions

This can be useful for debugging, UI synchronization, or future features.

---

# 9. `ai.py`

`ai.py` contains the AI player implementation.

Its purpose is to allow the game to operate in Human vs AI mode.

The AI can select moves based on the configured difficulty.

The AI system is designed to provide different levels of challenge.

---

## 9.1 AI Difficulty

The project supports multiple AI difficulty levels.

These are defined centrally in `constants.py`.

The AI can therefore provide different behaviors depending on the selected difficulty.

Conceptually:

```text
Easy
  ↓
Simpler decision-making

Medium
  ↓
More strategic decision-making

Impossible
  ↓
Minimax-based optimal decision-making
```

---

## 9.2 AI and Board Interaction

The AI does not directly manipulate the graphical interface.

Instead, it receives game information and determines a move.

The resulting move is then passed to the `Game` controller.

This keeps the AI independent of Tkinter.

---

# 10. `minimax.py`

`minimax.py` implements the **Minimax algorithm** used by the Impossible AI.

Minimax evaluates possible future game states and determines the move that produces the strongest outcome for the AI.

The module contains two major functions:

```text
minimax()
find_best_move()
```

---

## 10.1 `minimax()`

The recursive `minimax()` function evaluates possible game states.

It assigns scores based on the outcome:

```text
AI victory      → positive score
Opponent victory → negative score
Draw            → 0
```

Depth is incorporated into the score so that the AI prefers faster victories and delays losses when possible.

Conceptually:

```text
Current board
     ↓
Generate possible moves
     ↓
Simulate each move
     ↓
Recursively evaluate resulting states
     ↓
Choose maximum/minimum score
     ↓
Return best score
```

---

## 10.2 `find_best_move()`

`find_best_move()` examines the available moves and uses Minimax to determine the strongest move.

If there are no available moves, it returns:

```python
None
```

Otherwise it returns a coordinate:

```text
(row, column)
```

This function is the main entry point used when the Impossible AI needs to select a move.

---

# 11. `helper.py`

`helper.py` contains reusable utility functions.

These functions are intentionally kept separate from larger classes so that multiple modules can use them.

Current responsibilities include:

* Creating empty boards
* Finding available moves
* Checking whether a board is full
* Formatting time
* Finding the project root
* Clamping values
* Determining the opposite player

---

## 11.1 `create_empty_board()`

Creates a new empty Tic Tac Toe board.

This is used by `Board` when initializing and resetting itself.

---

## 11.2 `get_available_moves()`

Returns all currently empty positions.

For example:

```text
[(0, 1), (1, 2), (2, 0)]
```

This function is particularly important for AI and Minimax because they need to know which moves can still be played.

---

## 11.3 `is_board_full()`

Determines whether there are no empty cells remaining.

It relies on the available-moves functionality rather than duplicating the board-scanning logic.

---

## 11.4 `format_time()`

Converts a number of seconds into:

```text
MM:SS
```

format.

Example:

```text
125 → 02:05
```

---

## 11.5 `get_project_root()`

Determines the project's root directory based on the location of `helper.py`.

This is useful when constructing paths to project resources.

---

## 11.6 `clamp()`

Restricts a value to a specified range.

For example:

```text
value = 15
minimum = 0
maximum = 10

result = 10
```

---

## 11.7 `opposite_player()`

Returns the opposite player symbol.

Conceptually:

```text
X → O
O → X
```

---

# 12. `validator.py`

`validator.py` contains reusable validation functions.

Its purpose is to prevent invalid information from entering the application.

The module validates:

* Board positions
* Player names
* Themes
* AI difficulties
* Boolean values
* Integer values
* Statistics dictionaries
* Settings dictionaries

---

## 12.1 Position Validation

`is_valid_position()` determines whether coordinates fall within the board.

For a 3×3 board:

```text
Valid rows: 0–2
Valid columns: 0–2
```

---

## 12.2 Player Name Validation

`is_valid_player_name()` ensures that player names satisfy the project's requirements.

The current rules include:

* Must be a string
* Must contain between 1 and 20 characters after stripping whitespace
* Must contain at least one alphanumeric character

This prevents blank or meaningless player names.

---

## 12.3 Theme Validation

`is_valid_theme()` checks whether the selected theme is supported.

---

## 12.4 Difficulty Validation

`is_valid_difficulty()` checks whether a requested AI difficulty is defined in the project's constants.

---

## 12.5 Type Validation

Two general-purpose validators are provided:

```text
is_boolean()
is_integer()
```

`is_integer()` deliberately rejects Boolean values because Python considers `bool` to be a subclass of `int`.

---

## 12.6 Settings Validation

`validate_settings()` checks that the settings dictionary:

* Is a dictionary
* Contains exactly the required keys
* Contains a valid theme
* Contains valid Boolean values
* Contains a valid AI difficulty

---

## 12.7 Statistics Validation

`validate_statistics()` verifies that:

* The supplied data is a dictionary.
* The required statistic keys are present.
* No unexpected keys exist.
* All values are non-negative integers.

This protects the application from corrupted statistics data.

---

# 13. `file_manager.py`

`file_manager.py` provides centralized JSON file management.

The `FileManager` class handles operations such as:

```text
ensure_directory_exists()
create_file_if_missing()
load_json()
save_json()
reset_json()
file_exists()
delete_file()
```

---

## 13.1 Why FileManager Exists

Without `FileManager`, `SettingsManager` and `StatisticsManager` would each need to implement their own file-handling logic.

Instead:

```text
SettingsManager ──────┐
                      │
StatisticsManager ────┼──→ FileManager → JSON
                      │
Other future systems ─┘
```

This reduces duplicated code and creates a consistent file-management layer.

---

# 14. `settings.py`

`settings.py` contains the `SettingsManager` class.

It manages persistent application settings stored in:

```text
data/settings.json
```

Its responsibilities include:

* Loading settings
* Creating missing settings files
* Validating settings
* Saving settings
* Updating individual settings
* Returning individual settings
* Returning all settings
* Restoring default settings

---

## 14.1 Default Settings

The manager defines default values for settings such as:

```text
theme
ai_enabled
difficulty
sound_enabled
animations_enabled
```

If the settings file is missing or invalid, these defaults are restored.

---

# 15. `statistics.py`

`statistics.py` contains the `StatisticsManager` class.

It manages persistent gameplay statistics stored in:

```text
data/statistics.json
```

It is responsible for:

* Loading statistics
* Creating missing statistics files
* Validating statistics
* Recording wins
* Recording draws
* Returning individual statistics
* Returning all statistics
* Resetting statistics
* Saving changes

---

## 15.1 Recorded Statistics

The current statistics system tracks:

```text
games_played
x_wins
o_wins
ai_wins
draws
```

These values allow the application to maintain statistics across multiple sessions.

---

# 16. Relationship Between the Modules

The modules are not isolated. They form a layered backend architecture.

A simplified relationship is:

```text
                         Game
                          │
             ┌────────────┼────────────┐
             │            │            │
             ▼            ▼            ▼
           Board        Player         AI
             │                         │
             │                         ▼
             │                      Minimax
             │
             ▼
          Helpers
             │
             ▼
         Validator
```

Persistent data is handled separately:

```text
SettingsManager ──→ FileManager ──→ settings.json

StatisticsManager ─→ FileManager ──→ statistics.json
```

Shared configuration is supplied by:

```text
constants.py
```

---

# 17. Core Gameplay Flow

The major backend gameplay flow is:

```text
Game created
    ↓
Board initialized
    ↓
Players initialized
    ↓
Player X starts
    ↓
make_move()
    ↓
Board validates move
    ↓
Move placed
    ↓
check_winner()
    ↓
Winner?
 ┌──┴──┐
Yes    No
 ↓      ↓
Game   is_draw()
over     ↓
       ┌─┴─┐
      Yes  No
       ↓    ↓
     Draw  switch_player()
              ↓
          Next turn
```

This loop continues until the game reaches a win or draw.

---

# 18. AI Gameplay Flow

When AI mode is enabled, the flow becomes:

```text
Human move
    ↓
Game.make_move()
    ↓
Game state updated
    ↓
Human wins/draw?
   ↙        ↘
 Yes         No
 ↓           ↓
End        AI turn
             ↓
       AI chooses move
             ↓
       Game.make_move()
             ↓
       Game state updated
             ↓
       Winner/draw?
             ↓
          Continue
```

For Impossible difficulty, the AI ultimately uses Minimax to determine its move.

---

# 19. Separation from the UI

One of the most important architectural decisions is that the `game` package does not depend on the graphical interface for its core functionality.

For example, `Board` does not need to know:

* What a Tkinter button looks like
* What color X should be
* What animation should play
* Where a cell appears on screen

Instead:

```text
game/
    ↓
Game state and rules
    ↓
ui/
    ↓
Visual representation
```

This makes the backend easier to:

* Test
* Debug
* Reuse
* Extend
* Maintain

---

# 20. Interaction with the UI

The UI communicates with the backend primarily through `Game`.

For example:

```text
MainWindow
    ↓
Game.make_move()
    ↓
Board.place_move()
    ↓
Board.check_winner()
    ↓
Game.update_game_state()
    ↓
MainWindow updates display
```

The UI therefore acts as a presentation and interaction layer while the `game` package remains responsible for game logic.

---

# 21. Testing the Game Package

The `game` package is extensively testable because most of its functionality does not require a graphical interface.

The corresponding tests are located in:

```text
tests/
```

Relevant test files include:

```text
tests/
├── test_ai.py
├── test_board.py
├── test_file_manager.py
├── test_game.py
├── test_helper.py
├── test_minimax.py
├── test_player.py
├── test_settings.py
├── test_statistics.py
└── test_validator.py
```

These tests verify individual backend components independently.

---

## 21.1 Board Testing

`test_board.py` tests:

* Board initialization
* Board reset
* Cell access
* Cell modification
* Move validation
* Move placement
* Available moves
* Full-board detection
* Winner detection
* Winning positions
* Draw detection
* Board string representation

---

## 21.2 Game Testing

`test_game.py` tests:

* Game initialization
* Player creation
* Turn switching
* Move processing
* Winner detection
* Draw detection
* Score updates
* Game state
* Resetting the board
* Resetting the complete game
* Player lookup
* Symbol lookup

---

## 21.3 AI and Minimax Testing

The AI tests verify that different difficulty levels behave correctly.

`test_minimax.py` specifically tests the algorithm's ability to:

* Detect winning moves
* Detect blocking moves
* Evaluate winning states
* Evaluate losing states
* Evaluate draws
* Select optimal moves
* Return `None` when no moves remain

---

## 21.4 Manager Testing

`test_settings.py`, `test_statistics.py`, and `test_file_manager.py` verify the persistence layer.

These tests should generally isolate filesystem operations using temporary files or mocked dependencies.

---

# 22. Error Handling

The backend uses several approaches to prevent invalid state.

Examples include:

```text
ValueError
TypeError
False return values
None return values
Validation functions
Default-value recovery
```

For example, `Board.set_cell()` raises a `ValueError` when supplied with an invalid position or symbol.

By contrast, `Board.place_move()` returns `False` when a move cannot be played.

The distinction allows methods to communicate errors appropriately depending on their purpose.

---

# 23. Design Principles

The `game` package follows several important software-engineering principles.

### Separation of concerns

Each module has a focused responsibility.

### Reusability

Common functionality is placed in helper modules instead of being duplicated.

### Encapsulation

Classes such as `Board`, `Player`, `Game`, `SettingsManager`, and `StatisticsManager` manage their own state.

### Validation

Input and persistent data are validated before being accepted.

### Testability

Core game functionality can be tested without launching the graphical application.

### Maintainability

Constants and reusable functionality are centralized.

### Modularity

Individual systems can be modified without rewriting unrelated parts of the application.

---

# 24. Dependency Overview

A simplified dependency structure looks like this:

```text
constants.py
     │
     ├──────────────┐
     ▼              ▼
validator.py      helper.py
     │              │
     ├──────┬───────┘
     │      │
     ▼      ▼
  player.py board.py
     │       │
     └───┬───┘
         ▼
       game.py
         │
         └────────→ ai.py
                       │
                       ▼
                   minimax.py
```

The persistence components form another branch:

```text
constants.py
     │
     ├───────────────┐
     ▼               ▼
file_manager.py   validator.py
     │               │
     ▼               │
settings.py ◄────────┘
     │
     ▼
data/settings.json
```

and:

```text
file_manager.py
      │
      ▼
statistics.py
      │
      ▼
data/statistics.json
```

---

# 25. Overall Responsibility

The easiest way to understand the `game` folder is to think of it as the application's **brain**.

| File              | Primary Responsibility          |
| ----------------- | ------------------------------- |
| `__init__.py`     | Defines the package             |
| `constants.py`    | Shared project constants        |
| `board.py`        | Board state and rules           |
| `player.py`       | Player representation           |
| `game.py`         | Overall game controller         |
| `ai.py`           | AI decision-making              |
| `minimax.py`      | Optimal AI algorithm            |
| `helper.py`       | Reusable utility functions      |
| `validator.py`    | Input/data validation           |
| `file_manager.py` | JSON file operations            |
| `settings.py`     | Persistent application settings |
| `statistics.py`   | Persistent gameplay statistics  |

---

# 26. Summary

The `game` folder is the **core logic layer** of Advanced Tic Tac Toe.

It contains the complete backend required to run the game independently of its graphical interface. The `Game` class coordinates the `Board` and `Player` objects, while the AI system provides computer-controlled gameplay. `minimax.py` supplies optimal decision-making for the highest AI difficulty.

Supporting modules such as `helper.py`, `validator.py`, and `constants.py` provide reusable infrastructure, while `FileManager`, `SettingsManager`, and `StatisticsManager` handle persistent application data.

The overall architecture can be summarized as:

```text
                    GAME PACKAGE
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
     Gameplay           AI           Persistence
        │                │                │
   ┌────┼────┐           ▼          ┌─────┴─────┐
   │    │    │        Minimax       │           │
   ▼    ▼    ▼                      ▼           ▼
 Board Player Game              Settings    Statistics
        │    │                      │           │
        └────┴──────┐               │           │
                    ▼               ▼           ▼
                 Helpers       settings.json statistics.json
                    │
                    ▼
                Validator
```

Together, these modules form a modular backend that handles **game rules, state management, AI, validation, persistence, and reusable utilities**, while leaving presentation and user interaction to the separate `ui` package.

