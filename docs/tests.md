# Tests Folder Documentation

## 1. Purpose

The `tests` folder contains the automated unit tests for the **Advanced Tic Tac Toe** application. Its purpose is to verify that the individual components of the project behave correctly, detect regressions when code is changed, and provide confidence that the application's core game logic and graphical components work as intended.

The tests are written using Python's built-in `unittest` framework, with `unittest.mock` used where necessary to isolate components from external dependencies such as files, Tkinter widgets, dialogs, AI behavior, and other classes.

---

## 2. Role in the Project

The `tests` folder is separate from the application's actual source code. Files inside this folder do not implement game functionality; instead, they **verify functionality implemented elsewhere in the project**.

The tests primarily cover:

* Core game logic
* Board management
* Player management
* Input validation
* Minimax decision-making
* AI behavior
* Settings management
* Statistics management
* File management
* Graphical board behavior
* Dialog behavior
* Main application-window behavior

This separation keeps testing code independent from the production code while allowing every major component to be checked individually.

---

## 3. Testing Framework

The project uses Python's built-in `unittest` framework.

A typical test file imports:

```python
import unittest
```

and defines a test class that inherits from:

```python
unittest.TestCase
```

Individual methods beginning with `test_` are automatically discovered and executed by the test framework.

The tests use assertions such as:

* `assertEqual()`
* `assertTrue()`
* `assertFalse()`
* `assertIsNone()`
* `assertIsNotNone()`
* `assertRaises()`
* `assertIn()`
* `assert_called_once()`
* `assert_called_once_with()`
* `assert_not_called()`

These assertions allow the tests to verify both returned values and interactions between different components.

---

## 4. Mocking

Some parts of the application cannot or should not be tested using their real dependencies.

For example, `MainWindow` creates a real Tkinter window, while `DialogManager` displays real message boxes. Running these components directly during automated tests would make the tests dependent on the graphical environment.

The project therefore uses:

```python
from unittest.mock import MagicMock, Mock, patch
```

Mocking is used to replace real dependencies with controllable test objects.

Examples include:

* Replacing `tk.Tk` with a mock object
* Replacing `GameBoard` with a mock
* Replacing `AIPlayer` with a mock
* Replacing `SettingsManager` and `StatisticsManager`
* Replacing message-box functions
* Preventing real JSON files from being modified during certain tests
* Verifying that methods were called with the correct arguments

This allows each component to be tested independently.

---

## 5. Test Files

The folder contains a dedicated test file for the major modules of the project.

### `test_board.py`

Tests the `Board` class.

It verifies:

* Creation of an empty board
* Board resetting
* Retrieving board copies
* Cell access
* Empty-cell detection
* Move validation
* Placing valid moves
* Rejecting invalid moves
* Setting and clearing cells
* Available-move detection
* Full-board detection
* Winner detection
* Winning-position detection
* Draw detection
* String representation of the board

---

### `test_game.py`

Tests the `Game` class and overall game flow.

It verifies:

* Game initialization
* Player creation
* Turn management
* Making moves
* Switching players
* Winner detection
* Draw detection
* Game-over state
* Winning positions
* Player and symbol retrieval
* Score tracking
* AI-mode detection
* Game-state information
* Board resetting
* Complete game resetting
* String and representation methods

---

### `test_player.py`

Tests the `Player` class.

It verifies:

* Valid player creation
* Invalid player names
* Invalid symbols
* Invalid AI values
* Score initialization
* Adding points
* Resetting scores
* Changing player names
* Retrieving player details
* String representation
* Object representation

---

### `test_validator.py`

Tests the reusable validation functions in `validator.py`.

It verifies:

* Valid and invalid board positions
* Valid and invalid player names
* Supported and unsupported themes
* Supported and unsupported AI difficulties
* Boolean validation
* Integer validation
* Statistics validation
* Settings validation

Because these functions are used by several other modules, testing them independently is particularly important.

---

### `test_helper.py`

Tests the reusable helper functions in `helper.py`.

It verifies:

* Empty-board creation
* Available-move generation
* Full-board detection
* Time formatting
* Project-root detection
* Number clamping
* Opposite-player detection

These tests ensure that common utility functions produce consistent results wherever they are used.

---

### `test_file_manager.py`

Tests the `FileManager` class.

It verifies:

* Directory creation
* File creation
* JSON loading
* JSON saving
* Invalid JSON handling
* File resetting
* File existence checking
* File deletion

Temporary files and directories are used where appropriate so that tests do not interfere with the project's actual application data.

---

### `test_settings.py`

Tests the `SettingsManager` class.

It verifies:

* Loading settings
* Default settings
* Saving settings
* Retrieving individual settings
* Updating valid settings
* Rejecting invalid settings
* Resetting settings to defaults
* Retrieving all settings

File-related operations can be mocked to prevent tests from changing the application's real settings file.

---

### `test_statistics.py`

Tests the `StatisticsManager` class.

It verifies:

* Loading statistics
* Default statistics
* Saving statistics
* Recording X wins
* Recording O wins
* Recording AI wins
* Recording draws
* Retrieving individual statistics
* Retrieving all statistics
* Resetting statistics

The tests ensure that game statistics are updated correctly and that persistence methods are called when necessary.

---

### `test_minimax.py`

Tests the Minimax algorithm and `find_best_move()`.

It verifies that the AI:

* Correctly evaluates winning positions
* Correctly evaluates losing positions
* Recognizes drawn positions
* Maximizes its score when appropriate
* Minimizes the opponent's score when appropriate
* Searches possible moves correctly
* Selects winning moves
* Blocks dangerous opponent moves
* Returns `None` when no moves remain

These tests are particularly important because Minimax is responsible for the behavior of the game's highest AI difficulty.

---

### `test_ai.py`

Tests the `AIPlayer` class and its different difficulty levels.

It verifies:

* AI initialization
* Difficulty configuration
* Easy-mode behavior
* Medium-mode behavior
* Impossible-mode behavior
* Move selection
* Handling boards with no available moves
* Interaction with the Minimax algorithm

The goal is to ensure that the public AI interface behaves correctly regardless of which internal strategy is being used.

---

### `test_dialogs.py`

Tests the `DialogManager` class.

Since the class displays Tkinter message boxes, the actual `messagebox` functions are mocked.

It verifies that:

* Game-over dialogs use the correct title and message
* New-game confirmation works correctly
* Score-reset confirmation works correctly
* Exit confirmation works correctly
* About information is displayed
* Statistics are calculated and displayed correctly
* Information dialogs use the supplied title and message
* Warning dialogs use the supplied title and message
* Error dialogs use the supplied title and message

---

### `test_game_board.py`

Tests the graphical `GameBoard` class.

Tkinter widgets and animation functions are mocked where appropriate.

It verifies:

* Board initialization
* Creation of the 3×3 button grid
* Cell updates
* Clearing the board
* Enabling individual cells
* Disabling individual cells
* Enabling empty cells
* Disabling the entire board
* Winning-cell highlighting
* Resetting cell colors
* Retrieving buttons
* Handling invalid board positions

The tests focus on the behavior of the `GameBoard` class rather than visually testing Tkinter itself.

---

### `test_main_window.py`

Tests the application's primary graphical controller, `MainWindow`.

Because `MainWindow` coordinates many other components, extensive mocking is used.

It verifies:

* Window initialization
* Window configuration
* Widget creation
* Initial status information
* Initial scoreboard values
* Loading settings
* Creating the game
* Creating the AI
* Handling board clicks
* Updating the graphical board
* Updating status messages
* Handling wins
* Handling draws
* Performing AI moves
* Starting new games
* Resetting scores
* Toggling AI mode
* Changing AI difficulty
* Showing About information
* Showing statistics
* Exiting the application
* Starting the Tkinter event loop

---

## 6. Testing Philosophy

The tests follow a **unit-testing approach**. Each test should focus on one behavior or responsibility rather than attempting to test the entire application simultaneously.

For backend classes such as `Board`, `Player`, `Game`, and `Validator`, tests primarily use real objects and verify their actual results.

For classes that depend heavily on external systems or other components, such as `MainWindow`, `DialogManager`, and `GameBoard`, mocks are used to isolate the component being tested.

This distinction keeps the test suite:

* Independent
* Repeatable
* Fast
* Predictable
* Easier to debug

---

## 7. Test Independence

Each test should be independent of the results of other tests.

Tests should not rely on:

* The order in which tests execute
* Data created by another test
* A particular previous game state
* Existing application statistics
* Existing settings
* A real graphical window remaining open
* A previous test modifying a shared object

Whenever state is required, it should be created or reset within the test itself.

The `setUp()` method is used when a fresh common environment is required before every test.

---

## 8. Testing Error Conditions

The test suite does not only test successful operations. Invalid input and failure conditions are also tested.

Examples include:

* Invalid board coordinates
* Invalid player names
* Invalid player symbols
* Invalid AI configuration
* Invalid settings
* Invalid statistics
* Invalid JSON
* Attempting to make moves on occupied cells
* Attempting to move after a game has ended
* Attempting to access invalid board buttons

Testing these cases helps prevent unexpected crashes and ensures that the application handles incorrect input safely.

---

## 9. Running the Tests

The tests can be executed from the project's root directory.

To run the entire test suite using Python's built-in test discovery:

```text
python -m unittest discover
```

If the test files are specifically located inside the `tests` directory, the following can also be used:

```text
python -m unittest discover -s tests
```

A successful test run should report that all discovered tests passed.

Individual test modules can also be executed when debugging a particular component, for example:

```text
python -m unittest tests.test_board
```

or:

```text
python -m unittest tests.test_game
```

---

## 10. Importance to the Project

The `tests` folder acts as a safety net for the entire application.

As the project grows, changes to one component can unintentionally affect another component. Automated tests make these regressions easier to detect.

For example, changing `Board.place_move()` could potentially affect `Game.make_move()`, the AI, and the graphical interface. Running the test suite after such a change provides immediate feedback about whether existing behavior has been preserved.

The test suite therefore supports the project's goals of **reliability, maintainability, modularity, and professional software-development practices**.

---

## 11. Summary

The `tests` folder contains the automated verification layer of the Advanced Tic Tac Toe project. It uses Python's `unittest` framework together with mocking to test both backend game logic and frontend behavior without requiring every dependency to run for every test.

Each major application module has a corresponding test module, allowing problems to be isolated to specific components. Together, these tests provide confidence that the game behaves correctly, invalid input is handled properly, persistent data is managed safely, and changes to the project do not introduce unexpected regressions.

