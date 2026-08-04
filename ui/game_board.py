# game_board.py
# Contains the GameBoard class, which is responsible for displaying
# and updating the game board

import tkinter as tk
from typing import Callable

from ui.animations import AnimationManager
from ui.theme import (
    BOARD_SIZE,
    BOARD_FONT,
    CELL_WIDTH,
    CELL_HEIGHT,
    BUTTON_COLOR,
    BUTTON_HOVER_COLOR,
    BOARD_BACKGROUND,
    CELL_PADDING,
    TEXT_COLOR,
    EMPTY_STRING,
    WIN_HIGHLIGHT_COLOR,
)


class GameBoard(tk.Frame):
    # Graphical representation of the game board

    def __init__(
        self,
        master: tk.Widget,
        cell_click_callback: Callable[[int, int], None],
    ) -> None:
        # Initializes the game board

        super().__init__(
            master,
            bg=BOARD_BACKGROUND,
        )

        self.cell_click_callback = (
            cell_click_callback
        )

        self.buttons = []

        self._create_board()

    def _create_board(
        self,
    ) -> None:
        # Creates the 3x3 button grid

        for row in range(
            BOARD_SIZE,
        ):

            button_row = []

            for col in range(
                BOARD_SIZE,
            ):

                button = tk.Button(
                    self,
                    text=EMPTY_STRING,
                    font=BOARD_FONT,
                    width=CELL_WIDTH,
                    height=CELL_HEIGHT,
                    bg=BUTTON_COLOR,
                    activebackground=BUTTON_HOVER_COLOR,
                    command=lambda r=row, c=col:
                        self.cell_click_callback(
                            r,
                            c,
                        ),
                )

                AnimationManager.add_hover_effect(
                    button,
                )

                button.grid(
                    row=row,
                    column=col,
                    padx=CELL_PADDING,
                    pady=CELL_PADDING,
                )

                button_row.append(
                    button,
                )

            self.buttons.append(
                button_row,
            )

    def update_cell(
        self,
        row: int,
        col: int,
        symbol: str,
        color: str,
    ) -> None:
        # Updates the appearance of a board cell

        self.buttons[row][col].configure(
            text=symbol,
            fg=color,
            state=tk.DISABLED,
        )

    def clear_board(
        self,
    ) -> None:
        # Resets every board cell to its default state

        for row in self.buttons:

            for button in row:

                button.configure(
                    text=EMPTY_STRING,
                    fg=TEXT_COLOR,
                    bg=BUTTON_COLOR,
                    state=tk.NORMAL,
                )

    def enable_cell(
        self,
        row: int,
        col: int,
    ) -> None:
        # Enables a single board cell

        self.buttons[row][col].configure(
            state=tk.NORMAL,
        )

    def disable_cell(
        self,
        row: int,
        col: int,
    ) -> None:
        # Disables a single board cell

        self.buttons[row][col].configure(
            state=tk.DISABLED,
        )

    def enable_board(
        self,
    ) -> None:
        # Enables every empty cell on the board

        for row in self.buttons:

            for button in row:

                if (
                    button["text"]
                    == EMPTY_STRING
                ):

                    button.configure(
                        state=tk.NORMAL,
                    )

    def disable_board(
        self,
    ) -> None:
        # Disables every board cell

        for row in self.buttons:

            for button in row:

                button.configure(
                    state=tk.DISABLED,
                )

    def highlight_cells(
        self,
        positions: list[
            tuple[int, int]
        ],
    ) -> None:
        # Highlights and animates the winning cells

        winning_buttons = []

        for row, col in positions:

            button = self.buttons[row][col]

            button.configure(
                bg=WIN_HIGHLIGHT_COLOR,
            )

            winning_buttons.append(
                button,
            )

        AnimationManager.flash_winning_cells(
            winning_buttons,
        )

    def reset_cell_colors(
        self,
    ) -> None:
        # Restores every cell's background colour

        for row in self.buttons:

            for button in row:

                button.configure(
                    bg=BUTTON_COLOR,
                )

    def get_button(
        self,
        row: int,
        col: int,
    ) -> tk.Button:
        # Returns a button widget

        if (
            row < 0
            or row >= BOARD_SIZE
            or col < 0
            or col >= BOARD_SIZE
        ):
            raise IndexError(
                "Board position out of range."
            )

        return self.buttons[row][col]


__all__ = [
    "GameBoard",
] 

