# test_minimax.py
# Unit tests for minimax.py

import unittest
from game.board import Board
from game.constants import (
PLAYER_X,
PLAYER_O,
)
from game.minimax import (
minimax,
find_best_move,
)

class TestMinimax(unittest.TestCase):
    # Tests the Minimax algorithm and best-move selection

    def test_minimax_ai_win(self) -> None:
        # Tests that an AI victory receives a positive score

        board = Board()

        board.set_cell(
            0,
            0,
            PLAYER_X,
        )

        board.set_cell(
            0,
            1,
            PLAYER_X,
        )

        board.set_cell(
            0,
            2,
            PLAYER_X,
        )

        score = minimax(
            board,
            PLAYER_X,
            PLAYER_O,
            True,
        )

        self.assertGreater(
            score,
            0,
        )

    def test_minimax_opponent_win(self) -> None:
        # Tests that an opponent victory receives a negative score

        board = Board()

        board.set_cell(
            1,
            0,
            PLAYER_O,
        )

        board.set_cell(
            1,
            1,
            PLAYER_O,
        )

        board.set_cell(
            1,
            2,
            PLAYER_O,
        )

        score = minimax(
            board,
            PLAYER_X,
            PLAYER_O,
            True,
        )

        self.assertLess(
            score,
            0,
        )

    def test_minimax_draw(self) -> None:
        # Tests that a drawn position receives a score of zero

        board = Board()

        moves = [
            (
                PLAYER_X,
                0,
                0,
            ),
            (
                PLAYER_O,
                0,
                1,
            ),
            (
                PLAYER_X,
                0,
                2,
            ),
            (
                PLAYER_O,
                1,
                1,
            ),
            (
                PLAYER_X,
                1,
                0,
            ),
            (
                PLAYER_O,
                1,
                2,
            ),
            (
                PLAYER_X,
                2,
                1,
            ),
            (
                PLAYER_O,
                2,
                0,
            ),
            (
                PLAYER_X,
                2,
                2,
            ),
        ]

        for symbol, row, col in moves:
            board.set_cell(
                row,
                col,
                symbol,
            )

        score = minimax(
            board,
            PLAYER_X,
            PLAYER_O,
            True,
        )

        self.assertEqual(
            score,
            0,
        )

    def test_minimax_depth_prefers_faster_win(self) -> None:
        # Tests that a faster AI victory receives a higher score

        board = Board()

        board.set_cell(
            0,
            0,
            PLAYER_X,
        )

        board.set_cell(
            0,
            1,
            PLAYER_X,
        )

        score = minimax(
            board,
            PLAYER_X,
            PLAYER_O,
            True,
            depth=1,
        )

        self.assertGreater(
            score,
            0,
        )

    def test_find_best_move_returns_none_on_full_board(
        self,
    ) -> None:
        # Tests that no move is returned when the board is full

        board = Board()

        moves = [
            (
                PLAYER_X,
                0,
                0,
            ),
            (
                PLAYER_O,
                0,
                1,
            ),
            (
                PLAYER_X,
                0,
                2,
            ),
            (
                PLAYER_O,
                1,
                0,
            ),
            (
                PLAYER_X,
                1,
                1,
            ),
            (
                PLAYER_O,
                1,
                2,
            ),
            (
                PLAYER_O,
                2,
                0,
            ),
            (
                PLAYER_X,
                2,
                1,
            ),
            (
                PLAYER_O,
                2,
                2,
            ),
        ]

        for symbol, row, col in moves:
            board.set_cell(
                row,
                col,
                symbol,
            )

        move = find_best_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )

        self.assertIsNone(
            move,
        )

    def test_find_best_move_takes_winning_move(
        self,
    ) -> None:
        # Tests that the AI chooses an immediate winning move

        board = Board()

        board.set_cell(
            0,
            0,
            PLAYER_X,
        )

        board.set_cell(
            0,
            1,
            PLAYER_X,
        )

        board.set_cell(
            1,
            0,
            PLAYER_O,
        )

        board.set_cell(
            1,
            1,
            PLAYER_O,
        )

        move = find_best_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )

        self.assertEqual(
            move,
            (
                0,
                2,
            ),
        )

    def test_find_best_move_blocks_opponent(
        self,
    ) -> None:
        # Tests that the AI blocks an immediate opponent victory

        board = Board()

        board.set_cell(
            0,
            0,
            PLAYER_O,
        )

        board.set_cell(
            0,
            1,
            PLAYER_O,
        )

        board.set_cell(
            1,
            0,
            PLAYER_X,
        )

        move = find_best_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )

        self.assertEqual(
            move,
            (
                0,
                2,
            ),
        )

    def test_find_best_move_returns_legal_move(
        self,
    ) -> None:
        # Tests that the selected move is available on the board

        board = Board()

        board.set_cell(
            0,
            0,
            PLAYER_X,
        )

        board.set_cell(
            1,
            1,
            PLAYER_O,
        )

        move = find_best_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )

        self.assertIsNotNone(
            move,
        )

        self.assertIn(
            move,
            board.get_available_moves(),
        )

    def test_find_best_move_does_not_modify_board(
        self,
    ) -> None:
        # Tests that finding a move leaves the board unchanged

        board = Board()

        board.set_cell(
            0,
            0,
            PLAYER_X,
        )

        board.set_cell(
            1,
            1,
            PLAYER_O,
        )

        original_board = board.get_board()

        find_best_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )

        self.assertEqual(
            board.get_board(),
            original_board,
        )

if __name__ == "__main__":
    unittest.main()

__all__ = [
    "TestMinimax",
] 

