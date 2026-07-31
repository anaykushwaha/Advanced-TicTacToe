# settings.py 
# Loads settings from the settings.json file, provides methods to access and modify settings, 
# and saves any changes back to disk 


from game.file_manager import FileManager


class SettingsManager: 
    # Handles loading, saving and modifying application settings 

    DEFAULT_SETTINGS = {
        "theme": "Light",
        "ai_enabled": True,
        "difficulty": "Medium",
        "sound_enabled": True,
    }

    def __init__(self) -> None: 
        # Initializes the settings manager 

        self.settings = {}

        self.load_settings()

    def load_settings(self) -> None: 
        # Loads settings from the JSON file 

        data = FileManager.load_json(
            "data/settings.json"
        )

        if isinstance(data, dict):

            self.settings = data

        else:

            self.reset_defaults()

    def save_settings(self) -> None: 
        # Saves the current settings into the JSON file 

        FileManager.save_json(
            "data/settings.json",
            self.settings,
        )

    def get_setting(self, key: str): 
        # Returns the value of a setting 

        return self.settings.get(key)

    def set_setting(self, key: str, value) -> None: 
        # Updates a setting and saves it 

        self.settings[key] = value

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

