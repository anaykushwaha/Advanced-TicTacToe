# validator.py 
# Contains reusable validation functions used throughout the game project 

from typing import Any 
from game.constants import (
    AI_DIFFICULTIES,
    BOARD_SIZE,
    DARK_THEME,
    LIGHT_THEME,
)


def is_valid_position(row: int, col: int) -> bool: 
    # Check whether a board position is within bounds 

    return (
        0 <= row < BOARD_SIZE and
        0 <= col < BOARD_SIZE
    ) 

def is_valid_player_name(name: str) -> bool: 
    # Validates a player's name 
    # Rules: 
    # 1. Must be a string 
    # 2. Cannot be empty 
    # 3. Maximum length is 20 characters 

    if not isinstance(name, str):
        return False
    name = name.strip()
    return 1 <= len(name) <= 20

def is_valid_theme(theme: str) -> bool: 
    # Checks whether a theme exists 

    return theme in (LIGHT_THEME, DARK_THEME) 

def is_valid_difficulty(difficulty: str) -> bool: 
    # Checks whether an AI difficulty is supported 

    return difficulty in AI_DIFFICULTIES 

def is_boolean(value: Any) -> bool: 
    # Checks whether a value is a boolean 

    return isinstance(value, bool) 

def is_integer(value: Any) -> bool: 
    # Checks whether a value is an integer 

    return isinstance(value, int) 

def validate_statistics(data: dict) -> bool: 
    # Validates the structure of the statistics dictionary 

    required_keys = {
        "games_played",
        "player_one_wins",
        "player_two_wins",
        "draws",
    }

    if not isinstance(data, dict):
        return False

    if set(data.keys()) != required_keys:
        return False

    return all(
        is_integer(value) and value >= 0
        for value in data.values()
    )

def validate_settings(data: dict) -> bool: 
    # Validates the sturcture of the settings dictionary 

    required_keys = {
        "theme",
        "sound",
        "difficulty",
        "player_one",
        "player_two",
    }

    if not isinstance(data, dict):
        return False

    if set(data.keys()) != required_keys:
        return False

    if not is_valid_theme(data["theme"]):
        return False

    if not is_boolean(data["sound"]):
        return False

    if not is_valid_difficulty(data["difficulty"]):
        return False

    if not is_valid_player_name(data["player_one"]):
        return False

    if not is_valid_player_name(data["player_two"]):
        return False

    return True 

