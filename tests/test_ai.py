# test_ai.py
# Unit tests for the AIPlayer class

import unittest
from game.ai import AIPlayer
from game.board import Board
from game.constants import (
    AI_EASY,
    AI_MEDIUM,
    AI_IMPOSSIBLE,
    PLAYER_X,
    PLAYER_O,
)


class TestAIPlayer(unittest.TestCase):
    # Tests the AIPlayer class

    def test_default_difficulty(self) -> None:
        # Tests the default AI difficulty

        ai = AIPlayer()
        self.assertEqual(
            ai.get_difficulty(),
            AI_MEDIUM,
        )

    def test_set_easy_difficulty(self) -> None:
        # Tests setting Easy difficulty

        ai = AIPlayer()
        ai.set_difficulty(
            AI_EASY,
        )
        self.assertEqual(
            ai.get_difficulty(),
            AI_EASY,
        )

    def test_set_medium_difficulty(self) -> None:
        # Tests setting Medium difficulty

        ai = AIPlayer()
        ai.set_difficulty(
            AI_MEDIUM,
        )
        self.assertEqual(
            ai.get_difficulty(),
            AI_MEDIUM,
        )

    def test_set_impossible_difficulty(self) -> None:
        # Tests setting Impossible difficulty

        ai = AIPlayer()
        ai.set_difficulty(
            AI_IMPOSSIBLE,
        )
        self.assertEqual(
            ai.get_difficulty(),
            AI_IMPOSSIBLE,
        )

    def test_invalid_difficulty_raises_error(self) -> None:
        # Tests that an invalid difficulty raises an exception

        ai = AIPlayer()
        with self.assertRaises(
            ValueError,
        ):

            ai.set_difficulty(
                "Expert",
            )

    def test_easy_move_returns_available_position(self) -> None:
        # Tests that Easy AI selects a legal move

        board = Board()
        ai = AIPlayer(
            AI_EASY,
        )
        move = ai.choose_move(
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

    def test_easy_move_returns_none_on_full_board(self) -> None:
        # Tests that Easy AI returns None when the board is full

        board = Board()
        symbol = PLAYER_X
        for row, col in board.get_available_moves():

            board.place_move(
                row,
                col,
                symbol,
            )
            symbol = (
                PLAYER_O
                if symbol == PLAYER_X
                else PLAYER_X
            )
        ai = AIPlayer(
            AI_EASY,
        )
        self.assertIsNone(
            ai.choose_move(
                board,
                PLAYER_X,
                PLAYER_O,
            )
        )

    def test_medium_ai_finds_winning_move(self) -> None:
        # Tests that Medium AI plays a winning move

        board = Board()
        board.place_move(
            0,
            0,
            PLAYER_X,
        )
        board.place_move(
            0,
            1,
            PLAYER_X,
        )
        ai = AIPlayer(
            AI_MEDIUM,
        )
        move = ai.choose_move(
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

    def test_medium_ai_blocks_opponent(self) -> None:
        # Tests that Medium AI blocks an opponent's winning move

        board = Board()
        board.place_move(
            1,
            0,
            PLAYER_O,
        )
        board.place_move(
            1,
            1,
            PLAYER_O,
        )
        ai = AIPlayer(
            AI_MEDIUM,
        )
        move = ai.choose_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )
        self.assertEqual(
            move,
            (
                1,
                2,
            ),
        )

    def test_medium_ai_returns_valid_move(self) -> None:
        # Tests that Medium AI always returns a valid move

        board = Board()
        ai = AIPlayer(
            AI_MEDIUM,
        )
        move = ai.choose_move(
            board,
            PLAYER_X,
            PLAYER_O,
        )
        self.assertIn(
            move,
            board.get_available_moves(),
        )

    def test_impossible_ai_returns_valid_move(self) -> None:
        # Tests that Impossible AI returns a legal move

        board = Board()
        ai = AIPlayer(
            AI_IMPOSSIBLE,
        )
        move = ai.choose_move(
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

    def test_find_winning_move_returns_none(self) -> None:
        # Tests that no winning move returns None

        board = Board()
        ai = AIPlayer()
        move = ai._find_winning_move(
            board,
            PLAYER_X,
        )
        self.assertIsNone(
            move,
        )

    def test_string_representation(self) -> None:
        # Tests the readable string representation

        ai = AIPlayer(
            AI_EASY,
        )
        self.assertEqual(
            str(ai),
            "AIPlayer(Difficulty=Easy)",
        )

    def test_repr_representation(self) -> None:
        # Tests the unambiguous representation

        ai = AIPlayer(
            AI_MEDIUM,
        )
        self.assertEqual(
            repr(ai),
            "AIPlayer(difficulty='Medium')",
        )


if __name__ == "__main__":
    unittest.main() 
