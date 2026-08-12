# test_main_window.py
# Unit tests for main_window.py

import unittest
from unittest.mock import (
    MagicMock,
    patch, 
    Mock, 
)
from game.constants import (
    PLAYER_X,
    PLAYER_O,
)
from ui.main_window import (
    MainWindow,
)
from ui.theme import (
    STATUS_READY,
    STATUS_DRAW,
    STATUS_WINNER,
    WINDOW_TITLE,
)

class TestMainWindow(unittest.TestCase):
    # Tests the MainWindow class

    @patch("ui.main_window.GameBoard")
    @patch("ui.main_window.StatisticsManager")
    @patch("ui.main_window.SettingsManager")
    @patch("ui.main_window.AIPlayer")
    @patch("ui.main_window.Game")
    @patch("ui.main_window.tk.Tk")
    def setUp(
        self,
        mock_tk,
        mock_game,
        mock_ai,
        mock_settings,
        mock_statistics,
        mock_game_board,
    ) -> None:
        # Creates a fresh MainWindow before every test

        self.root = MagicMock()

        mock_tk.return_value = self.root

        self.settings = MagicMock()

        self.settings.get_setting.side_effect = (
            lambda key: {
                "ai_enabled": False,
                "difficulty": "Medium",
            }[key]
        )

        mock_settings.return_value = (
            self.settings
        )

        self.statistics = MagicMock()

        mock_statistics.return_value = (
            self.statistics
        )

        self.game = MagicMock()

        self.game.get_board.return_value = (
            MagicMock()
        )

        self.game.get_current_player.return_value.symbol = (
            PLAYER_X
        )

        self.game.get_current_player.return_value.name = (
            "Player 1"
        )

        self.game.is_game_over.return_value = (
            False
        )

        mock_game.return_value = (
            self.game
        )

        self.ai = MagicMock()

        mock_ai.return_value = (
            self.ai
        )

        self.game_board = MagicMock()

        mock_game_board.return_value = (
            self.game_board
        )

        self.window = MainWindow()

    def test_initialization(self) -> None:
        # Tests the constructor

        self.assertIsNotNone(
            self.window.game,
        )

        self.assertIsNotNone(
            self.window.ai,
        )

        self.assertIsNotNone(
            self.window.settings,
        )

        self.assertIsNotNone(
            self.window.statistics,
        )

        self.assertEqual(
            self.window.ai_enabled,
            False,
        )
        self.assertEqual(
            self.window.x_score,
            0,
        )
        self.assertEqual(
            self.window.o_score,
            0,
        )
        self.assertEqual(
            self.window.draws,
            0,
        )

    def test_window_configuration(self) -> None:
        # Tests configuring the main window

        self.root.title.assert_called_once_with(
            WINDOW_TITLE,
        )
        self.root.geometry.assert_called_once()
        self.root.resizable.assert_called_once()
        self.root.configure.assert_called_once()
        self.root.protocol.assert_called_once()

    def test_create_widgets(self) -> None:
        # Tests creating the interface widgets

        self.assertIsNotNone(
            self.window.title_label,
        )
        self.assertIsNotNone(
            self.window.status_label,
        )
        self.assertIsNotNone(
            self.window.score_frame,
        )
        self.assertIsNotNone(
            self.window.game_board,
        )

    def test_status_variable_initial_value(self) -> None:
        # Tests the initial status message

        self.assertEqual(
            self.window.status_var.get(),
            STATUS_READY,
        )

    def test_initial_scoreboard_values(self) -> None:
        # Tests the initial scoreboard

        self.assertEqual(
            self.window.x_score_var.get(),
            "X : 0",
        )
        self.assertEqual(
            self.window.o_score_var.get(),
            "O : 0",
        )
        self.assertEqual(
            self.window.draw_var.get(),
            "Draws : 0",
        )

    def test_gameboard_created(self) -> None:
        # Tests creating the game board

        self.assertIsNotNone(
            self.window.game_board,
        )

    def test_settings_loaded(self) -> None:
        # Tests loading settings

        self.settings.get_setting.assert_any_call(
            "ai_enabled",
        )
        self.settings.get_setting.assert_any_call(
            "difficulty",
        )

    def test_statistics_manager_created(self) -> None:
        # Tests creating the statistics manager

        self.assertIsNotNone(
            self.window.statistics,
        )

    def test_ai_created(self) -> None:
        # Tests creating the AI

        self.assertIsNotNone(
            self.window.ai,
        )

    def test_game_created(self) -> None:
        # Tests creating the Game object

        self.assertIsNotNone(
            self.window.game,
        ) 

    @patch.object(
        MainWindow,
        "_update_board",
        )
    @patch.object(
            MainWindow,
            "_handle_game_end",
    )
    def test_on_cell_clicked_valid_move(
        self,
        mock_handle_game_end,
        mock_update_board,
    ) -> None:
        # Tests clicking a valid board cell

        self.game.is_game_over.return_value = (
            False
        )

        self.game.make_move.return_value = (
            True
        )

        mock_handle_game_end.return_value = (
            False
        )

        self.window.ai_enabled = False

        self.window._on_cell_clicked(
            1,
            2,
        )

        self.game.make_move.assert_called_once_with(
            1,
            2,
        )

        mock_update_board.assert_called_once()

        mock_handle_game_end.assert_called_once()

    @patch.object(
        MainWindow,
        "_update_board",
    )
    def test_on_cell_clicked_invalid_move(
        self,
        mock_update_board,
    ) -> None:
        # Tests clicking an occupied cell

        self.game.is_game_over.return_value = (
            False
        )

        self.game.make_move.return_value = (
            False
        )

        self.window._on_cell_clicked(
            0,
            0,
        )

        mock_update_board.assert_not_called()

    @patch.object(
        MainWindow,
        "_update_board",
    )
    def test_on_cell_clicked_game_over(
        self,
        mock_update_board,
    ) -> None:
        # Tests clicking after the game ends

        self.game.is_game_over.return_value = (
            True
        )

        self.window._on_cell_clicked(
            0,
            0,
        )

        self.game.make_move.assert_not_called()

        mock_update_board.assert_not_called()

    @patch.object(
        MainWindow,
        "_perform_ai_move",
    )
    @patch.object(
        MainWindow,
        "_handle_game_end",
    )
    @patch.object(
        MainWindow,
        "_update_board",
    )
    def test_on_cell_clicked_ai_enabled(
        self,
        mock_update_board,
        mock_handle_game_end,
        mock_ai_move,
    ) -> None:
        # Tests AI being triggered

        self.window.ai_enabled = True

        self.game.is_game_over.return_value = (
            False
        )

        self.game.make_move.return_value = (
            True
        )

        mock_handle_game_end.return_value = (
            False
        )

        self.window._on_cell_clicked(
            2,
            1,
        )

        mock_ai_move.assert_called_once()

    def test_update_board(
        self,
    ) -> None:
        # Tests updating the graphical board

        board = [
            [
                PLAYER_X,
                "",
                "",
            ],
            [
                "",
                PLAYER_O,
                "",
            ],
            [
                "",
                "",
                PLAYER_X,
            ],
        ]

        self.game.get_board.return_value.get_board.return_value = (
            board
        )

        self.window._update_board()

        self.assertEqual(
            self.game_board.update_cell.call_count,
            3,
        )

    @patch.object(
        MainWindow,
        "_update_status",
    )
    def test_update_board_updates_status(
        self,
        mock_update_status,
    ) -> None:
        # Tests updating the status message

        self.game.get_board.return_value.get_board.return_value = (
            [
                [
                    "",
                    "",
                    "",
                ],
                [
                    "",
                    "",
                    "",
                ],
                [
                    "",
                    "",
                    "",
                ],
            ]
        )
        self.window._update_board()
        mock_update_status.assert_called_once()

    def test_update_status(self) -> None: 
        # Tests updating the turn message

        self.game.is_game_over.return_value = (
            False
        )

        player = MagicMock()
        player.symbol = PLAYER_O
        self.game.get_current_player.return_value = (
            player
        )
        self.window._update_status()
        self.assertIn(
            PLAYER_O,
            self.window.status_var.get(),
        )

    def test_update_status_game_over(self) -> None: 
        # Tests that no status update occurs
        # after the game ends

        self.game.is_game_over.return_value = (
            True
        )
        previous_status = (
            self.window.status_var.get()
        )
        self.window._update_status()
        self.assertEqual(
            self.window.status_var.get(),
            previous_status,
        ) 

    @patch(
        "ui.main_window.DialogManager.ask_new_game",
        return_value=False,
    )
    @patch(
        "ui.main_window.DialogManager.show_game_over",
    )
    def test_handle_game_end_draw(
        self,
        mock_show_game_over,
        mock_new_game,
    ) -> None:
        # Tests handling a draw

        self.game.is_game_over.return_value = (
            True
        )

        self.game.get_winner.return_value = (
            None
        )

        result = self.window._handle_game_end()

        self.assertTrue(
            result,
        )

        self.assertEqual(
            self.window.draws,
            1,
        )

        self.statistics.record_draw.assert_called_once()

        mock_show_game_over.assert_called_once_with(
            STATUS_DRAW,
        )

        self.game_board.disable_board.assert_called_once()

    @patch(
        "ui.main_window.DialogManager.ask_new_game",
        return_value=False,
    )
    @patch(
        "ui.main_window.DialogManager.show_game_over",
    )
    def test_handle_game_end_player_x_win(
        self,
        mock_show_game_over,
        mock_new_game,
    ) -> None:
        # Tests Player X winning

        winner = MagicMock()

        winner.symbol = PLAYER_X

        winner.name = "Player 1"

        self.game.is_game_over.return_value = (
            True
        )

        self.game.get_winner.return_value = (
            winner
        )

        self.game.get_winning_positions.return_value = [
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

        result = self.window._handle_game_end()

        self.assertTrue(
            result,
        )

        self.assertEqual(
            self.window.x_score,
            1,
        )

        self.statistics.record_win.assert_called_once_with(
            PLAYER_X,
            False,
        )

        self.game_board.highlight_cells.assert_called_once()

        mock_show_game_over.assert_called_once_with(
            STATUS_WINNER.format(
                winner.name,
            ),
        )

    @patch(
        "ui.main_window.DialogManager.ask_new_game",
        return_value=False,
    )
    @patch(
        "ui.main_window.DialogManager.show_game_over",
    )
    def test_handle_game_end_player_o_win(
        self,
        mock_show_game_over,
        mock_new_game,
    ) -> None:
        # Tests Player O winning

        winner = MagicMock()

        winner.symbol = PLAYER_O

        winner.name = "Player 2"

        self.game.is_game_over.return_value = (
            True
        )

        self.game.get_winner.return_value = (
            winner
        )

        self.game.get_winning_positions.return_value = [
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
        ]

        self.window._handle_game_end()

        self.assertEqual(
            self.window.o_score,
            1,
        )

        self.statistics.record_win.assert_called_once_with(
            PLAYER_O,
            False,
        )

        self.game_board.highlight_cells.assert_called_once()

    def test_handle_game_end_not_finished(
        self,
    ) -> None:
        # Tests calling the handler before
        # the game has ended

        self.game.is_game_over.return_value = (
            False
        )

        result = self.window._handle_game_end()

        self.assertFalse(
            result,
        )

    @patch.object(
        MainWindow,
        "_update_board",
    )
    @patch.object(
        MainWindow,
        "_handle_game_end",
    )
    def test_perform_ai_move(
        self,
        mock_handle_game_end,
        mock_update_board,
    ) -> None:
        # Tests a successful AI move

        self.game.is_game_over.return_value = (
            False
        )

        ai_player = MagicMock()

        ai_player.symbol = PLAYER_O

        opponent = MagicMock()

        opponent.symbol = PLAYER_X

        self.game.get_current_player.return_value = (
            ai_player
        )

        self.game.get_player_by_symbol.return_value = (
            opponent
        )

        self.ai.choose_move.return_value = (
            (
                1,
                1,
            )
        )

        self.window._perform_ai_move()

        self.ai.choose_move.assert_called_once()

        self.game.make_move.assert_called_once_with(
            1,
            1,
        )

        mock_update_board.assert_called_once()

        mock_handle_game_end.assert_called_once()

    def test_perform_ai_move_game_over(
        self,
    ) -> None:
        # Tests AI move after the game ends

        self.game.is_game_over.return_value = (
            True
        )

        self.window._perform_ai_move()

        self.ai.choose_move.assert_not_called()

    @patch.object(
        MainWindow,
        "_update_board",
    )
    @patch.object(
        MainWindow,
        "_handle_game_end",
    )
    def test_perform_ai_move_no_move(
        self,
        mock_handle_game_end,
        mock_update_board,
    ) -> None:
        # Tests when the AI has no move

        self.game.is_game_over.return_value = (
            False
        )
        ai_player = MagicMock()
        ai_player.symbol = PLAYER_O
        opponent = MagicMock()
        opponent.symbol = PLAYER_X
        self.game.get_current_player.return_value = (
            ai_player
        )
        self.game.get_player_by_symbol.return_value = (
            opponent
        )
        self.ai.choose_move.return_value = (
            None
        )
        self.window._perform_ai_move()
        self.game.make_move.assert_not_called()
        mock_update_board.assert_not_called()
        mock_handle_game_end.assert_not_called() 

    def test_new_game(
        self,
    ) -> None:
        # Tests starting a new game

        self.window.new_game()
        self.game.reset_board.assert_called_once()
        self.game_board.clear_board.assert_called_once()
        self.game_board.enable_board.assert_called_once()
        self.assertEqual(
            self.window.status_var.get(),
            STATUS_READY,
        )

    @patch(
        "ui.main_window.DialogManager.confirm_reset_scores",
        return_value=True,
    )
    def test_reset_scores(
        self,
        mock_confirm,
    ) -> None:
        # Tests resetting the session scores

        self.window.x_score = 5

        self.window.o_score = 4

        self.window.draws = 2

        self.window.reset_scores()

        self.assertEqual(
            self.window.x_score,
            0,
        )

        self.assertEqual(
            self.window.o_score,
            0,
        )

        self.assertEqual(
            self.window.draws,
            0,
        )

    @patch(
        "ui.main_window.DialogManager.confirm_reset_scores",
        return_value=False,
    )
    def test_reset_scores_cancelled(
        self,
        mock_confirm,
    ) -> None:
        # Tests cancelling score reset

        self.window.x_score = 7

        self.window.reset_scores()

        self.assertEqual(
            self.window.x_score,
            7,
        )

    def test_toggle_ai(
        self,
    ) -> None:
        # Tests enabling AI mode

        self.window.toggle_ai(
            True,
        )

        self.assertTrue(
            self.window.ai_enabled,
        )

        self.settings.set_setting.assert_called_once_with(
            "ai_enabled",
            True,
        )

        self.game_board.clear_board.assert_called_once()

        self.game_board.enable_board.assert_called_once()

    def test_set_ai_difficulty(
        self,
    ) -> None:
        # Tests changing AI difficulty

        self.window.set_ai_difficulty(
            "Impossible",
        )

        self.ai.set_difficulty.assert_called_once_with(
            "Impossible",
        )

        self.settings.set_setting.assert_called_once_with(
            "difficulty",
            "Impossible",
        )

    @patch(
        "ui.main_window.DialogManager.show_about",
    )
    def test_show_about(
        self,
        mock_show_about,
    ) -> None:
        # Tests displaying the About dialog

        self.window.show_about()
        mock_show_about.assert_called_once()

    @patch(
        "ui.main_window.DialogManager.show_statistics",
    )
    def test_show_statistics(
        self,
        mock_show_statistics,
    ) -> None:
        # Tests displaying the Statistics dialog

        self.window.show_statistics()
        mock_show_statistics.assert_called_once_with(
            self.window.x_score,
            self.window.o_score,
            self.window.draws,
        )

    def test_exit_application(
        self,
    ) -> None:
        # Tests closing the application

        self.window.exit_application()
        self.settings.save_settings.assert_called_once()
        self.statistics.save_statistics.assert_called_once()
        self.root.destroy.assert_called_once()

    def test_run(
        self,
    ) -> None:
        # Tests starting the Tkinter event loop
        
        self.window.run()
        self.root.mainloop.assert_called_once()


if __name__ == "__main__":
    unittest.main()

__all__ = [
    "TestMainWindow",
] 

