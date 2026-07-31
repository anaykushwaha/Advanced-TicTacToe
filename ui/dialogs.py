# dialogs.py 
# Contains resuable dialog windows used throughout the game application 


from tkinter import messagebox

from ui.theme import (
    GAME_OVER_TITLE,
    RESET_TITLE,
    ABOUT_TITLE,
)


class DialogManager: 
    # Collection of resable dialog windows 

    @staticmethod
    def show_game_over(message: str) -> None: 
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
            RESET_TITLE,
            (
                "Reset all scores?\n\n"
                "This cannot be undone."
            ),
        ) 

    @staticmethod
    def show_about() -> None: 
        # Displays information about the application 

        messagebox.showinfo(
            ABOUT_TITLE,
            (
                "Advanced Tic Tac Toe\n\n"
                "A polished desktop implementation of the "
                "classic Tic Tac Toe game built using Python "
                "and Tkinter.\n\n"
                "Features:\n"
                "• Human vs Human mode\n"
                "• Human vs AI mode\n"
                "• Three AI difficulty levels\n"
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

        messagebox.showinfo(
            "Statistics",
            (
                f"Player X Wins : {x_wins}\n"
                f"Player O Wins : {o_wins}\n"
                f"Draws         : {draws}\n\n"
                f"Total Games   : "
                f"{x_wins + o_wins + draws}"
            ),
        )


__all__ = [
    "DialogManager",
] 

