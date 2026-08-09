# test_settings.py
# Unit tests for settings.py

import unittest
from unittest.mock import (
    patch,
    MagicMock, 
    Mock, 
)

from game.settings import (
    SettingsManager,
)


class TestSettingsManager(unittest.TestCase):
    # Tests the SettingsManager class

    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_initialization(
        self,
        mock_create_file,
        mock_load_json,
    ) -> None:
        # Tests creating a settings manager

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        self.assertEqual(
            manager.settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

        mock_create_file.assert_called_once()

        mock_load_json.assert_called_once()

    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_load_settings_valid_data(
        self,
        mock_create_file,
        mock_load_json,
    ) -> None:
        # Tests loading valid settings

        settings = {
            "theme": "Dark",
            "ai_enabled": True,
            "difficulty": "Impossible",
            "sound_enabled": False,
            "animations_enabled": False,
        }

        mock_load_json.return_value = settings

        manager = SettingsManager()

        self.assertEqual(
            manager.settings,
            settings,
        )

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_load_settings_invalid_data(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests resetting to defaults when settings are invalid

        mock_load_json.return_value = {
            "invalid": True,
        }

        manager = SettingsManager()

        self.assertEqual(
            manager.settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
        side_effect=ValueError,
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_load_settings_invalid_json(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests resetting to defaults when JSON is invalid

        manager = SettingsManager()

        self.assertEqual(
            manager.settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
        side_effect=FileNotFoundError,
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_load_settings_file_not_found(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests resetting to defaults when the file is missing

        manager = SettingsManager()

        self.assertEqual(
            manager.settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_save_settings(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests saving the current settings

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        mock_save_json.reset_mock()

        manager.save_settings()

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_get_setting(
        self,
        mock_create_file,
        mock_load_json,
    ) -> None:
        # Tests retrieving a setting

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        self.assertEqual(
            manager.get_setting(
                "theme",
            ),
            "Light",
        )

        self.assertEqual(
            manager.get_setting(
                "ai_enabled",
            ),
            False,
        )

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_get_setting_missing_key(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests retrieving a setting that does not exist

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        self.assertIsNone(
            manager.get_setting(
                "missing_key",
            ),
        )

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_set_setting(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests changing a valid setting

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        manager.set_setting(
            "theme",
            "Dark",
        )

        self.assertEqual(
            manager.get_setting(
                "theme",
            ),
            "Dark",
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_set_setting_ai_enabled(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests enabling AI mode

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        manager.set_setting(
            "ai_enabled",
            True,
        )

        self.assertTrue(
            manager.get_setting(
                "ai_enabled",
            ),
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_set_setting_invalid_key(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests ignoring an unknown setting key

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        manager.set_setting(
            "unknown_setting",
            True,
        )

        self.assertEqual(
            manager.settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

        mock_save_json.assert_not_called()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_set_setting_invalid_value(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests rejecting an invalid setting value

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        manager.set_setting(
            "ai_enabled",
            "yes",
        )

        self.assertEqual(
            manager.get_setting(
                "ai_enabled",
            ),
            False,
        )

        mock_save_json.assert_not_called()

    @patch(
        "game.settings.FileManager.save_json",
    )
    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_reset_defaults(
        self,
        mock_create_file,
        mock_load_json,
        mock_save_json,
    ) -> None:
        # Tests restoring the default settings

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        manager.settings["theme"] = "Dark"

        mock_save_json.reset_mock()

        manager.reset_defaults()

        self.assertEqual(
            manager.settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

        mock_save_json.assert_called_once()

    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_get_all_settings(
        self,
        mock_create_file,
        mock_load_json,
    ) -> None:
        # Tests retrieving all settings

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        settings = manager.get_all_settings()

        self.assertEqual(
            settings,
            SettingsManager.DEFAULT_SETTINGS,
        )

    @patch(
        "game.settings.FileManager.load_json",
    )
    @patch(
        "game.settings.FileManager.create_file_if_missing",
    )
    def test_get_all_settings_returns_copy(
        self,
        mock_create_file,
        mock_load_json,
    ) -> None:
        # Tests that get_all_settings returns a copy

        mock_load_json.return_value = (
            SettingsManager.DEFAULT_SETTINGS.copy()
        )

        manager = SettingsManager()

        settings = manager.get_all_settings()

        settings["theme"] = "Dark"

        self.assertEqual(
            manager.get_setting(
                "theme",
            ),
            "Light",
        )


if __name__ == "__main__":
    unittest.main()


__all__ = [
    "TestSettingsManager",
] 

