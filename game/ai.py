# ai.py
# Defines the AIPlayer class, which is responsible for selecting moves
# for computer-controlled players at different difficulty levels

import random
from typing import Optional, Tuple

from game.board import Board
from game.constants import (
    AI_EASY,
    AI_MEDIUM,
    AI_IMPOSSIBLE,
)
from game.minimax import find_best_move


class AIPlayer:
    # Represents the computer-controlled player

    def __init__(
        self,
        difficulty: str = AI_MEDIUM,
    ) -> None:
        # Initializes the AI

        self.difficulty = AI_MEDIUM

        self.set_difficulty(
            difficulty,
        )

    def choose_move(
        self,
        board: Board,
        ai_symbol: str,
        opponent_symbol: str,
    ) -> Optional[Tuple[int, int]]:
        # Chooses a move based on the selected difficulty

        if self.difficulty == AI_EASY:

            return self._easy_move(
                board,
            )

        if self.difficulty == AI_MEDIUM:

            return self._medium_move(
                board,
                ai_symbol,
                opponent_symbol,
            )

        if self.difficulty == AI_IMPOSSIBLE:

            return self._impossible_move(
                board,
                ai_symbol,
                opponent_symbol,
            )

        raise ValueError(
            f"Unknown AI difficulty: {self.difficulty}"
        )

    def _easy_move(
        self,
        board: Board,
    ) -> Optional[Tuple[int, int]]:
        # Selects a completely random legal move

        available_moves = (
            board.get_available_moves()
        )

        if not available_moves:
            return None

        return random.choice(
            available_moves,
        )

    def _medium_move(
        self,
        board: Board,
        ai_symbol: str,
        opponent_symbol: str,
    ) -> Optional[Tuple[int, int]]:
        # Selects a move for the medium AI

        winning_move = self._find_winning_move(
            board,
            ai_symbol,
        )

        if winning_move is not None:
            return winning_move

        blocking_move = self._find_winning_move(
            board,
            opponent_symbol,
        )

        if blocking_move is not None:
            return blocking_move

        return self._easy_move(
            board,
        )

    def _find_winning_move(
        self,
        board: Board,
        symbol: str,
    ) -> Optional[Tuple[int, int]]:
        # Finds a move that immediately wins the game

        available_moves = (
            board.get_available_moves()
        )

        for row, col in available_moves:

            board.set_cell(
                row,
                col,
                symbol,
            )

            if (
                board.check_winner()
                == symbol
            ):

                board.clear_cell(
                    row,
                    col,
                )

                return (
                    row,
                    col,
                )

            board.clear_cell(
                row,
                col,
            )

        return None

    def _impossible_move(
        self,
        board: Board,
        ai_symbol: str,
        opponent_symbol: str,
    ) -> Optional[Tuple[int, int]]:
        # Selects the best possible move
        # using the Minimax algorithm

        return find_best_move(
            board,
            ai_symbol,
            opponent_symbol,
        )

    def set_difficulty(
        self,
        difficulty: str,
    ) -> None:
        # Changes the AI difficulty

        if difficulty not in (
            AI_EASY,
            AI_MEDIUM,
            AI_IMPOSSIBLE,
        ):
            raise ValueError(
                "Invalid AI difficulty."
            )

        self.difficulty = difficulty

    def get_difficulty(
        self,
    ) -> str:
        # Returns the current AI difficulty

        return self.difficulty

    def __str__(
        self,
    ) -> str:
        # Returns a readable description
        # of the AI

        return (
            f"AIPlayer("
            f"Difficulty={self.difficulty})"
        )

    def __repr__(
        self,
    ) -> str:
        # Returns an unambiguous representation
        # of the AIPlayer object

        return (
            f"AIPlayer("
            f"difficulty='{self.difficulty}')"
        )


__all__ = [
    "AIPlayer",
] 

