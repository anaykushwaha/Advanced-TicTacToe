# game.py
# Defines the Game class, which acts as the controller for the game.
# It coordinates the players, board, game state and overall game flow.

from typing import Optional

from game.board import Board
from game.constants import (
    DEFAULT_PLAYER_ONE,
    DEFAULT_PLAYER_TWO,
    PLAYER_X,
    PLAYER_O,
)
from game.player import Player


class Game:
    # Controls the overall game flow

    def __init__(
        self,
        player_one_name: str = DEFAULT_PLAYER_ONE,
        player_two_name: str = DEFAULT_PLAYER_TWO,
        versus_ai: bool = False,
    ) -> None:
        # Initializes a new game

        # Create the board

        self.board = Board()

        # Create the players

        self.player_one = Player(
            player_one_name,
            PLAYER_X,
            False,
        )

        self.player_two = Player(
            player_two_name,
            PLAYER_O,
            versus_ai,
        )

        # X always starts first

        self.current_player = self.player_one

        # Winner of the current game

        self.winner: Optional[Player] = None

        # Whether the game has ended

        self.game_over = False

        # Coordinates of the winning line

        self.winning_positions = []

    def switch_player(
        self,
    ) -> None:
        # Switches the current player

        if self.current_player == self.player_one:

            self.current_player = self.player_two

        else:

            self.current_player = self.player_one

    def make_move(
        self,
        row: int,
        col: int,
    ) -> bool:
        # Attempts to place the current player's symbol
        # on the board

        if self.game_over:
            return False

        move_played = self.board.place_move(
            row,
            col,
            self.current_player.symbol,
        )

        if not move_played:
            return False

        self.update_game_state()

        if not self.game_over:

            self.switch_player()

        return True

    def update_game_state(
        self,
    ) -> None:
        # Updates the game state after every move

        winning_symbol = self.board.check_winner()

        if winning_symbol is not None:

            self.winning_positions = (
                self.board.get_winning_positions()
            )

            self.winner = (
                self.player_one
                if winning_symbol
                == self.player_one.symbol
                else self.player_two
            )

            self.winner.add_point()

            self.game_over = True

            return

        if self.board.is_draw():

            self.game_over = True

    def get_current_player(
        self,
    ) -> Player:
        # Returns the player whose turn it is

        return self.current_player

    def get_current_symbol(
        self,
    ) -> str:
        # Returns the symbol of the current player

        return self.current_player.symbol

    def get_opponent_symbol(
        self,
    ) -> str:
        # Returns the opponent's symbol

        if self.current_player == self.player_one:

            return self.player_two.symbol

        return self.player_one.symbol

    def get_winner(
        self,
    ) -> Optional[Player]:
        # Returns the winner of the current game

        return self.winner

    def get_board(
        self,
    ) -> Board:
        # Returns the Board object

        return self.board

    def get_player_one(
        self,
    ) -> Player:
        # Returns Player One

        return self.player_one

    def get_player_two(
        self,
    ) -> Player:
        # Returns Player Two

        return self.player_two

    def get_scores(
        self,
    ) -> dict:
        # Returns both player scores

        return {
            self.player_one.name:
                self.player_one.score,
            self.player_two.name:
                self.player_two.score,
        }

    def is_against_ai(
        self,
    ) -> bool:
        # Checks whether Player Two is AI

        return self.player_two.is_ai

    def get_game_state(
        self,
    ) -> dict:
        # Returns the current game state

        return {
            "current_player":
                self.current_player.name,
            "winner":
                (
                    self.winner.name
                    if self.winner is not None
                    else None
                ),
            "game_over":
                self.game_over,
            "board":
                self.board.get_board(),
            "winning_positions":
                self.winning_positions,
        }

    def get_player_by_symbol(
        self,
        symbol: str,
    ) -> Optional[Player]:
        # Returns the player with the given symbol

        if symbol == self.player_one.symbol:

            return self.player_one

        if symbol == self.player_two.symbol:

            return self.player_two

        return None

    def is_game_over(
        self,
    ) -> bool:
        # Returns whether the game has ended

        return self.game_over

    def get_winning_positions(
        self,
    ):
        # Returns the coordinates of the winning line

        return self.winning_positions

    def reset_board(
        self,
    ) -> None:
        # Resets the board while keeping scores

        self.board.reset()

        self.current_player = self.player_one

        self.winner = None

        self.game_over = False

        self.winning_positions = []

    def reset_game(
        self,
    ) -> None:
        # Resets the entire game session

        self.reset_board()

        self.player_one.reset_score()

        self.player_two.reset_score()

    def __str__(
        self,
    ) -> str:
        # Returns a readable description of the game

        status = (
            "Finished"
            if self.game_over
            else "In Progress"
        )

        return (
            f"Game("
            f"Status={status}, "
            f"Current Player={self.current_player.name})"
        )

    def __repr__(
        self,
    ) -> str:
        # Returns an unambiguous representation
        # of the Game object

        return (
            f"Game("
            f"player_one={repr(self.player_one)}, "
            f"player_two={repr(self.player_two)}, "
            f"game_over={self.game_over})"
        )


__all__ = [
    "Game",
] 

