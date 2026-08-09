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
    # Checks whether a board position is within the board boundaries 

    return (
        0 <= row < BOARD_SIZE
        and
        0 <= col < BOARD_SIZE
    )


def is_valid_player_name(name: str) -> bool: 
    # Validates a player's name 

    if not isinstance(name, str):
        return False

    name = name.strip()

    return (
        1 <= len(name) <= 20
        and any(
            character.isalnum()
            for character in name
        )
    )


def is_valid_theme(theme: str) -> bool: 
    # Checks whether the supplied theme is supported 

    return theme in (
        LIGHT_THEME,
        DARK_THEME,
    )


def is_valid_difficulty(difficulty: str) -> bool: 
    # Checks whether the supplied AI difficulty exists 

    return difficulty in AI_DIFFICULTIES


def is_boolean(value: Any) -> bool: 
    # Checks whether the supplied value is a boolean 

    return isinstance(
        value,
        bool,
    )


def is_integer(value: Any) -> bool: 
    # Checks whether the supplied value is an integer 

    return (
        isinstance(value, int)
        and not isinstance(value, bool)
    )


def validate_statistics(data: dict) -> bool: 
    # Validates the structure of the statistics dictionary 

    if not isinstance(data, dict):
        return False

    required_keys = {
        "games_played",
        "x_wins",
        "o_wins",
        "ai_wins",
        "draws",
    }

    if set(data.keys()) != required_keys:
        return False

    return all(
        is_integer(value)
        and value >= 0
        for value in data.values()
    )


def validate_settings(data: dict) -> bool: 
    # Validates the structure of the settings dictionary 

    if not isinstance(data, dict):
        return False

    required_keys = {
        "theme",
        "ai_enabled",
        "difficulty",
        "sound_enabled",
        "animations_enabled",
    }

    if set(data.keys()) != required_keys:
        return False

    if not is_valid_theme(
        data["theme"],
    ):
        return False

    if not is_boolean(
        data["ai_enabled"],
    ):
        return False

    if not is_valid_difficulty(
        data["difficulty"],
    ):
        return False

    if not is_boolean(
        data["sound_enabled"],
    ):
        return False

    if not is_boolean(
        data["animations_enabled"],
    ):
        return False

    return True


__all__ = [
    "is_valid_position",
    "is_valid_player_name",
    "is_valid_theme",
    "is_valid_difficulty",
    "is_boolean",
    "is_integer",
    "validate_statistics",
    "validate_settings",
] 

