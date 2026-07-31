# file_manager.py 
# Provides utility methods for creating, reading, writing and resetting 
# JSON files used by the application 

import json
from pathlib import Path
from typing import Any

from game.constants import DATA_DIRECTORY


class FileManager: 
    # Utility class responsible for all JSON file operations used throughout the project 

    @staticmethod
    def ensure_directory_exists(
        directory: Path,
    ) -> None: 
        # Creates the directory if it doesn't exist 

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def create_file_if_missing(
        file_path: Path,
        default_data: Any,
    ) -> None: 
        # Creates a JSON file containing the supplied default data 
        # if it doesn't already exist 

        FileManager.ensure_directory_exists(
            DATA_DIRECTORY
        )

        if not file_path.exists():

            with open(
                file_path,
                "w",
                encoding="utf-8",
            ) as file:

                json.dump(
                    default_data,
                    file,
                    indent=4,
                )

    @staticmethod
    def load_json(
        file_path: str | Path,
    ) -> Any: 
        # Loads JSON daa from a file 

        file_path = Path(file_path)

        FileManager.create_file_if_missing(
            file_path,
            {},
        )

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            return json.load(file)

    @staticmethod
    def save_json(
        file_path: str | Path,
        data: Any,
    ) -> None: 
        # Saves data to a JSON file 

        file_path = Path(file_path)

        FileManager.ensure_directory_exists(
            DATA_DIRECTORY
        )

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                indent=4,
            )

    @staticmethod
    def reset_json(
        file_path: str | Path,
        default_data: Any,
    ) -> None: 
        # Replaces the contents of a JSON file with the supplied default data 

        FileManager.save_json(
            file_path,
            default_data,
        )


__all__ = [
    "FileManager",
] 

