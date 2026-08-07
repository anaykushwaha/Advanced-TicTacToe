# test_board.py
# Unit tests for the Board class

import unittest
from game.board import Board
from game.constants import (
    BOARD_SIZE,
    EMPTY_CELL,
    PLAYER_X,
    PLAYER_O,
)


class TestBoard(unittest.TestCase):
    # Tests the Board class

    def setUp(self) -> None: 
        # Creates a fresh board before every test

        self.board = Board()

    def test_board_starts_empty(self) -> None: 
        # Tests that a new board is empty

        for row in self.board.get_board():
            for cell in row:
                self.assertEqual(
                    cell,
                    EMPTY_CELL,
                )

    def test_reset_clears_board(self) -> None: 
        # Tests that reset clears every cell

        self.board.place_move(
            0,
            0,
            PLAYER_X,
        )
        self.board.reset()
        for row in self.board.get_board():
            for cell in row:
                self.assertEqual(
                    cell,
                    EMPTY_CELL,
                )

    def test_get_board_returns_copy(self) -> None: 
        # Tests that get_board returns a copy

        board_copy = self.board.get_board()
        board_copy[0][0] = PLAYER_X
        self.assertEqual(
            self.board.get_cell(
                0,
                0,
            ),
            EMPTY_CELL,
        )

    def test_is_cell_empty(self) -> None: 
        # Tests empty cell detection

        self.assertTrue(
            self.board.is_cell_empty(
                1,
                1,
            )
        )
        self.board.place_move(
            1,
            1,
            PLAYER_X,
        )
        self.assertFalse(
            self.board.is_cell_empty(
                1,
                1,
            )
        )

    def test_invalid_position_not_empty(self) -> None: 
        # Tests invalid positions

        self.assertFalse(
            self.board.is_cell_empty(
                -1,
                5,
            )
        )

    def test_valid_move(self) -> None: 
        # Tests move validation

        self.assertTrue(
            self.board.is_valid_move(
                0,
                0,
            )
        )
        self.board.place_move(
            0,
            0,
            PLAYER_X,
        )
        self.assertFalse(
            self.board.is_valid_move(
                0,
                0,
            )
        )

    def test_place_move(self) -> None: 
        # Tests placing a valid move

        self.assertTrue(
            self.board.place_move(
                0,
                0,
                PLAYER_X,
            )
        )
        self.assertEqual(
            self.board.get_cell(
                0,
                0,
            ),
            PLAYER_X,
        )

    def test_invalid_symbol(self) -> None: 
        # Tests invalid player symbol

        self.assertFalse(
            self.board.place_move(
                0,
                0,
                "Z",
            )
        )

    def test_set_and_get_cell(self) -> None: 
        # Tests setting and retrieving cells

        self.board.set_cell(
            2,
            2,
            PLAYER_O,
        )
        self.assertEqual(
            self.board.get_cell(
                2,
                2,
            ),
            PLAYER_O,
        )

    def test_clear_cell(self) -> None: 
        # Tests clearing a cell

        self.board.set_cell(
            0,
            1,
            PLAYER_X,
        )
        self.board.clear_cell(
            0,
            1,
        )
        self.assertEqual(
            self.board.get_cell(
                0,
                1,
            ),
            EMPTY_CELL,
        )

    def test_invalid_set_cell_position(self) -> None: 
        # Tests invalid board position

        with self.assertRaises(
            ValueError,
        ):
            self.board.set_cell(
                -1,
                0,
                PLAYER_X,
            )

    def test_invalid_set_cell_value(self) -> None: 
        # Tests invalid board value

        with self.assertRaises(
            ValueError,
        ):
            self.board.set_cell(
                0,
                0,
                "A",
            )

    def test_available_moves(self) -> None: 
        # Tests available move count

        self.assertEqual(
            len(
                self.board.get_available_moves()
            ),
            BOARD_SIZE * BOARD_SIZE,
        )
        self.board.place_move(
            0,
            0,
            PLAYER_X,
        )
        self.assertEqual(
            len(
                self.board.get_available_moves()
            ),
            BOARD_SIZE * BOARD_SIZE - 1,
        )

    def test_is_full(self) -> None: 
        # Tests board full detection

        symbol = PLAYER_X
        for row in range(
            BOARD_SIZE,
        ):
            for col in range(
                BOARD_SIZE,
            ):
                self.board.place_move(
                    row,
                    col,
                    symbol,
                )
                symbol = (
                    PLAYER_O
                    if symbol == PLAYER_X
                    else PLAYER_X
                )
        self.assertTrue(
            self.board.is_full()
        )

    def test_row_win(self) -> None: 
        # Tests row winner detection

        for col in range(
            BOARD_SIZE,
        ):
            self.board.place_move(
                0,
                col,
                PLAYER_X,
            )
        self.assertEqual(
            self.board.check_winner(),
            PLAYER_X,
        )

    def test_column_win(self) -> None: 
        # Tests column winner detection

        for row in range(
            BOARD_SIZE,
        ):
            self.board.place_move(
                row,
                1,
                PLAYER_O,
            )
        self.assertEqual(
            self.board.check_winner(),
            PLAYER_O,
        )

    def test_main_diagonal_win(self) -> None: 
        # Tests main diagonal winner

        for i in range(
            BOARD_SIZE,
        ):
            self.board.place_move(
                i,
                i,
                PLAYER_X,
            )
        self.assertEqual(
            self.board.check_winner(),
            PLAYER_X,
        )

    def test_secondary_diagonal_win(self) -> None: 
        # Tests secondary diagonal winner

        for i in range(
            BOARD_SIZE,
        ):
            self.board.place_move(
                i,
                BOARD_SIZE - 1 - i,
                PLAYER_O,
            )
        self.assertEqual(
            self.board.check_winner(),
            PLAYER_O,
        )

    def test_no_winner(self) -> None: 
        # Tests unfinished game

        self.assertIsNone(
            self.board.check_winner()
        )

    def test_get_winning_positions(self) -> None: 
        # Tests winning coordinate detection

        for col in range(
            BOARD_SIZE,
        ):
            self.board.place_move(
                0,
                col,
                PLAYER_X,
            )
        self.assertEqual(
            self.board.get_winning_positions(),
            [
                (0, 0),
                (0, 1),
                (0, 2),
            ],
        )

    def test_no_winning_positions(self) -> None: 
        # Tests no winning coordinates

        self.assertEqual(
            self.board.get_winning_positions(),
            [],
        )

    def test_draw(self) -> None: 
        # Tests draw detection

        moves = [
            (0, 0, PLAYER_X),
            (0, 1, PLAYER_O),
            (0, 2, PLAYER_X),

            (1, 0, PLAYER_X),
            (1, 1, PLAYER_O),
            (1, 2, PLAYER_O),

            (2, 0, PLAYER_O),
            (2, 1, PLAYER_X),
            (2, 2, PLAYER_X),
        ]

        for row, col, symbol in moves:
            self.board.place_move(
                row,
                col,
                symbol,
            )
        self.assertTrue(
            self.board.is_draw()
        )

    def test_string_representation(self) -> None: 
        # Tests string conversion

        text = str(
            self.board,
        )
        self.assertIsInstance(
            text,
            str,
        )
        self.assertGreater(
            len(text),
            0,
        )


if __name__ == "__main__":
    unittest.main() 

