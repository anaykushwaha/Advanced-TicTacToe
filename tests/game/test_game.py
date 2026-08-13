# test_game.py
# Unit tests for game.py

import unittest
from game.constants import (
    PLAYER_X,
    PLAYER_O,
)
from game.game import Game
from game.player import Player


class TestGame(unittest.TestCase):
    # Tests the Game class

    def setUp(self) -> None:
        # Creates a fresh game before every test

        self.game = Game()

    def test_game_initialization(self) -> None:
        # Tests the constructor

        self.assertIsNotNone(
            self.game.board,
        )
        self.assertIsInstance(
            self.game.player_one,
            Player,
        )
        self.assertIsInstance(
            self.game.player_two,
            Player,
        )
        self.assertEqual(
            self.game.current_player,
            self.game.player_one,
        )
        self.assertFalse(
            self.game.game_over,
        )
        self.assertIsNone(
            self.game.winner,
        )
        self.assertEqual(
            self.game.winning_positions,
            [],
        )

    def test_switch_player(self) -> None:
        # Tests switching between players

        self.assertEqual(
            self.game.current_player,
            self.game.player_one,
        )
        self.game.switch_player()
        self.assertEqual(
            self.game.current_player,
            self.game.player_two,
        )
        self.game.switch_player()
        self.assertEqual(
            self.game.current_player,
            self.game.player_one,
        )

    def test_make_valid_move(self) -> None:
        # Tests making a valid move

        result = self.game.make_move(
            0,
            0,
        )
        self.assertTrue(
            result,
        )
        self.assertEqual(
            self.game.board.get_cell(
                0,
                0,
            ),
            PLAYER_X,
        )

    def test_make_invalid_move(self) -> None:
        # Tests making an invalid move

        self.game.make_move(
            0,
            0,
        )
        result = self.game.make_move(
            0,
            0,
        )
        self.assertFalse(
            result,
        )

    def test_make_move_after_game_over(self) -> None:
        # Tests making a move after the game ends

        self.game.game_over = True
        result = self.game.make_move(
            0,
            0,
        )
        self.assertFalse(
            result,
        )

    def test_get_current_player(self) -> None:
        # Tests retrieving the current player

        self.assertEqual(
            self.game.get_current_player(),
            self.game.player_one,
        )

    def test_get_current_symbol(self) -> None:
        # Tests retrieving the current symbol

        self.assertEqual(
            self.game.get_current_symbol(),
            PLAYER_X,
        )
        self.game.switch_player()
        self.assertEqual(
            self.game.get_current_symbol(),
            PLAYER_O,
        )

    def test_get_opponent_symbol(self) -> None:
        # Tests retrieving the opponent symbol

        self.assertEqual(
            self.game.get_opponent_symbol(),
            PLAYER_O,
        )
        self.game.switch_player()
        self.assertEqual(
            self.game.get_opponent_symbol(),
            PLAYER_X,
        )

    def test_get_board(self) -> None:
        # Tests retrieving the board

        self.assertEqual(
            self.game.get_board(),
            self.game.board,
        )

    def test_get_player_one(self) -> None:
        # Tests retrieving Player One

        self.assertEqual(
            self.game.get_player_one(),
            self.game.player_one,
        )

    def test_get_player_two(self) -> None:
        # Tests retrieving Player Two

        self.assertEqual(
            self.game.get_player_two(),
            self.game.player_two,
        )

    def test_is_against_ai(self) -> None:
        # Tests AI mode detection

        self.assertFalse(
            self.game.is_against_ai(),
        )
        ai_game = Game(
            versus_ai=True,
        )
        self.assertTrue(
            ai_game.is_against_ai(),
        )

    def test_get_player_by_symbol(self) -> None:
        # Tests retrieving players by symbol

        self.assertEqual(
            self.game.get_player_by_symbol(
                PLAYER_X,
            ),
            self.game.player_one,
        )
        self.assertEqual(
            self.game.get_player_by_symbol(
                PLAYER_O,
            ),
            self.game.player_two,
        )
        self.assertIsNone(
            self.game.get_player_by_symbol(
                "Z",
            ),
        ) 

    def test_update_game_state_win(self) -> None:
        # Tests detecting a winning game

        self.game.board.set_cell(
            0,
            0,
            PLAYER_X,
        )
        self.game.board.set_cell(
            0,
            1,
            PLAYER_X,
        )
        self.game.board.set_cell(
            0,
            2,
            PLAYER_X,
        )
        self.game.update_game_state()
        self.assertTrue(
            self.game.game_over,
        )
        self.assertEqual(
            self.game.winner,
            self.game.player_one,
        )
        self.assertEqual(
            self.game.player_one.score,
            1,
        )
        self.assertEqual(
            self.game.get_winning_positions(),
            [
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
            ],
        )

    def test_update_game_state_draw(self) -> None:
        # Tests detecting a draw

        board = [
            [
                PLAYER_X,
                PLAYER_O,
                PLAYER_X,
            ],
            [
                PLAYER_X,
                PLAYER_O,
                PLAYER_O,
            ],
            [
                PLAYER_O,
                PLAYER_X,
                PLAYER_X,
            ],
        ]
        for row in range(3):
            for col in range(3):
                self.game.board.set_cell(
                    row,
                    col,
                    board[row][col],
                )
        self.game.update_game_state()
        self.assertTrue(
            self.game.game_over,
        )
        self.assertIsNone(
            self.game.winner,
        )
        self.assertEqual(
            self.game.get_winning_positions(),
            [],
        )

    def test_get_winner(self) -> None:
        # Tests retrieving the winner

        self.assertIsNone(
            self.game.get_winner(),
        )
        self.game.board.set_cell(
            0,
            0,
            PLAYER_X,
        )
        self.game.board.set_cell(
            0,
            1,
            PLAYER_X,
        )
        self.game.board.set_cell(
            0,
            2,
            PLAYER_X,
        )
        self.game.update_game_state()
        self.assertEqual(
            self.game.get_winner(),
            self.game.player_one,
        )

    def test_get_scores(self) -> None:
        # Tests retrieving player scores

        self.game.player_one.add_point()
        self.game.player_two.add_point()
        scores = self.game.get_scores()
        self.assertEqual(
            scores[
                self.game.player_one.name
            ],
            1,
        )
        self.assertEqual(
            scores[
                self.game.player_two.name
            ],
            1,
        )

    def test_get_game_state(self) -> None:
        # Tests retrieving the complete game state

        state = self.game.get_game_state()
        self.assertIn(
            "current_player",
            state,
        )
        self.assertIn(
            "winner",
            state,
        )
        self.assertIn(
            "game_over",
            state,
        )
        self.assertIn(
            "board",
            state,
        )
        self.assertIn(
            "winning_positions",
            state,
        )

    def test_is_game_over(self) -> None:
        # Tests checking whether the game is over

        self.assertFalse(
            self.game.is_game_over(),
        )
        self.game.game_over = True
        self.assertTrue(
            self.game.is_game_over(),
        )

    def test_get_winning_positions(self) -> None:
        # Tests retrieving the winning positions

        self.assertEqual(
            self.game.get_winning_positions(),
            [],
        )
        self.game.winning_positions = [
            (
                1,
                0,
            ),
            (
                1,
                1,
            ),
            (
                1,
                2,
            ),
        ]
        self.assertEqual(
            self.game.get_winning_positions(),
            [
                (
                    1,
                    0,
                ),
                (
                    1,
                    1,
                ),
                (
                    1,
                    2,
                ),
            ],
        ) 
    def test_reset_board(self) -> None:
        # Tests resetting only the board

        self.game.make_move(
            0,
            0,
        )
        self.game.player_one.add_point()
        self.game.game_over = True
        self.game.winning_positions = [
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
        self.game.reset_board()
        self.assertFalse(
            self.game.is_game_over(),
        )
        self.assertIsNone(
            self.game.get_winner(),
        )
        self.assertEqual(
            self.game.get_winning_positions(),
            [],
        )
        self.assertEqual(
            self.game.get_current_player(),
            self.game.player_one,
        )
        self.assertEqual(
            self.game.player_one.score,
            1,
        )
        self.assertEqual(
            self.game.board.get_available_moves(),
            [
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
                (
                    1,
                    0,
                ),
                (
                    1,
                    1,
                ),
                (
                    1,
                    2,
                ),
                (
                    2,
                    0,
                ),
                (
                    2,
                    1,
                ),
                (
                    2,
                    2,
                ),
            ],
        )

    def test_reset_game(self) -> None:
        # Tests resetting the entire game

        self.game.player_one.add_point()
        self.game.player_two.add_point()
        self.game.make_move(
            0,
            0,
        )
        self.game.reset_game()
        self.assertEqual(
            self.game.player_one.score,
            0,
        )
        self.assertEqual(
            self.game.player_two.score,
            0,
        )
        self.assertFalse(
            self.game.is_game_over(),
        )
        self.assertIsNone(
            self.game.get_winner(),
        )
        self.assertEqual(
            self.game.get_winning_positions(),
            [],
        )

    def test_str(self) -> None:
        # Tests the string representation

        text = str(
            self.game,
        )
        self.assertIn(
            "Game",
            text,
        )
        self.assertIn(
            "Current Player",
            text,
        )

    def test_repr(self) -> None:
        # Tests the object representation

        text = repr(
            self.game,
        )
        self.assertIn(
            "Game",
            text,
        )
        self.assertIn(
            "player_one",
            text,
        )
        self.assertIn(
            "player_two",
            text,
        )


__all__ = [
    "TestGame",
]

if __name__ == "__main__":
    unittest.main() 

