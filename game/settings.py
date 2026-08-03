# settings.py
# Loads settings from the settings.json file, provides methods for accessing
# and modifying settings, and saves any changes back to disk

from typing import Any

from game.constants import SETTINGS_FILE
from game.file_manager import FileManager
from game.validator import validate_settings


class SettingsManager:
    # Handles loading, saving and modifying application settings

    DEFAULT_SETTINGS = {
        "theme": "Light",
        "ai_enabled": False,
        "difficulty": "Medium",
        "sound_enabled": True,
        "animations_enabled": True,
    }

    def __init__(self) -> None:
        # Initializes the settings manager

        self.settings = {}

        self.load_settings()

    def load_settings(self) -> None:
        # Loads settings from the JSON file
        # Creates the file with default settings if it does not exist

        FileManager.create_file_if_missing(
            SETTINGS_FILE,
            self.DEFAULT_SETTINGS,
        )

        try:

            data = FileManager.load_json(
                SETTINGS_FILE,
            )

            if validate_settings(data):

                self.settings = data

            else:

                self.reset_defaults()

        except (
            FileNotFoundError,
            ValueError,
        ):

            self.reset_defaults()

    def save_settings(self) -> None:
        # Saves the current settings into the JSON file

        FileManager.save_json(
            SETTINGS_FILE,
            self.settings,
        )

    def get_setting(
        self,
        key: str,
    ) -> Any:
        # Returns the value of a setting

        return self.settings.get(key)

    def set_setting(
        self,
        key: str,
        value: Any,
    ) -> None:
        # Updates a setting if it is valid
        # and immediately saves the changes

        if key not in self.DEFAULT_SETTINGS:
            return

        updated_settings = self.settings.copy()

        updated_settings[key] = value

        if validate_settings(updated_settings):

            self.settings = updated_settings

            self.save_settings()

    def reset_defaults(self) -> None:
        # Restores the default settings

        self.settings = self.DEFAULT_SETTINGS.copy()

        self.save_settings()

    def get_all_settings(self) -> dict:
        # Returns every setting

        return self.settings.copy()


__all__ = [
    "SettingsManager",
] 

