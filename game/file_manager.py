# file_manager.py
# Provides utility methods for creating, reading, writing and resetting
# JSON files used by the application

import json
from pathlib import Path
from typing import Any

from game.constants import DATA_DIRECTORY


class FileManager:
    # Utility class responsible for all JSON file operations
    # used throughout the project

    @staticmethod
    def ensure_directory_exists(
        directory: Path,
    ) -> None:
        # Creates the supplied directory if it does not exist

        directory.mkdir(
            parents=True,
            exist_ok=True,
        )

    @staticmethod
    def create_file_if_missing(
        file_path: str | Path,
        default_data: Any,
    ) -> None:
        # Creates a JSON file containing the supplied default data
        # if the file does not already exist

        file_path = Path(file_path)

        FileManager.ensure_directory_exists(
            file_path.parent,
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
        # Loads JSON data from a file
        # Raises FileNotFoundError if the file does not exist
        # Raises ValueError if the JSON is invalid

        file_path = Path(file_path)

        with open(
            file_path,
            "r",
            encoding="utf-8",
        ) as file:

            try:
                return json.load(file)

            except json.JSONDecodeError as error:
                raise ValueError(
                    f"Invalid JSON file: {file_path}"
                ) from error

    @staticmethod
    def save_json(
        file_path: str | Path,
        data: Any,
    ) -> None:
        # Saves data to a JSON file

        file_path = Path(file_path)

        FileManager.ensure_directory_exists(
            file_path.parent,
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
        # Replaces the contents of a JSON file
        # with the supplied default data

        FileManager.save_json(
            file_path,
            default_data,
        )

    @staticmethod
    def file_exists(
        file_path: str | Path,
    ) -> bool:
        # Checks whether a file exists

        return Path(file_path).exists()

    @staticmethod
    def delete_file(
        file_path: str | Path,
    ) -> None:
        # Deletes a file if it exists

        file_path = Path(file_path)

        if file_path.exists():
            file_path.unlink()


__all__ = [
    "FileManager",
] 

