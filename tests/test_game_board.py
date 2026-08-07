# test_game_board.py
# Unit tests for game_board.py

import tkinter as tk
import unittest
from unittest.mock import patch, Mock 
from ui.game_board import GameBoard
from ui.theme import (
    BOARD_SIZE,
    BUTTON_COLOR,
    EMPTY_STRING,
    WIN_HIGHLIGHT_COLOR,
)


class TestGameBoard(unittest.TestCase):
    # Tests the GameBoard class

    def setUp(self) -> None:
        # Creates a test window and board

        self.root = tk.Tk()
        self.root.withdraw()
        self.clicked_position = None
        self.game_board = GameBoard(
            self.root,
            self._cell_clicked,
        )

    def tearDown(self) -> None:
        # Closes the test window

        self.root.destroy()

    def _cell_clicked(
        self,
        row: int,
        col: int,
    ) -> None:
        # Records the clicked position

        self.clicked_position = (
            row,
            col,
        )

    def test_board_creation(self) -> None:
        # Tests that a 3x3 board is created

        self.assertEqual(
            len(self.game_board.buttons),
            BOARD_SIZE,
        )
        for row in self.game_board.buttons:
            self.assertEqual(
                len(row),
                BOARD_SIZE,
            )

    def test_update_cell(self) -> None:
        # Tests updating a board cell

        self.game_board.update_cell(
            0,
            0,
            "X",
            "blue",
        )
        button = self.game_board.get_button(
            0,
            0,
        )
        self.assertEqual(
            button["text"],
            "X",
        )
        self.assertEqual(
            button["fg"],
            "blue",
        )
        self.assertEqual(
            str(button["state"]),
            "disabled",
        )

    def test_clear_board(self) -> None:
        # Tests clearing the board

        self.game_board.update_cell(
            0,
            0,
            "X",
            "blue",
        )
        self.game_board.clear_board()
        for row in self.game_board.buttons:
            for button in row:
                self.assertEqual(
                    button["text"],
                    EMPTY_STRING,
                )
                self.assertEqual(
                    button["bg"],
                    BUTTON_COLOR,
                )
                self.assertEqual(
                    str(button["state"]),
                    "normal",
                )

    def test_enable_cell(self) -> None:
        # Tests enabling a cell

        self.game_board.disable_cell(
            1,
            1,
        )
        self.game_board.enable_cell(
            1,
            1,
        )
        button = self.game_board.get_button(
            1,
            1,
        )
        self.assertEqual(
            str(button["state"]),
            "normal",
        )

    def test_disable_cell(self) -> None:
        # Tests disabling a cell

        self.game_board.disable_cell(
            2,
            2,
        )
        button = self.game_board.get_button(
            2,
            2,
        )
        self.assertEqual(
            str(button["state"]),
            "disabled",
        )

    def test_enable_board(self) -> None:
        # Tests enabling the board

        self.game_board.disable_board()
        self.game_board.enable_board()
        for row in self.game_board.buttons:
            for button in row:
                self.assertEqual(
                    str(button["state"]),
                    "normal",
                )

    def test_disable_board(self) -> None:
        # Tests disabling the board

        self.game_board.disable_board()
        for row in self.game_board.buttons:
            for button in row:
                self.assertEqual(
                    str(button["state"]),
                    "disabled",
                )

    @patch(
        "ui.game_board.AnimationManager.flash_winning_cells"
    )
    def test_highlight_cells(
        self,
        mock_flash,
    ) -> None:
        # Tests highlighting winning cells

        winning_positions = [
            (
                0,
                0,
            ),
            (
                0,
                1,
            ),
            (
                0,
                2,
            ),
        ]
        self.game_board.highlight_cells(
            winning_positions,
        )
        for row, col in winning_positions:
            button = self.game_board.get_button(
                row,
                col,
            )
            self.assertEqual(
                button["bg"],
                WIN_HIGHLIGHT_COLOR,
            )
        mock_flash.assert_called_once()

    def test_reset_cell_colors(self) -> None:
        # Tests resetting cell colours

        button = self.game_board.get_button(
            0,
            0,
        )
        button.configure(
            bg="red",
        )
        self.game_board.reset_cell_colors()
        self.assertEqual(
            button["bg"],
            BUTTON_COLOR,
        )

    def test_get_button(self) -> None:
        # Tests retrieving a button

        button = self.game_board.get_button(
            1,
            2,
        )
        self.assertIsInstance(
            button,
            tk.Button,
        )

    def test_get_button_invalid_position(self) -> None:
        # Tests requesting an invalid button

        with self.assertRaises(
            IndexError,
        ):
            self.game_board.get_button(
                -1,
                0,
            )
        with self.assertRaises(
            IndexError,
        ):
            self.game_board.get_button(
                3,
                3,
            )


__all__ = [
    "TestGameBoard",
]

if __name__ == "__main__": 
    unittest.main() 

