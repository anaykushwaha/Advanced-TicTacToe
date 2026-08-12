# UI Folder Documentation

## 1. Purpose

The `ui` folder contains all of the **graphical user interface components** for the Advanced Tic Tac Toe application. It is responsible for creating the visual appearance of the game, displaying the board, handling dialogs, managing the main application window, and providing visual feedback to the player.

The UI layer is intentionally separated from the core game logic contained in the `game` folder. This allows the game's rules, players, AI, settings, and statistics to operate independently from Tkinter-specific code.

---

## 2. Role in the Project

The `ui` folder acts as the presentation layer of the application.

It connects the user to the underlying game engine by:

* Displaying the game board
* Showing player turns and game status
* Displaying scores
* Handling graphical interaction
* Showing confirmation and information dialogs
* Providing visual feedback for winning moves
* Applying consistent colors, fonts, dimensions, and styling
* Managing animations and visual effects
* Coordinating the graphical application window

The UI does not determine the fundamental rules of Tic Tac Toe. Instead, it communicates with classes in the `game` package to display and interact with the current game state.

---

## 3. Technology

The graphical interface is built using **Python's Tkinter library**.

Tkinter provides the application's:

* Main window
* Frames
* Buttons
* Labels
* Message boxes
* Event handling
* Widget configuration
* Main event loop

The UI also uses Python's standard typing features to make callback functions and widget-related code easier to understand and maintain.

---

## 4. UI Architecture

The UI layer is divided into several focused modules rather than placing the entire interface inside one large file.

The major components are:

```text
ui/
├── __init__.py
├── animations.py
├── dialogs.py
├── game_board.py
├── main_window.py
└── theme.py
```

Each module has a specific responsibility.

This modular structure prevents the graphical code from becoming tightly coupled and makes individual UI components easier to test and modify.

---

## 5. `main_window.py`

`main_window.py` contains the `MainWindow` class, which acts as the **main controller for the graphical application**.

It is the primary connection between the backend and the UI.

The `MainWindow` class:

* Creates the Tkinter root window
* Configures the application window
* Creates the game engine
* Creates the AI player
* Loads settings
* Loads statistics
* Creates the graphical widgets
* Handles board clicks
* Updates the graphical board
* Updates status messages
* Handles completed games
* Performs AI moves
* Starts new games
* Resets session scores
* Toggles AI mode
* Changes AI difficulty
* Displays dialogs
* Saves data when the application closes
* Starts the Tkinter event loop

### Important methods

#### `__init__()`

Initializes the entire application window and its major components.

It creates:

* The Tkinter root
* Settings manager
* Statistics manager
* Game object
* AI player
* Score variables
* Tkinter display variables
* UI components

It then calls `_create_widgets()` to construct the interface.

#### `_create_widgets()`

Builds the visible interface.

This includes:

* Application title
* Status label
* Scoreboard
* Game board

#### `_on_cell_clicked()`

Handles user interaction with a board cell.

It checks whether the game is still active, attempts to make the move through the `Game` object, updates the interface, checks whether the game ended, and triggers the AI when appropriate.

#### `_update_board()`

Synchronizes the graphical board with the backend `Board` object.

The method determines which cells contain `X` or `O` and updates the corresponding graphical buttons.

#### `_handle_game_end()`

Processes the completion of a game.

It handles:

* Player victories
* Draws
* Session score updates
* Persistent statistics
* Status messages
* Winning-cell highlighting
* Game-over dialogs
* Starting another game

#### `_perform_ai_move()`

Requests a move from the `AIPlayer`, applies it through the `Game` object, and updates the interface.

#### `new_game()`

Resets the current game while preserving the session scoreboard.

#### `reset_scores()`

Resets the current X, O, and draw counters after confirmation from the user.

#### `toggle_ai()`

Enables or disables AI mode and updates the corresponding setting.

#### `set_ai_difficulty()`

Changes the AI difficulty and persists the new setting.

#### `exit_application()`

Saves settings and statistics before destroying the Tkinter root window.

#### `run()`

Starts the Tkinter event loop.

---

## 6. `game_board.py`

`game_board.py` contains the `GameBoard` class.

`GameBoard` is responsible specifically for the **visual representation of the 3×3 Tic Tac Toe board**.

It inherits from:

```python
tk.Frame
```

The class creates a 3×3 grid of Tkinter buttons.

### Responsibilities

The `GameBoard` class handles:

* Creating board buttons
* Connecting buttons to click callbacks
* Updating individual cells
* Clearing the board
* Enabling cells
* Disabling cells
* Enabling the entire board
* Disabling the entire board
* Highlighting winning cells
* Resetting cell colors
* Retrieving individual buttons

### Important methods

#### `__init__()`

Creates the graphical board and stores the callback that should be executed when a player clicks a cell.

#### `_create_board()`

Constructs the 3×3 button grid.

Each button:

* Represents one board position
* Displays an empty value initially
* Uses the configured theme
* Calls the supplied callback when clicked
* Receives the hover animation behavior

#### `update_cell()`

Changes the displayed symbol and color of a particular cell and disables the button after the move.

#### `clear_board()`

Restores every button to its default empty state.

#### `enable_cell()` / `disable_cell()`

Control whether an individual board cell can be interacted with.

#### `enable_board()`

Enables all currently empty cells while leaving occupied cells disabled.

#### `disable_board()`

Disables every board cell.

This is used when the game ends.

#### `highlight_cells()`

Highlights the cells belonging to the winning line and triggers the winning-cell animation.

#### `reset_cell_colors()`

Restores all board cells to their standard background color.

#### `get_button()`

Returns a specific Tkinter button while validating that the requested position is within the board boundaries.

---

## 7. `dialogs.py`

`dialogs.py` contains the `DialogManager` class.

This class provides reusable wrappers around Tkinter's `messagebox` functionality.

Centralizing dialogs prevents individual parts of the application from directly managing message boxes.

### Available dialogs

The class provides methods for:

* Game-over messages
* New-game confirmation
* Score-reset confirmation
* Exit confirmation
* About information
* Statistics display
* General information
* Warnings
* Errors

### Why use `DialogManager`?

Without a dedicated dialog manager, `MainWindow` would contain many direct calls to `messagebox`.

Instead, the UI can simply call:

```text
DialogManager.show_game_over(...)
```

or:

```text
DialogManager.confirm_exit()
```

This keeps the main controller cleaner and makes dialog behavior easier to modify or test.

---

## 8. `animations.py`

`animations.py` contains the application's reusable visual animation functionality.

The animation layer is responsible for making the interface feel more interactive and polished without changing the underlying game logic.

The `AnimationManager` is used by graphical components such as `GameBoard`.

### Animation responsibilities

Depending on the implemented animation methods, this module handles visual effects such as:

* Button hover effects
* Winning-cell flashing
* Temporary visual changes
* Restoring widgets to their normal appearance

The animation manager is deliberately separate from `GameBoard` so that animation behavior can be changed without rewriting the board implementation.

This separation also allows animations to be disabled or modified independently of the core game logic.

---

## 9. `theme.py`

`theme.py` contains the application's centralized visual configuration.

Instead of hard-coding colors, fonts, dimensions, and display strings throughout the UI files, these values are defined in one location.

The theme module contains constants for areas such as:

* Window title
* Window dimensions
* Window resizing behavior
* Background colors
* Button colors
* Hover colors
* Text colors
* X and O colors
* Winning-cell colors
* Fonts
* Board dimensions
* Cell dimensions
* Padding
* Section spacing
* Status messages
* Dialog titles
* Empty-cell values
* Theme-related settings

### Benefits of centralized theme constants

Centralizing UI configuration provides several advantages:

* Consistent appearance
* Easier visual customization
* Less duplicated code
* Easier maintenance
* Fewer accidental inconsistencies
* Simpler future theme changes

For example, changing the application's primary background color can be done in `theme.py` rather than searching through every UI file.

---

## 10. Interaction Between UI Components

The UI components work together as a layered system.

A typical player move follows this sequence:

```text
User clicks a GameBoard button
        ↓
GameBoard invokes its callback
        ↓
MainWindow._on_cell_clicked()
        ↓
Game.make_move()
        ↓
Board.place_move()
        ↓
Game state is updated
        ↓
MainWindow._update_board()
        ↓
GameBoard.update_cell()
        ↓
MainWindow checks for game completion
        ↓
DialogManager / AnimationManager if necessary
```

This structure ensures that each class remains responsible for its own role.

For example:

* `GameBoard` does not determine whether a move is legal.
* `Board` does not know anything about Tkinter.
* `DialogManager` does not manage game state.
* `AnimationManager` does not determine winners.
* `MainWindow` coordinates the different components.

---

## 11. Separation from the Game Package

One of the most important architectural decisions in the project is the separation between:

```text
game/
```

and:

```text
ui/
```

The `game` package contains the underlying application logic, while the `ui` package contains the graphical presentation.

The game package handles things such as:

* Board state
* Players
* Game rules
* AI
* Minimax
* Settings
* Statistics
* Validation
* File management

The UI package handles:

* Windows
* Buttons
* Labels
* Dialogs
* Animations
* Visual styling
* User interaction

This means the core game logic can theoretically be reused with another interface without rewriting the underlying rules.

---

## 12. Callback-Based Interaction

The UI uses callback functions to connect graphical events to game logic.

For example, `GameBoard` receives a callback when it is created:

```text
GameBoard(
    parent,
    cell_click_callback,
)
```

When a player clicks a button, the board passes the corresponding row and column to the callback.

`MainWindow` provides `_on_cell_clicked()` as that callback.

This allows `GameBoard` to remain unaware of the larger game system.

It only needs to communicate:

```text
"The user clicked row X, column Y."
```

The `MainWindow` then decides what should happen.

---

## 13. Visual State Management

The UI reflects several different game states.

### Ready state

The application has been initialized and is waiting for the first move.

### Player-turn state

The status label identifies which player's turn it is.

### AI-thinking state

The status label indicates that the AI is selecting a move.

### Winner state

The UI displays the winner, disables the board, highlights the winning line, and displays a game-over dialog.

### Draw state

The UI disables the board, updates the draw count, displays the draw status, and shows a game-over dialog.

### New-game state

The board is cleared, cells are re-enabled, and the status returns to the ready state.

Keeping these states coordinated is primarily the responsibility of `MainWindow`.

---

## 14. Error and Boundary Handling

The UI components include checks to prevent invalid graphical operations.

For example, `GameBoard.get_button()` validates row and column coordinates before accessing the button grid.

The UI also relies on the backend's validation rather than attempting to duplicate all game rules.

For example, when a board cell is clicked, `MainWindow` delegates move validation to:

```text
Game.make_move()
```

This avoids having two separate implementations of the game's move-validation rules.

---

## 15. Testing the UI

The UI is tested through the project's `tests` folder.

Relevant test modules include:

* `test_game_board.py`
* `test_dialogs.py`
* `test_main_window.py`

Because Tkinter creates graphical objects and dialogs, these tests use mocks extensively.

This allows the tests to verify behavior without requiring a user to manually interact with the application during automated testing.

Examples include verifying that:

* A board button is updated correctly
* A winning line is highlighted
* A dialog is called with the correct message
* The main window creates its components
* AI moves are triggered correctly
* Scores are updated correctly
* The application saves data when exiting

---

## 16. Design Principles

The UI package follows several software-design principles.

### Single Responsibility

Each class has a focused purpose.

`GameBoard` manages the board display, while `DialogManager` manages dialogs and `MainWindow` coordinates the overall application.

### Separation of Concerns

Game rules are kept outside the UI.

The UI displays and communicates with the game engine rather than implementing the rules itself.

### Reusability

Dialogs and animations are centralized into reusable managers rather than duplicated across the application.

### Maintainability

Theme values are centralized, making visual changes easier.

### Modularity

Individual UI components can be changed or tested without requiring the entire application to be rewritten.

---

## 17. Summary

The `ui` folder forms the **presentation and interaction layer** of Advanced Tic Tac Toe.

Its components work together to turn the backend game engine into a complete desktop application:

* `main_window.py` coordinates the application.
* `game_board.py` displays and manages the interactive board.
* `dialogs.py` manages message boxes and confirmations.
* `animations.py` provides visual effects.
* `theme.py` centralizes the application's visual configuration.
* `__init__.py` identifies the directory as the UI package.

The overall architecture keeps graphical concerns separate from the game's underlying logic while providing a clean path for user interaction. This separation makes the project easier to test, maintain, extend, and potentially adapt to a different interface in the future.

