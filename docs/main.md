# `main.py` Documentation

## 1. Purpose

The `main.py` file is the **entry point** of the Advanced Tic Tac Toe application. It is responsible for starting the application by creating the main graphical window and launching the Tkinter event loop.

The file intentionally contains very little application logic. Its purpose is to provide a clean starting point for the program while leaving the actual game and interface logic to the `game` and `ui` packages.

---

## 2. Location

```text
Advanced-Tic-Tac-Toe/
├── main.py
├── game/
├── ui/
├── tests/
├── assets/
├── data/
└── docs/
```

`main.py` is located directly in the project's root directory.

---

## 3. Role in the Project

The overall application starts through the following sequence:

```text
main.py
   ↓
main()
   ↓
MainWindow()
   ↓
UI initialization
   ↓
Game initialization
   ↓
Tkinter event loop
   ↓
Application running
```

This makes `main.py` the bridge between the Python interpreter and the application's graphical interface.

---

# 4. Import

The file imports the `MainWindow` class:

```python
from ui.main_window import MainWindow
```

`MainWindow` is responsible for constructing and controlling the application's graphical interface.

`main.py` does not directly import:

* `Board`
* `Game`
* `Player`
* `AIPlayer`
* `DialogManager`
* `GameBoard`
* `SettingsManager`
* `StatisticsManager`

Those components are initialized and managed by the appropriate classes further down the application architecture.

This keeps `main.py` simple and prevents it from becoming another application controller.

---

# 5. `main()`

The primary function in the file is:

```python
def main() -> None:
```

Its responsibility is to start the application.

Inside the function, a `MainWindow` instance is created:

```python
application = MainWindow()
```

This triggers the initialization of the application's graphical interface and its associated managers.

The application's event loop is then started:

```python
application.run()
```

The event loop keeps the Tkinter application running and allows it to respond to:

* Mouse clicks
* Button presses
* Window events
* User interactions
* UI updates
* Game actions

---

# 6. Application Startup Flow

The startup process can be represented as:

```text
Python executes main.py
        ↓
__name__ == "__main__"
        ↓
main()
        ↓
MainWindow()
        ↓
Create Tkinter root window
        ↓
Load settings/statistics
        ↓
Create Game and AI
        ↓
Create graphical widgets
        ↓
application.run()
        ↓
Tkinter mainloop()
```

Once `mainloop()` begins, control is effectively handed over to Tkinter's event-driven system.

---

# 7. Error Handling

`main()` contains exception handling around application startup and execution.

```python
try:
    application = MainWindow()
    application.run()
```

This allows the program to handle expected interruption and unexpected failures in a controlled way.

---

## 7.1 Keyboard Interrupt

The first exception handler handles `KeyboardInterrupt`:

```python
except KeyboardInterrupt:
    print(
        "\nApplication closed by user."
    )
```

This occurs when the user interrupts the Python process, such as by sending an interrupt from the terminal.

Instead of displaying a Python traceback for a normal user interruption, the application prints:

```text
Application closed by user.
```

This provides a cleaner shutdown message.

---

## 7.2 Unexpected Exceptions

The second handler catches unexpected exceptions:

```python
except Exception as error:
    print(
        "An unexpected error occurred:"
    )
    print(
        f"Error: {error}"
    )
    raise
```

The error message is displayed to the user or developer.

The exception is then re-raised using:

```python
raise
```

This is important during development because it preserves the original exception and traceback.

The program therefore does **not** silently hide programming errors.

---

# 8. `if __name__ == "__main__"`

The file contains:

```python
if __name__ == "__main__":
    main()
```

This is the standard Python entry-point pattern.

When `main.py` is executed directly:

```text
python main.py
```

Python sets:

```python
__name__ = "__main__"
```

Therefore, `main()` is called.

However, if another module imports `main.py`:

```python
from main import main
```

then `main()` is **not automatically executed**.

This distinction is important because it allows the function to be imported and tested without automatically launching the graphical application.

---

# 9. `__all__`

The file defines:

```python
__all__ = [
    "main",
]
```

This explicitly identifies `main` as the public object exposed by the module.

It communicates that the intended public functionality of `main.py` is the `main()` entry-point function.

This also keeps the file consistent with the project's other modules, which define their own `__all__` declarations.

---

# 10. Why `main.py` Is Kept Small

`main.py` deliberately does not contain game logic.

For example, it should **not** contain code for:

* Checking winners
* Managing the board
* Selecting AI moves
* Updating scores
* Displaying dialogs
* Managing settings
* Managing statistics
* Creating individual game-board buttons

Those responsibilities belong elsewhere.

The architecture is instead:

```text
main.py
   │
   ▼
MainWindow
   │
   ├── Game
   │    ├── Board
   │    ├── Player
   │    └── AI
   │         └── Minimax
   │
   ├── GameBoard
   ├── DialogManager
   ├── SettingsManager
   └── StatisticsManager
```

This separation makes the project easier to understand and maintain.

---

# 11. Relationship with `ui.main_window`

`main.py` depends directly on:

```text
ui/main_window.py
```

The relationship is one-directional:

```text
main.py
   ↓
MainWindow
```

`MainWindow` handles the actual application interface and coordinates the backend systems.

`main.py` simply starts it.

This prevents circular responsibility between the entry point and the UI controller.

---

# 12. Testing Considerations

The `main()` function can be tested independently by mocking `MainWindow`.

Potential tests can verify that:

* `MainWindow` is instantiated.
* `run()` is called.
* `KeyboardInterrupt` is handled.
* Unexpected exceptions are re-raised.

The important part is that:

```python
if __name__ == "__main__":
    main()
```

prevents the GUI from automatically launching when the module is imported by a test.

---

# 13. Running the Application

From the project's root directory, the application can be started with:

```text
python main.py
```

This executes the following:

```text
main.py
    ↓
main()
    ↓
MainWindow()
    ↓
application.run()
```

The Tkinter interface then remains active until the user closes the application.

---

# 14. Design Principles

`main.py` follows several important principles.

### Single Responsibility

The file's primary responsibility is application startup.

### Separation of Concerns

Game logic and UI implementation are handled by other modules.

### Reusability

The `main()` function can be imported without automatically starting the application.

### Error Visibility

Unexpected exceptions are re-raised instead of being silently suppressed.

### Minimalism

The entry point remains small and easy to understand.

---

# 15. Overall Responsibility

The easiest way to think about `main.py` is:

> **It starts the application, but it does not run the application logic itself.**

The file acts as the project's **launch point**.

Its complete responsibility can be summarized as:

```text
Create MainWindow
        ↓
Start application
        ↓
Handle shutdown/errors
```

Everything beyond that is delegated to the appropriate package.

---

# 16. Summary

`main.py` is the root-level entry point of Advanced Tic Tac Toe. It imports `MainWindow`, creates the main application window, and starts the Tkinter event loop through `application.run()`.

It also provides basic handling for user interruption and unexpected exceptions while preserving tracebacks for development and debugging. The `if __name__ == "__main__"` guard ensures that the application starts only when the file is executed directly.

Because the file contains no game or UI implementation itself, it remains a clean and maintainable entry point for the entire project.

