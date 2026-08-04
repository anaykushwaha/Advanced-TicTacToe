# dialogs.py
# Contains reusable dialog windows used throughout the game application

from tkinter import messagebox

from ui.theme import (
    GAME_OVER_TITLE,
    RESET_TITLE,
    ABOUT_TITLE,
    STATISTICS_TITLE,
    CONFIRM_EXIT_TITLE,
    CONFIRM_RESET_TITLE,
)


class DialogManager:
    # Collection of reusable dialog windows

    @staticmethod
    def show_game_over(
        message: str,
    ) -> None:
        # Displays the final game result

        messagebox.showinfo(
            GAME_OVER_TITLE,
            message,
        )

    @staticmethod
    def ask_new_game() -> bool:
        # Asks the user whether they would like to start another game

        return messagebox.askyesno(
            GAME_OVER_TITLE,
            "Would you like to play again?",
        )

    @staticmethod
    def confirm_reset_scores() -> bool:
        # Asks the user to confirm that all scores should be reset

        return messagebox.askyesno(
            CONFIRM_RESET_TITLE,
            (
                "Reset all scores?\n\n"
                "This action cannot be undone."
            ),
        )

    @staticmethod
    def confirm_exit() -> bool:
        # Asks the user to confirm before closing the application

        return messagebox.askyesno(
            CONFIRM_EXIT_TITLE,
            (
                "Are you sure you want to exit "
                "the game?"
            ),
        )

    @staticmethod
    def show_about() -> None:
        # Displays information about the application

        messagebox.showinfo(
            ABOUT_TITLE,
            (
                "Advanced Tic Tac Toe\n\n"
                "Version 1.0\n\n"
                "A polished desktop implementation of "
                "the classic Tic Tac Toe game built "
                "using Python and Tkinter.\n\n"
                "Features:\n"
                "• Human vs Human mode\n"
                "• Human vs AI mode\n"
                "• Three AI difficulty levels\n"
                "• Persistent settings\n"
                "• Persistent statistics\n"
                "• Score tracking\n"
                "• Clean graphical interface"
            ),
        )

    @staticmethod
    def show_statistics(
        x_wins: int,
        o_wins: int,
        draws: int,
    ) -> None:
        # Displays the current match statistics

        total_games = (
            x_wins
            + o_wins
            + draws
        )

        messagebox.showinfo(
            STATISTICS_TITLE,
            (
                f"Games Played : "
                f"{total_games}\n\n"
                f"Player X Wins : "
                f"{x_wins}\n"
                f"Player O Wins : "
                f"{o_wins}\n"
                f"Draws         : "
                f"{draws}"
            ),
        )

    @staticmethod
    def show_information(
        title: str,
        message: str,
    ) -> None:
        # Displays an informational dialog

        messagebox.showinfo(
            title,
            message,
        )

    @staticmethod
    def show_warning(
        title: str,
        message: str,
    ) -> None:
        # Displays a warning dialog

        messagebox.showwarning(
            title,
            message,
        )

    @staticmethod
    def show_error(
        title: str,
        message: str,
    ) -> None:
        # Displays an error dialog

        messagebox.showerror(
            title,
            message,
        )


__all__ = [
    "DialogManager",
] 

