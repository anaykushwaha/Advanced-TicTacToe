# main.py
# Entry point for the Advanced Tic Tac Toe application.
# Creates the main window and starts the Tkinter event loop.

from ui.main_window import MainWindow

def main() -> None:
    # Starts the application

    try:
        application = MainWindow()
        application.run()

    except KeyboardInterrupt:
        print("\nApplication closed by user")

    except Exception as error:
        print("An unexpected error occurred:")
        print(error)
        raise


if __name__ == "__main__":
    main()


__all__ = [
    "main",
]

