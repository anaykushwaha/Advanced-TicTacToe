# test_player.py
# Unit tests for player.py

import unittest
from game.constants import (
    PLAYER_X,
    PLAYER_O,
)

from game.player import (
    Player,
)


class TestPlayer(unittest.TestCase):
    # Tests the Player class

    def test_initialization(self) -> None:
        # Tests creating a valid human player

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        self.assertEqual(
            player.name,
            "Player 1",
        )

        self.assertEqual(
            player.symbol,
            PLAYER_X,
        )

        self.assertFalse(
            player.is_ai,
        )

        self.assertEqual(
            player.score,
            0,
        )

    def test_initialization_ai_player(self) -> None:
        # Tests creating a valid AI player

        player = Player(
            "Computer",
            PLAYER_O,
            True,
        )

        self.assertEqual(
            player.name,
            "Computer",
        )

        self.assertEqual(
            player.symbol,
            PLAYER_O,
        )

        self.assertTrue(
            player.is_ai,
        )

        self.assertEqual(
            player.score,
            0,
        )

    def test_name_is_stripped(self) -> None:
        # Tests that surrounding whitespace is removed from names

        player = Player(
            "  Player 1  ",
            PLAYER_X,
        )

        self.assertEqual(
            player.name,
            "Player 1",
        )

    def test_invalid_name_raises_value_error(self) -> None:
        # Tests that an invalid player name is rejected

        with self.assertRaises(
            ValueError,
        ):
            Player(
                "",
                PLAYER_X,
            )

    def test_invalid_symbol_raises_value_error(self) -> None:
        # Tests that an invalid player symbol is rejected

        with self.assertRaises(
            ValueError,
        ):
            Player(
                "Player 1",
                "A",
            )

    def test_invalid_ai_value_raises_type_error(self) -> None:
        # Tests that a non-boolean AI value is rejected

        with self.assertRaises(
            TypeError,
        ):
            Player(
                "Player 1",
                PLAYER_X,
                "True",
            )

    def test_add_point(self) -> None:
        # Tests increasing the player's score

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        player.add_point()

        self.assertEqual(
            player.score,
            1,
        )

    def test_add_multiple_points(self) -> None:
        # Tests increasing the score multiple times

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        player.add_point()
        player.add_point()
        player.add_point()

        self.assertEqual(
            player.score,
            3,
        )

    def test_reset_score(self) -> None:
        # Tests resetting the player's score

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        player.add_point()
        player.add_point()

        player.reset_score()

        self.assertEqual(
            player.score,
            0,
        )

    def test_change_name(self) -> None:
        # Tests changing the player's name

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        player.change_name(
            "Player 2",
        )

        self.assertEqual(
            player.name,
            "Player 2",
        )

    def test_change_name_strips_whitespace(self) -> None:
        # Tests that whitespace is removed from a new name

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        player.change_name(
            "  New Player  ",
        )

        self.assertEqual(
            player.name,
            "New Player",
        )

    def test_change_name_invalid(self) -> None:
        # Tests rejecting an invalid new player name

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        with self.assertRaises(
            ValueError,
        ):
            player.change_name(
                "",
            )

        self.assertEqual(
            player.name,
            "Player 1",
        )

    def test_get_details(self) -> None:
        # Tests retrieving the player's details

        player = Player(
            "Player 1",
            PLAYER_X,
            True,
        )

        player.add_point()

        details = player.get_details()

        self.assertEqual(
            details,
            {
                "name": "Player 1",
                "symbol": PLAYER_X,
                "is_ai": True,
                "score": 1,
            },
        )

    def test_get_details_returns_new_dictionary(self) -> None:
        # Tests that get_details returns player information
        # without exposing the internal player attributes directly

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        details = player.get_details()

        details["name"] = "Changed"

        self.assertEqual(
            player.name,
            "Player 1",
        )

    def test_string_representation_human(self) -> None:
        # Tests the readable string representation of a human player

        player = Player(
            "Player 1",
            PLAYER_X,
        )

        result = str(
            player,
        )

        self.assertEqual(
            result,
            "Player 1 (X) | Human | Score: 0",
        )

    def test_string_representation_ai(self) -> None:
        # Tests the readable string representation of an AI player

        player = Player(
            "Computer",
            PLAYER_O,
            True,
        )

        player.add_point()

        result = str(
            player,
        )

        self.assertEqual(
            result,
            "Computer (O) | AI | Score: 1",
        )

    def test_repr(self) -> None:
        # Tests the unambiguous representation of the player

        player = Player(
            "Player 1",
            PLAYER_X,
            True,
        )

        result = repr(
            player,
        )

        self.assertEqual(
            result,
            (
                "Player("
                "name='Player 1', "
                "symbol='X', "
                "is_ai=True, "
                "score=0)"
            ),
        )


if __name__ == "__main__":
    unittest.main()


__all__ = [
    "TestPlayer",
] 

