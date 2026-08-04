# main_window.py
# Main controller for the graphical game application
# This class connects the backend game logic with the Tkinter UI

import tkinter as tk

from game.ai import AIPlayer
from game.constants import (
    PLAYER_X,
    PLAYER_O,
)
from game.game import Game
from game.settings import SettingsManager
from game.statistics import StatisticsManager

from ui.dialogs import DialogManager
from ui.game_board import GameBoard
from ui.theme import (
    WINDOW_TITLE,
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    WINDOW_RESIZABLE,
    BACKGROUND_COLOR,
    TITLE_FONT,
    HEADER_FONT,
    BODY_FONT,
    OUTER_PADDING,
    SECTION_SPACING,
    STATUS_READY,
    STATUS_PLAYER_TURN,
    STATUS_DRAW,
    STATUS_WINNER,
    STATUS_AI_THINKING,
    X_COLOR,
    O_COLOR,
)


class MainWindow:
    # Main application window

    def __init__(
        self,
    ) -> None:
        # Creates the application window and initializes
        # every game component

        # Window

        self.root = tk.Tk()

        self.root.title(
            WINDOW_TITLE,
        )

        self.root.geometry(
            f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}"
        )

        self.root.resizable(
            WINDOW_RESIZABLE,
            WINDOW_RESIZABLE,
        )

        self.root.configure(
            bg=BACKGROUND_COLOR,
        )

        self.root.protocol(
            "WM_DELETE_WINDOW",
            self.exit_application,
        )

        # Managers

        self.settings = SettingsManager()

        self.statistics = StatisticsManager()

        # Game Engine

        self.game = Game(
            versus_ai=self.settings.get_setting(
                "ai_enabled",
            ),
        )

        self.ai = AIPlayer(
            self.settings.get_setting(
                "difficulty",
            ),
        )

        self.ai_enabled = self.settings.get_setting(
            "ai_enabled",
        )

        # Session Scoreboard

        self.x_score = 0

        self.o_score = 0

        self.draws = 0

        # Tkinter Variables

        self.status_var = tk.StringVar(
            value=STATUS_READY,
        )

        self.x_score_var = tk.StringVar(
            value="X : 0",
        )

        self.o_score_var = tk.StringVar(
            value="O : 0",
        )

        self.draw_var = tk.StringVar(
            value="Draws : 0",
        )

        # UI Components

        self.title_label: tk.Label | None = None

        self.status_label: tk.Label | None = None

        self.score_frame: tk.Frame | None = None

        self.game_board: GameBoard | None = None

        # Build the interface

        self._create_widgets()

    def _create_widgets(
        self,
    ) -> None:
        # Creates every widget displayed in the application

        # Title

        self.title_label = tk.Label(
            self.root,
            text=WINDOW_TITLE,
            font=TITLE_FONT,
            bg=BACKGROUND_COLOR,
        )

        self.title_label.pack(
            pady=OUTER_PADDING,
        )

        # Status Label

        self.status_label = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=BODY_FONT,
            bg=BACKGROUND_COLOR,
        )

        self.status_label.pack(
            pady=SECTION_SPACING,
        )

        # Scoreboard

        self.score_frame = tk.Frame(
            self.root,
            bg=BACKGROUND_COLOR,
        )

        self.score_frame.pack(
            pady=SECTION_SPACING,
        )

        tk.Label(
            self.score_frame,
            textvariable=self.x_score_var,
            font=HEADER_FONT,
            fg=X_COLOR,
            bg=BACKGROUND_COLOR,
        ).grid(
            row=0,
            column=0,
            padx=20,
        )

        tk.Label(
            self.score_frame,
            textvariable=self.draw_var,
            font=HEADER_FONT,
            bg=BACKGROUND_COLOR,
        ).grid(
            row=0,
            column=1,
            padx=20,
        )

        tk.Label(
            self.score_frame,
            textvariable=self.o_score_var,
            font=HEADER_FONT,
            fg=O_COLOR,
            bg=BACKGROUND_COLOR,
        ).grid(
            row=0,
            column=2,
            padx=20,
        )

        # Game Board

        self.game_board = GameBoard(
            self.root,
            self._on_cell_clicked,
        )

        self.game_board.pack(
            pady=OUTER_PADDING,
        ) 

    def _on_cell_clicked(
        self,
        row: int,
        col: int,
    ) -> None:
        # Handles a click on the game board

        if self.game.is_game_over():
            return

        if not self.game.make_move(
            row,
            col,
        ):
            return

        self._update_board()

        if self._handle_game_end():
            return

        if self.ai_enabled:
            self._perform_ai_move()

    def _update_board(
        self,
    ) -> None:
        # Synchronizes the graphical board with the backend game state

        board = self.game.get_board().get_board()

        for row in range(
            len(board),
        ):

            for col in range(
                len(board[row]),
            ):

                symbol = board[row][col]

                if not symbol:
                    continue

                color = (
                    X_COLOR
                    if symbol == PLAYER_X
                    else O_COLOR
                )

                self.game_board.update_cell(
                    row,
                    col,
                    symbol,
                    color,
                )

        self._update_status()

    def _update_status(
        self,
    ) -> None:
        # Updates the status message beneath the title

        if self.game.is_game_over():
            return

        current_player = (
            self.game.get_current_player()
        )

        self.status_var.set(
            STATUS_PLAYER_TURN.format(
                current_player.symbol,
            )
        )

    def _handle_game_end(
        self,
    ) -> bool:
        # Handles the end of a completed game

        if not self.game.is_game_over():
            return False

        self.game_board.disable_board()

        winner = self.game.get_winner()

        if winner is None:

            self.draws += 1

            self.draw_var.set(
                f"Draws : {self.draws}"
            )

            self.statistics.record_draw()

            self.status_var.set(
                STATUS_DRAW,
            )

            DialogManager.show_game_over(
                STATUS_DRAW,
            )

        else:

            if winner.symbol == PLAYER_X:

                self.x_score += 1

                self.x_score_var.set(
                    f"X : {self.x_score}"
                )

            else:

                self.o_score += 1

                self.o_score_var.set(
                    f"O : {self.o_score}"
                )

            self.statistics.record_win(
                winner.symbol,
                self.ai_enabled,
            )

            self.status_var.set(
                STATUS_WINNER.format(
                    winner.name,
                )
            )

            winning_cells = (
                self.game.get_winning_positions()
            )

            if winning_cells:

                self.game_board.highlight_cells(
                    winning_cells,
                )

            DialogManager.show_game_over(
                STATUS_WINNER.format(
                    winner.name,
                )
            )

        if DialogManager.ask_new_game():

            self.new_game()

        return True 

    def _perform_ai_move(
        self,
    ) -> None:
        # Allows the AI player to make its move

        if self.game.is_game_over():
            return

        self.status_var.set(
            STATUS_AI_THINKING,
        )

        self.root.update_idletasks()

        current_player = (
            self.game.get_current_player()
        )

        opponent = (
            self.game.get_player_by_symbol(
                PLAYER_X
                if current_player.symbol == PLAYER_O
                else PLAYER_O
            )
        )

        move = self.ai.choose_move(
            self.game.get_board(),
            current_player.symbol,
            opponent.symbol,
        )

        if move is None:
            return

        row, col = move

        self.game.make_move(
            row,
            col,
        )

        self._update_board()

        self._handle_game_end()

    def new_game(
        self,
    ) -> None:
        # Starts a new game while keeping the current
        # session scores

        self.game.reset_board()

        self.game_board.clear_board()

        self.game_board.enable_board()

        self.status_var.set(
            STATUS_READY,
        )

    def reset_scores(
        self,
    ) -> None:
        # Resets the current session scores

        if not DialogManager.confirm_reset_scores():
            return

        self.x_score = 0

        self.o_score = 0

        self.draws = 0

        self.x_score_var.set(
            "X : 0",
        )

        self.o_score_var.set(
            "O : 0",
        )

        self.draw_var.set(
            "Draws : 0",
        )

    def toggle_ai(
        self,
        enabled: bool,
    ) -> None:
        # Enables or disables AI mode

        self.ai_enabled = enabled

        self.settings.set_setting(
            "ai_enabled",
            enabled,
        )

        self.game = Game(
            versus_ai=enabled,
        )

        self.game_board.clear_board()

        self.game_board.enable_board()

        self.status_var.set(
            STATUS_READY,
        )

    def set_ai_difficulty(
        self,
        difficulty: str,
    ) -> None:
        # Changes the AI difficulty

        self.ai.set_difficulty(
            difficulty,
        )

        self.settings.set_setting(
            "difficulty",
            difficulty,
        )

    def show_about(
        self,
    ) -> None:
        # Displays the About dialog

        DialogManager.show_about()

    def show_statistics(
        self,
    ) -> None:
        # Displays the current session statistics

        DialogManager.show_statistics(
            self.x_score,
            self.o_score,
            self.draws,
        )

    def exit_application(
        self,
    ) -> None:
        # Saves application data before closing

        self.settings.save_settings()

        self.statistics.save_statistics()

        self.root.destroy()

    def run(
        self,
    ) -> None:
        # Starts the Tkinter event loop

        self.root.mainloop()


__all__ = [
    "MainWindow",
] 

