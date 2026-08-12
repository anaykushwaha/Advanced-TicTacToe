# test_dialogs.py
# Unit tests for dialogs.py

from unittest.mock import patch, Mock 
from ui.dialogs import DialogManager
from ui.theme import (
    ABOUT_TITLE,
    CONFIRM_EXIT_TITLE,
    CONFIRM_RESET_TITLE,
    GAME_OVER_TITLE,
    STATISTICS_TITLE,
)


class TestDialogManager:
    # Tests for the DialogManager class

    @patch("ui.dialogs.messagebox.showinfo")
    def test_show_game_over(self, mock_showinfo):
        # Tests the game over dialog

        DialogManager.show_game_over(
            "Player X Wins!",
        )

        mock_showinfo.assert_called_once_with(
            GAME_OVER_TITLE,
            "Player X Wins!",
        )

    @patch("ui.dialogs.messagebox.askyesno")
    def test_ask_new_game_yes(self, mock_askyesno):
        # Tests accepting a new game

        mock_askyesno.return_value = True

        result = DialogManager.ask_new_game()

        assert result is True

        mock_askyesno.assert_called_once_with(
            GAME_OVER_TITLE,
            "Would you like to play again?",
        )

    @patch("ui.dialogs.messagebox.askyesno")
    def test_ask_new_game_no(self, mock_askyesno):
        # Tests declining a new game

        mock_askyesno.return_value = False

        result = DialogManager.ask_new_game()

        assert result is False

        mock_askyesno.assert_called_once_with(
            GAME_OVER_TITLE,
            "Would you like to play again?",
        )

    @patch("ui.dialogs.messagebox.askyesno")
    def test_confirm_reset_scores(self, mock_askyesno):
        # Tests the reset confirmation dialog

        mock_askyesno.return_value = True

        result = DialogManager.confirm_reset_scores()

        assert result is True

        mock_askyesno.assert_called_once_with(
            CONFIRM_RESET_TITLE,
            (
                "Reset all scores?\n\n"
                "This action cannot be undone."
            ),
        )

    @patch("ui.dialogs.messagebox.askyesno")
    def test_confirm_exit(self, mock_askyesno):
        # Tests the exit confirmation dialog

        mock_askyesno.return_value = False
        result = DialogManager.confirm_exit()
        assert result is False

        mock_askyesno.assert_called_once_with(
            CONFIRM_EXIT_TITLE,
            (
                "Are you sure you want to exit "
                "the game?"
            ),
        )

    @patch("ui.dialogs.messagebox.showinfo")
    def test_show_about(self, mock_showinfo):
        # Tests the about dialog

        DialogManager.show_about()

        mock_showinfo.assert_called_once()
        args = mock_showinfo.call_args[0]

        assert args[0] == ABOUT_TITLE
        assert "Advanced Tic Tac Toe" in args[1]
        assert "Version 1.0" in args[1]

    @patch("ui.dialogs.messagebox.showinfo")
    def test_show_statistics(self, mock_showinfo):
        # Tests the statistics dialog

        DialogManager.show_statistics(
            5,
            3,
            2,
        )

        mock_showinfo.assert_called_once()
        args = mock_showinfo.call_args[0]

        assert args[0] == STATISTICS_TITLE
        assert "Games Played : 10" in args[1]
        assert "Player X Wins : 5" in args[1]
        assert "Player O Wins : 3" in args[1]
        assert "Draws         : 2" in args[1]

    @patch("ui.dialogs.messagebox.showinfo")
    def test_show_information(self, mock_showinfo):
        # Tests a generic information dialog

        DialogManager.show_information(
            "Information",
            "Operation completed.",
        )

        mock_showinfo.assert_called_once_with(
            "Information",
            "Operation completed.",
        )

    @patch("ui.dialogs.messagebox.showwarning")
    def test_show_warning(self, mock_showwarning):
        # Tests a generic warning dialog

        DialogManager.show_warning(
            "Warning",
            "Invalid move.",
        )

        mock_showwarning.assert_called_once_with(
            "Warning",
            "Invalid move.",
        )

    @patch("ui.dialogs.messagebox.showerror")
    def test_show_error(self, mock_showerror):
        # Tests a generic error dialog

        DialogManager.show_error(
            "Error",
            "Unexpected error.",
        )

        mock_showerror.assert_called_once_with(
            "Error",
            "Unexpected error.",
        )

__all__ = [
    "TestDialogManager",
] 

