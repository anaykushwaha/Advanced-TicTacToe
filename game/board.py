# board.py
# Defines the Board class, which manages the game board,
# player moves and win/draw detection

from typing import List, Optional, Tuple

from game.constants import (
    BOARD_SIZE,
    EMPTY_CELL,
    PLAYER_X,
    PLAYER_O,
)
from game.helper import (
    create_empty_board,
    get_available_moves,
)
from game.validator import is_valid_position


class Board:
    # Represents the game board

    def __init__(
        self,
    ) -> None:
        # Creates a new empty game board

        self.board = create_empty_board()

    def reset(
        self,
    ) -> None:
        # Resets the board to its initial empty state

        self.board = create_empty_board()

    def get_board(
        self,
    ) -> List[List[str]]:
        # Returns a copy of the current board

        return [
            row.copy()
            for row in self.board
        ]

    def is_cell_empty(
        self,
        row: int,
        col: int,
    ) -> bool:
        # Checks whether a board cell is empty

        if not is_valid_position(
            row,
            col,
        ):
            return False

        return (
            self.board[row][col]
            == EMPTY_CELL
        )

    def is_valid_move(
        self,
        row: int,
        col: int,
    ) -> bool:
        # Determines whether a move is valid

        return (
            is_valid_position(
                row,
                col,
            )
            and self.is_cell_empty(
                row,
                col,
            )
        )

    def place_move(
        self,
        row: int,
        col: int,
        symbol: str,
    ) -> bool:
        # Places a player's symbol on the board

        if symbol not in (
            PLAYER_X,
            PLAYER_O,
        ):
            return False

        if not self.is_valid_move(
            row,
            col,
        ):
            return False

        self.board[row][col] = symbol

        return True

    def set_cell(
        self,
        row: int,
        col: int,
        value: str,
    ) -> None:
        # Sets the value of a board cell

        if not is_valid_position(
            row,
            col,
        ):
            raise ValueError(
                "Invalid board position."
            )

        if value not in (
            PLAYER_X,
            PLAYER_O,
            EMPTY_CELL,
        ):
            raise ValueError(
                "Invalid board value."
            )

        self.board[row][col] = value

    def clear_cell(
        self,
        row: int,
        col: int,
    ) -> None:
        # Clears a board cell

        if not is_valid_position(
            row,
            col,
        ):
            raise ValueError(
                "Invalid board position."
            )

        self.board[row][col] = EMPTY_CELL

    def get_cell(
        self,
        row: int,
        col: int,
    ) -> str:
        # Returns the value stored in a board cell

        if not is_valid_position(
            row,
            col,
        ):
            raise ValueError(
                "Invalid board position."
            )

        return self.board[row][col]

    def get_available_moves(
        self,
    ) -> List[Tuple[int, int]]:
        # Returns every available move

        return get_available_moves(
            self.board,
        )

    def is_full(
        self,
    ) -> bool:
        # Checks whether the board is full

        return (
            len(
                self.get_available_moves()
            )
            == 0
        )

    def check_winner(
        self,
    ) -> Optional[str]:
        # Determines whether either player has won

        # Check rows

        for row in self.board:

            if (
                row[0] != EMPTY_CELL
                and row.count(row[0])
                == BOARD_SIZE
            ):
                return row[0]

        # Check columns

        for col in range(
            BOARD_SIZE,
        ):

            symbol = self.board[0][col]

            if symbol == EMPTY_CELL:
                continue

            if all(
                self.board[row][col]
                == symbol
                for row in range(
                    BOARD_SIZE,
                )
            ):
                return symbol

        # Check main diagonal

        symbol = self.board[0][0]

        if (
            symbol != EMPTY_CELL
            and all(
                self.board[i][i]
                == symbol
                for i in range(
                    BOARD_SIZE,
                )
            )
        ):
            return symbol

        # Check secondary diagonal

        symbol = self.board[0][
            BOARD_SIZE - 1
        ]

        if (
            symbol != EMPTY_CELL
            and all(
                self.board[i][
                    BOARD_SIZE - 1 - i
                ]
                == symbol
                for i in range(
                    BOARD_SIZE,
                )
            )
        ):
            return symbol

        return None

    def is_draw(
        self,
    ) -> bool:
        # Determines whether the game is a draw

        return (
            self.is_full()
            and self.check_winner()
            is None
        )

    def __str__(
        self,
    ) -> str:
        # Returns a readable board representation

        rows = []

        for row in self.board:

            rows.append(
                " | ".join(
                    cell
                    if cell
                    else " "
                    for cell in row
                )
            )

        separator = (
            "\n"
            + "-" * 9
            + "\n"
        )

        return separator.join(
            rows
        )


__all__ = [
    "Board",
] 

