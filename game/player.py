# player.py
# Defines the Player class used throughout the game.
# Each Player object stores information about a single player,
# including their name, symbol, AI status and score.

from game.constants import (
    PLAYER_X,
    PLAYER_O,
)
from game.validator import is_valid_player_name


class Player:
    # Represents a player in the game

    def __init__(
        self,
        name: str,
        symbol: str,
        is_ai: bool = False,
    ) -> None:
        # Initializes a new player

        if not is_valid_player_name(name):
            raise ValueError(
                "Invalid player name."
            )

        if symbol not in (
            PLAYER_X,
            PLAYER_O,
        ):
            raise ValueError(
                "Player symbol must be 'X' or 'O'."
            )

        if not isinstance(is_ai, bool):
            raise TypeError(
                "is_ai must be a boolean."
            )

        self.name = name.strip()
        self.symbol = symbol
        self.is_ai = is_ai
        self.score = 0

    def add_point(
        self,
    ) -> None:
        # Increases the player's score by one

        self.score += 1

    def reset_score(
        self,
    ) -> None:
        # Resets the player's score to zero

        self.score = 0

    def change_name(
        self,
        new_name: str,
    ) -> None:
        # Changes the player's display name

        if not is_valid_player_name(
            new_name,
        ):
            raise ValueError(
                "Invalid player name."
            )

        self.name = new_name.strip()

    def get_details(
        self,
    ) -> dict:
        # Returns the player's information
        # as a dictionary

        return {
            "name": self.name,
            "symbol": self.symbol,
            "is_ai": self.is_ai,
            "score": self.score,
        }

    def __str__(
        self,
    ) -> str:
        # Returns a readable string
        # representation of the player

        player_type = (
            "AI"
            if self.is_ai
            else "Human"
        )

        return (
            f"{self.name} "
            f"({self.symbol}) | "
            f"{player_type} | "
            f"Score: {self.score}"
        )

    def __repr__(
        self,
    ) -> str:
        # Returns an unambiguous representation
        # of the player

        return (
            f"Player("
            f"name='{self.name}', "
            f"symbol='{self.symbol}', "
            f"is_ai={self.is_ai}, "
            f"score={self.score})"
        )


__all__ = [
    "Player",
] 

