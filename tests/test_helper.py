# test_helper.py
# Unit tests for helper.py

import unittest
from pathlib import Path
from game.constants import (
    BOARD_SIZE,
    EMPTY_CELL,
    PLAYER_X,
    PLAYER_O,
)
from game.helper import (
    create_empty_board,
    get_available_moves,
    is_board_full,
    format_time,
    get_project_root,
    clamp,
    opposite_player,
)


class TestHelper(unittest.TestCase):
    # Tests the helper functions

    def test_create_empty_board(self) -> None:
        # Tests creating an empty board

        board = create_empty_board()
        self.assertEqual(
            len(board),
            BOARD_SIZE,
        )
        for row in board:
            self.assertEqual(
                len(row),
                BOARD_SIZE,
            )
            for cell in row:
                self.assertEqual(
                    cell,
                    EMPTY_CELL,
                )

    def test_get_available_moves_empty_board(self) -> None:
        # Tests available moves on an empty board

        board = create_empty_board()
        moves = get_available_moves(
            board,
        )
        self.assertEqual(
            len(moves),
            BOARD_SIZE * BOARD_SIZE,
        )

    def test_get_available_moves_partial_board(self) -> None:
        # Tests available moves on a partially filled board

        board = create_empty_board()
        board[0][0] = PLAYER_X
        board[1][1] = PLAYER_O
        moves = get_available_moves(
            board,
        )
        self.assertEqual(
            len(moves),
            7,
        )
        self.assertNotIn(
            (
                0,
                0,
            ),
            moves,
        )
        self.assertNotIn(
            (
                1,
                1,
            ),
            moves,
        )

    def test_is_board_full_false(self) -> None:
        # Tests a board that is not full

        board = create_empty_board()
        self.assertFalse(
            is_board_full(
                board,
            ),
        )

    def test_is_board_full_true(self) -> None:
        # Tests a completely filled board

        board = [
            [
                PLAYER_X,
                PLAYER_O,
                PLAYER_X,
            ],
            [
                PLAYER_O,
                PLAYER_X,
                PLAYER_O,
            ],
            [
                PLAYER_O,
                PLAYER_X,
                PLAYER_O,
            ],
        ]
        self.assertTrue(
            is_board_full(
                board,
            ),
        )

    def test_format_time(self) -> None:
        # Tests formatting time

        self.assertEqual(
            format_time(
                0,
            ),
            "00:00",
        )
        self.assertEqual(
            format_time(
                65,
            ),
            "01:05",
        )
        self.assertEqual(
            format_time(
                600,
            ),
            "10:00",
        )

    def test_get_project_root(self) -> None:
        # Tests retrieving the project root

        root = get_project_root()
        self.assertIsInstance(
            root,
            Path,
        )
        self.assertTrue(
            root.exists(),
        )

    def test_clamp_inside_range(self) -> None:
        # Tests a value already inside the range

        self.assertEqual(
            clamp(
                5,
                0,
                10,
            ),
            5,
        )

    def test_clamp_below_range(self) -> None:
        # Tests a value below the range

        self.assertEqual(
            clamp(
                -5,
                0,
                10,
            ),
            0,
        )

    def test_clamp_above_range(self) -> None:
        # Tests a value above the range

        self.assertEqual(
            clamp(
                15,
                0,
                10,
            ),
            10,
        )

    def test_opposite_player(self) -> None:
        # Tests retrieving the opposite player

        self.assertEqual(
            opposite_player(
                PLAYER_X,
            ),
            PLAYER_O,
        )
        self.assertEqual(
            opposite_player(
                PLAYER_O,
            ),
            PLAYER_X,
        )


__all__ = [
    "TestHelper",
]

if __name__ == "__main__":
    unittest.main() 

