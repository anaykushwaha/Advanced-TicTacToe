# Data Folder Documentation

## 1. Purpose

The `data` folder contains the **persistent data files** used by the Advanced Tic Tac Toe application. These files allow information such as application settings and gameplay statistics to remain available even after the program is closed.

The `data` directory is intentionally separate from the application's Python source code. The `game` package contains the logic responsible for managing this information, while the `data` folder contains the actual stored data.

---

## 2. Role in the Project

The `data` folder acts as the application's **persistent storage location**.

It is used to store information that needs to survive between application sessions, such as:

* User settings
* AI configuration
* Theme preferences
* Sound preferences
* Animation preferences
* Game statistics
* Number of games played
* X wins
* O wins
* AI wins
* Draws

The folder therefore provides persistence without requiring a database.

---

## 3. Typical Directory Structure

The project's data directory is structured approximately as follows:

```text
data/
├── settings.json
└── statistics.json
```

The exact files present may depend on whether the application has already been run.

The application automatically creates the necessary JSON files if they do not exist.

---

## 4. `settings.json`

`settings.json` stores the user's application configuration.

The file is managed by the `SettingsManager` class in:

```text
game/settings.py
```

The UI does not directly manipulate `settings.json`. Instead, the application goes through `SettingsManager`, which validates and saves settings before writing them to disk.

### Stored settings

The settings file contains values such as:

```json
{
    "theme": "Light",
    "ai_enabled": false,
    "difficulty": "Medium",
    "sound_enabled": true,
    "animations_enabled": true
}
```

These values control how the application behaves.

### `theme`

Determines the selected visual theme.

Example:

```text
Light
```

The value is validated against the supported themes defined in the project's constants.

### `ai_enabled`

Determines whether the game should operate in AI mode.

Possible values:

```text
true
false
```

### `difficulty`

Determines the AI difficulty level.

For example:

```text
Easy
Medium
Impossible
```

The exact supported values are defined by `AI_DIFFICULTIES` in `game/constants.py`.

### `sound_enabled`

Determines whether sound functionality is enabled.

### `animations_enabled`

Determines whether graphical animations are enabled.

---

## 5. `statistics.json`

`statistics.json` stores persistent gameplay statistics.

It is managed by:

```text
game/statistics.py
```

The `StatisticsManager` class handles loading, modifying, validating, and saving these statistics.

A newly initialized statistics file contains values similar to:

```json
{
    "games_played": 0,
    "x_wins": 0,
    "o_wins": 0,
    "ai_wins": 0,
    "draws": 0
}
```

### `games_played`

Stores the total number of completed games.

This value increases whenever a game ends with either:

* A player victory
* A draw

### `x_wins`

Stores the number of games won by Player X.

### `o_wins`

Stores the number of games won by Player O in non-AI games.

### `ai_wins`

Stores the number of games won by the AI.

### `draws`

Stores the number of completed games that ended in a draw.

---

## 6. JSON as the Storage Format

The project uses **JSON** for persistent application data.

JSON was selected because it is:

* Lightweight
* Human-readable
* Easy to edit
* Native to Python through the `json` module
* Appropriate for the relatively small amount of data used by the application
* Easy to validate
* Easy to back up or reset

The application does not require a database for its current scope.

---

## 7. Relationship with `FileManager`

The `data` folder is closely connected to:

```text
game/file_manager.py
```

The `FileManager` class provides the low-level file operations required by the application.

It handles operations such as:

* Creating directories
* Creating missing JSON files
* Loading JSON
* Saving JSON
* Resetting JSON files
* Checking whether files exist
* Deleting files

The managers responsible for settings and statistics use `FileManager` rather than directly implementing their own file-handling logic.

The relationship can be represented as:

```text
SettingsManager
       │
       ▼
 FileManager
       │
       ▼
settings.json
```

and:

```text
StatisticsManager
       │
       ▼
 FileManager
       │
       ▼
statistics.json
```

This keeps file-handling logic centralized.

---

## 8. Automatic File Creation

The application does not require the user to manually create the JSON files.

When `SettingsManager` or `StatisticsManager` starts, it checks whether the appropriate file exists.

If the file does not exist, `FileManager.create_file_if_missing()` creates it using the appropriate default data.

For example:

```text
Application starts
        ↓
SettingsManager initializes
        ↓
Check settings.json
        ↓
File missing?
        ↓
Create file using default settings
```

The same process occurs for `statistics.json`.

This makes the application easier to distribute because a fresh installation does not need pre-created data files.

---

## 9. Data Validation

Persistent data should not automatically be trusted.

The project therefore validates loaded JSON before accepting it as valid application data.

Settings are validated using:

```text
validate_settings()
```

Statistics are validated using:

```text
validate_statistics()
```

Both functions are located in:

```text
game/validator.py
```

This provides a safety layer between the JSON files and the rest of the application.

---

## 10. Invalid Settings Data

If `settings.json` contains invalid data, `SettingsManager` does not simply continue using the corrupted information.

Instead, it restores the default settings.

Examples of invalid data include:

* Missing required keys
* Extra unexpected keys
* Invalid theme values
* Invalid difficulty values
* Non-boolean AI settings
* Non-boolean sound settings
* Non-boolean animation settings

The general flow is:

```text
Load settings.json
        ↓
Validate settings
        ↓
Valid?
   ↙        ↘
 Yes         No
 ↓           ↓
Use data   Restore defaults
```

---

## 11. Invalid Statistics Data

The same principle applies to `statistics.json`.

Statistics are expected to contain a specific set of keys:

```text
games_played
x_wins
o_wins
ai_wins
draws
```

Each value must be a non-negative integer.

Invalid examples include:

```json
{
    "games_played": -5
}
```

or:

```json
{
    "games_played": "ten"
}
```

or a file missing required statistics.

If validation fails, the application restores the default statistics.

---

## 12. Resetting Data

The project provides mechanisms for restoring stored information to its default state.

For settings, `SettingsManager.reset_defaults()` restores the default configuration.

For statistics, `StatisticsManager.reset_statistics()` resets all statistics to zero.

This is useful when:

* Data becomes corrupted
* A user wants to start over
* Testing requires a clean state
* Development requires resetting application data

---

## 13. Persistence Between Sessions

One of the primary purposes of the `data` folder is allowing the application to maintain information between executions.

For example:

### First session

```text
Player wins 5 games
        ↓
statistics.json
        ↓
x_wins = 5
```

The application closes.

### Second session

```text
Application starts
        ↓
StatisticsManager loads statistics.json
        ↓
x_wins = 5
```

The previous statistics remain available.

The same principle applies to user settings.

---

## 14. Data Flow

The overall data flow can be represented as:

```text
                 Application
                      │
          ┌───────────┴───────────┐
          │                       │
          ▼                       ▼
 SettingsManager          StatisticsManager
          │                       │
          └───────────┬───────────┘
                      │
                      ▼
                 FileManager
                      │
             ┌────────┴────────┐
             │                 │
             ▼                 ▼
       settings.json     statistics.json
```

This architecture keeps persistent storage separate from the rest of the project.

---

## 15. Data and the `MainWindow`

The graphical application accesses persistent data indirectly through the managers.

`MainWindow` creates:

```python
SettingsManager()
```

and:

```python
StatisticsManager()
```

These managers then load the relevant files.

During application execution:

```text
MainWindow
     ↓
SettingsManager / StatisticsManager
     ↓
FileManager
     ↓
JSON files
```

When the application closes, `MainWindow.exit_application()` saves the current settings and statistics before destroying the Tkinter window.

---

## 16. Why the Data Folder Is Separate

Keeping persistent data outside the source-code packages provides several advantages.

### Separation of concerns

Python source files remain separate from runtime-generated data.

### Easier maintenance

Developers can inspect or reset stored data without modifying application code.

### Cleaner project structure

The `game` and `ui` directories contain program logic, while `data` contains application state.

### Easier backups

Important persistent information can be backed up independently.

### Easier testing

Tests can use temporary files and directories without modifying the project's normal persistent data.

---

## 17. Relationship with `.gitignore`

The `data` directory requires special consideration when using Git.

Persistent runtime data can change whenever the application is executed. Depending on the project's intended behavior, generated JSON files may be excluded from version control.

For example:

```text
data/*.json
```

could be added to `.gitignore` if the project treats these files as local runtime data.

Alternatively, default JSON files can be committed if the repository is intended to provide initial example data.

The important distinction is between:

* **Source/default data** that belongs in the repository
* **User-generated runtime data** that should generally remain local

The project should use one consistent approach.

---

## 18. Testing Data Operations

The functionality associated with the `data` folder is primarily tested through the `tests` directory.

Relevant tests include:

```text
tests/
├── test_file_manager.py
├── test_settings.py
└── test_statistics.py
```

These tests verify that the application can correctly:

* Create missing files
* Read JSON data
* Write JSON data
* Reset data
* Delete files
* Detect existing files
* Load valid settings
* Reject invalid settings
* Load valid statistics
* Reject invalid statistics
* Record wins
* Record draws
* Reset statistics

Tests should preferably use temporary directories or mocked file operations so that automated tests do not corrupt the project's real application data.

---

## 19. Security and Reliability Considerations

The current application uses local JSON files rather than a remote server or database.

Because the data is local, the primary concerns are:

* Invalid JSON
* Missing files
* Incorrect data types
* Accidental deletion
* Unexpected manual modifications
* Runtime file errors

The project's validation and file-management layers help mitigate these issues.

However, JSON files should still be treated as persistent application state rather than immutable source code.

---

## 20. Future Expansion

The `data` directory can be expanded if the application gains additional persistent features.

Possible future files could include:

```text
data/
├── settings.json
├── statistics.json
├── profiles.json
├── achievements.json
└── game_history.json
```

For example, a future `game_history.json` could store:

* Match dates
* Players
* Game results
* AI difficulty
* Winning moves
* Draws

A future version could also migrate from JSON to a database such as SQLite if the amount of persistent data becomes significantly larger.

For the current project, JSON is appropriately simple and sufficient.

---

## 21. Design Principles

The data system follows several important design principles.

### Centralized file handling

`FileManager` provides reusable low-level file operations.

### Validation before use

Loaded data is validated before being accepted by the application.

### Default recovery

Invalid or missing data can be replaced with safe default values.

### Separation of responsibilities

The data files store information, while the managers determine how that information is interpreted and modified.

### Persistence

Important application information survives program restarts.

### Simplicity

JSON provides an appropriate storage solution without introducing unnecessary database complexity.

---

## 22. Summary

The `data` folder is the **persistent storage layer** of Advanced Tic Tac Toe.

It stores runtime information in JSON files while keeping those files separate from the application's Python source code.

The major components involved are:

* `settings.json` — stores user/application settings.
* `statistics.json` — stores persistent gameplay statistics.
* `FileManager` — performs low-level JSON file operations.
* `SettingsManager` — manages settings.
* `StatisticsManager` — manages statistics.
* `validator.py` — validates loaded data.

The overall design provides a simple but effective persistence system:

```text
Application
     ↓
Managers
     ↓
Validation + FileManager
     ↓
JSON Data
```

This keeps persistent data organized, validated, reusable, and independent from the core game and UI logic.


