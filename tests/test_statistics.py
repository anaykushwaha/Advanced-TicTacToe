# test_statistics.py
# Unit tests for statistics.py

import unittest
from unittest.mock import (
    MagicMock,
    patch, 
    Mock, 
)
from game.statistics import StatisticsManager


class TestStatisticsManager(unittest.TestCase):
    # Tests the StatisticsManager class

    @patch("game.statistics.validate_statistics")
    @patch("game.statistics.FileManager")
    def setUp(
        self,
        mock_file_manager,
        mock_validate_statistics,
    ) -> None:
        # Creates a fresh StatisticsManager before every test

        self.file_manager = mock_file_manager

        mock_validate_statistics.return_value = True

        self.statistics = StatisticsManager()

        self.statistics.statistics = (
            StatisticsManager.DEFAULT_STATISTICS.copy()
        )

    @patch("game.statistics.FileManager.create_file_if_missing")
    @patch("game.statistics.FileManager.load_json")
    @patch("game.statistics.validate_statistics")
    def test_initialization(
        self,
        mock_validate_statistics,
        mock_load_json,
        mock_create_file,
    ) -> None:
        # Tests creating the statistics manager

        mock_load_json.return_value = (
            StatisticsManager.DEFAULT_STATISTICS.copy()
        )

        mock_validate_statistics.return_value = True

        with patch.object(
            StatisticsManager,
            "load_statistics",
        ):

            manager = StatisticsManager()

        self.assertIsNotNone(
            manager.statistics,
        )

    @patch(
        "game.statistics.FileManager.create_file_if_missing",
    )
    @patch(
        "game.statistics.FileManager.load_json",
    )
    @patch(
        "game.statistics.validate_statistics",
    )
    def test_load_statistics_valid_data(
        self,
        mock_validate_statistics,
        mock_load_json,
        mock_create_file,
    ) -> None:
        # Tests loading valid statistics

        data = {
            "games_played": 10,
            "x_wins": 5,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 2,
        }

        mock_load_json.return_value = data

        mock_validate_statistics.return_value = True

        manager = StatisticsManager()

        self.assertEqual(
            manager.statistics,
            data,
        )

        mock_create_file.assert_called_once()

    @patch(
        "game.statistics.FileManager.create_file_if_missing",
    )
    @patch(
        "game.statistics.FileManager.load_json",
    )
    @patch(
        "game.statistics.validate_statistics",
    )
    def test_load_statistics_invalid_data(
        self,
        mock_validate_statistics,
        mock_load_json,
        mock_create_file,
    ) -> None:
        # Tests resetting statistics when loaded data is invalid

        mock_load_json.return_value = {
            "invalid": True,
        }

        mock_validate_statistics.return_value = False

        with patch.object(
            StatisticsManager,
            "reset_statistics",
        ) as mock_reset:

            manager = StatisticsManager()

            mock_reset.assert_called_once()

        self.assertIsNotNone(
            manager.statistics,
        )

    @patch(
        "game.statistics.FileManager.create_file_if_missing",
    )
    @patch(
        "game.statistics.FileManager.load_json",
        side_effect=FileNotFoundError,
    )
    @patch(
        "game.statistics.validate_statistics",
    )
    def test_load_statistics_file_not_found(
        self,
        mock_validate_statistics,
        mock_load_json,
        mock_create_file,
    ) -> None:
        # Tests resetting statistics when the file is missing

        with patch.object(
            StatisticsManager,
            "reset_statistics",
        ) as mock_reset:

            StatisticsManager()

            mock_reset.assert_called_once()

    @patch(
        "game.statistics.FileManager.create_file_if_missing",
    )
    @patch(
        "game.statistics.FileManager.load_json",
        side_effect=ValueError,
    )
    @patch(
        "game.statistics.validate_statistics",
    )
    def test_load_statistics_invalid_json(
        self,
        mock_validate_statistics,
        mock_load_json,
        mock_create_file,
    ) -> None:
        # Tests resetting statistics when the JSON is invalid

        with patch.object(
            StatisticsManager,
            "reset_statistics",
        ) as mock_reset:

            StatisticsManager()

            mock_reset.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_save_statistics(
        self,
        mock_save_json,
    ) -> None:
        # Tests saving the current statistics

        self.statistics.save_statistics()

        mock_save_json.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_record_x_win(
        self,
        mock_save_json,
    ) -> None:
        # Tests recording a Player X win

        self.statistics.record_win(
            "X",
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "x_wins",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "o_wins",
            ),
            0,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "ai_wins",
            ),
            0,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_record_o_win(
        self,
        mock_save_json,
    ) -> None:
        # Tests recording a Player O win

        self.statistics.record_win(
            "O",
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "o_wins",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "ai_wins",
            ),
            0,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_record_ai_win(
        self,
        mock_save_json,
    ) -> None:
        # Tests recording an AI win

        self.statistics.record_win(
            "O",
            True,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "ai_wins",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "o_wins",
            ),
            0,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_record_invalid_win(
        self,
        mock_save_json,
    ) -> None:
        # Tests ignoring an invalid winner symbol

        self.statistics.record_win(
            "A",
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            0,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "x_wins",
            ),
            0,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "o_wins",
            ),
            0,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "ai_wins",
            ),
            0,
        )

        mock_save_json.assert_not_called()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_record_draw(
        self,
        mock_save_json,
    ) -> None:
        # Tests recording a draw

        self.statistics.record_draw()

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "draws",
            ),
            1,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_get_statistic(
        self,
        mock_save_json,
    ) -> None:
        # Tests retrieving an individual statistic

        self.statistics.statistics[
            "games_played"
        ] = 15

        result = self.statistics.get_statistic(
            "games_played",
        )

        self.assertEqual(
            result,
            15,
        )

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_get_missing_statistic(
        self,
        mock_save_json,
    ) -> None:
        # Tests retrieving a statistic that does not exist

        result = self.statistics.get_statistic(
            "unknown",
        )

        self.assertIsNone(
            result,
        )

    def test_get_all_statistics(
        self,
    ) -> None:
        # Tests retrieving all statistics

        result = (
            self.statistics.get_all_statistics()
        )

        self.assertEqual(
            result,
            StatisticsManager.DEFAULT_STATISTICS,
        )

        self.assertIsNot(
            result,
            self.statistics.statistics,
        )

    def test_get_all_statistics_returns_copy(
        self,
    ) -> None:
        # Tests that returned statistics are independent

        result = (
            self.statistics.get_all_statistics()
        )

        result["games_played"] = 100

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            0,
        )

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_reset_statistics(
        self,
        mock_save_json,
    ) -> None:
        # Tests resetting all statistics

        self.statistics.statistics = {
            "games_played": 10,
            "x_wins": 5,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 2,
        }

        self.statistics.reset_statistics()

        self.assertEqual(
            self.statistics.statistics,
            StatisticsManager.DEFAULT_STATISTICS,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.statistics.FileManager.save_json",
    )
    def test_multiple_games(
        self,
        mock_save_json,
    ) -> None:
        # Tests recording multiple completed games

        self.statistics.record_win(
            "X",
        )

        self.statistics.record_win(
            "O",
        )

        self.statistics.record_win(
            "O",
            True,
        )

        self.statistics.record_draw()

        self.assertEqual(
            self.statistics.get_statistic(
                "games_played",
            ),
            4,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "x_wins",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "o_wins",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "ai_wins",
            ),
            1,
        )

        self.assertEqual(
            self.statistics.get_statistic(
                "draws",
            ),
            1,
        )

        self.assertEqual(
            mock_save_json.call_count,
            4,
        )


if __name__ == "__main__":
    unittest.main()


__all__ = [
    "TestStatisticsManager",
] 

