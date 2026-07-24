# file_manager.py 
# Provides utility functions for creating, reading, writing 
# and resetting JSON files used by the application 

import json
from pathlib import Path
from typing import Any 
from game.constants import DATA_DIRECTORY 

def ensure_directory_exists(directory: Path) -> None: 
    # Creates a directory if it does not already exist 

    directory.mkdir(parents=True, exist_ok=True) 

def create_file_if_missing(file_path: Path, default_data: Any) -> None: 
    # Creates a JSON file with default data if it doesn't exist 

    ensure_directory_exists(DATA_DIRECTORY) 

    if not file_path.exists():
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(default_data, file, indent=4)


def load_json(file_path: Path) -> Any:
    # Loads JSON data from a file 
    # Raises FileNotFoundError & json.JSONDecodeError 

    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def save_json(file_path: Path, data: Any) -> None: 
    # Saves data to a JSON file 

    ensure_directory_exists(DATA_DIRECTORY) 
    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


def reset_json(file_path: Path, default_data: Any) -> None: 
    # Replaces the contents of a JSON file with the supplied default data 

    save_json(file_path, default_data) 

 