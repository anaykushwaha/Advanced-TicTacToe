# test_validator.py
# Unit tests for validator.py

import unittest
from game.constants import (
    AI_DIFFICULTIES,
    DARK_THEME,
    LIGHT_THEME,
)
from game.validator import (
    is_valid_position,
    is_valid_player_name,
    is_valid_theme,
    is_valid_difficulty,
    is_boolean,
    is_integer,
    validate_statistics,
    validate_settings,
)


class TestValidator(unittest.TestCase):
    # Tests the validation functions

    def test_is_valid_position_valid_positions(
        self,
    ) -> None:
        # Tests valid board positions

        self.assertTrue(
            is_valid_position(
                0,
                0,
            )
        )

        self.assertTrue(
            is_valid_position(
                1,
                1,
            )
        )

        self.assertTrue(
            is_valid_position(
                2,
                2,
            )
        )

    def test_is_valid_position_invalid_positions(
        self,
    ) -> None:
        # Tests positions outside the board

        self.assertFalse(
            is_valid_position(
                -1,
                0,
            )
        )

        self.assertFalse(
            is_valid_position(
                0,
                -1,
            )
        )

        self.assertFalse(
            is_valid_position(
                3,
                0,
            )
        )

        self.assertFalse(
            is_valid_position(
                0,
                3,
            )
        )

    def test_is_valid_player_name_valid_names(
        self,
    ) -> None:
        # Tests valid player names

        self.assertTrue(
            is_valid_player_name(
                "Alex",
            )
        )

        self.assertTrue(
            is_valid_player_name(
                "Player 1",
            )
        )

        self.assertTrue(
            is_valid_player_name(
                "A",
            )
        )

        self.assertTrue(
            is_valid_player_name(
                "123",
            )
        )

    def test_is_valid_player_name_strips_whitespace(
        self,
    ) -> None:
        # Tests names with surrounding whitespace

        self.assertTrue(
            is_valid_player_name(
                "  Alex  ",
            )
        )

    def test_is_valid_player_name_empty_name(
        self,
    ) -> None:
        # Tests empty player names

        self.assertFalse(
            is_valid_player_name(
                "",
            )
        )

        self.assertFalse(
            is_valid_player_name(
                "   ",
            )
        )

    def test_is_valid_player_name_name_too_long(
        self,
    ) -> None:
        # Tests names longer than twenty characters

        self.assertFalse(
            is_valid_player_name(
                "A" * 21,
            )
        )

    def test_is_valid_player_name_name_at_maximum_length(
        self,
    ) -> None:
        # Tests a name containing exactly twenty characters

        self.assertTrue(
            is_valid_player_name(
                "A" * 20,
            )
        )

    def test_is_valid_player_name_no_alphanumeric_characters(
        self,
    ) -> None:
        # Tests names containing no alphanumeric characters

        self.assertFalse(
            is_valid_player_name(
                "!!!",
            )
        )

        self.assertFalse(
            is_valid_player_name(
                "---",
            )
        )

    def test_is_valid_player_name_non_string(
        self,
    ) -> None:
        # Tests non-string player names

        self.assertFalse(
            is_valid_player_name(
                123,
            )
        )

        self.assertFalse(
            is_valid_player_name(
                None,
            )
        )

        self.assertFalse(
            is_valid_player_name(
                True,
            )
        )

    def test_is_valid_theme_valid_themes(
        self,
    ) -> None:
        # Tests supported themes

        self.assertTrue(
            is_valid_theme(
                LIGHT_THEME,
            )
        )

        self.assertTrue(
            is_valid_theme(
                DARK_THEME,
            )
        )

    def test_is_valid_theme_invalid_themes(
        self,
    ) -> None:
        # Tests unsupported themes

        self.assertFalse(
            is_valid_theme(
                "Blue",
            )
        )

        self.assertFalse(
            is_valid_theme(
                "",
            )
        )

        self.assertFalse(
            is_valid_theme(
                None,
            )
        )

    def test_is_valid_difficulty_valid_difficulties(
        self,
    ) -> None:
        # Tests supported AI difficulties

        for difficulty in AI_DIFFICULTIES:

            self.assertTrue(
                is_valid_difficulty(
                    difficulty,
                )
            )

    def test_is_valid_difficulty_invalid_difficulties(
        self,
    ) -> None:
        # Tests unsupported AI difficulties

        self.assertFalse(
            is_valid_difficulty(
                "Invalid",
            )
        )

        self.assertFalse(
            is_valid_difficulty(
                "",
            )
        )

        self.assertFalse(
            is_valid_difficulty(
                None,
            )
        )

    def test_is_boolean_valid_values(
        self,
    ) -> None:
        # Tests valid boolean values

        self.assertTrue(
            is_boolean(
                True,
            )
        )

        self.assertTrue(
            is_boolean(
                False,
            )
        )

    def test_is_boolean_invalid_values(
        self,
    ) -> None:
        # Tests non-boolean values

        self.assertFalse(
            is_boolean(
                1,
            )
        )

        self.assertFalse(
            is_boolean(
                0,
            )
        )

        self.assertFalse(
            is_boolean(
                "True",
            )
        )

        self.assertFalse(
            is_boolean(
                None,
            )
        )

    def test_is_integer_valid_values(
        self,
    ) -> None:
        # Tests valid integer values

        self.assertTrue(
            is_integer(
                0,
            )
        )

        self.assertTrue(
            is_integer(
                10,
            )
        )

        self.assertTrue(
            is_integer(
                -5,
            )
        )

    def test_is_integer_invalid_values(
        self,
    ) -> None:
        # Tests values that are not integers

        self.assertFalse(
            is_integer(
                1.5,
            )
        )

        self.assertFalse(
            is_integer(
                "10",
            )
        )

        self.assertFalse(
            is_integer(
                None,
            )
        )

    def test_is_integer_rejects_boolean(
        self,
    ) -> None:
        # Tests that booleans are not treated as integers

        self.assertFalse(
            is_integer(
                True,
            )
        )

        self.assertFalse(
            is_integer(
                False,
            )
        )

    def test_validate_statistics_valid_data(
        self,
    ) -> None:
        # Tests a valid statistics dictionary

        data = {
            "games_played": 10,
            "x_wins": 5,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 2,
        }

        self.assertTrue(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_default_data(
        self,
    ) -> None:
        # Tests the default statistics structure

        data = {
            "games_played": 0,
            "x_wins": 0,
            "o_wins": 0,
            "ai_wins": 0,
            "draws": 0,
        }

        self.assertTrue(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_missing_key(
        self,
    ) -> None:
        # Tests statistics with a missing key

        data = {
            "games_played": 10,
            "x_wins": 5,
            "o_wins": 3,
            "ai_wins": 2,
        }

        self.assertFalse(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_extra_key(
        self,
    ) -> None:
        # Tests statistics containing an unexpected key

        data = {
            "games_played": 10,
            "x_wins": 5,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 2,
            "extra": 1,
        }

        self.assertFalse(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_negative_value(
        self,
    ) -> None:
        # Tests statistics containing a negative value

        data = {
            "games_played": 10,
            "x_wins": -1,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 2,
        }

        self.assertFalse(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_non_integer_value(
        self,
    ) -> None:
        # Tests statistics containing a non-integer value

        data = {
            "games_played": 10,
            "x_wins": 5,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 1.5,
        }

        self.assertFalse(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_boolean_value(
        self,
    ) -> None:
        # Tests statistics containing a boolean value

        data = {
            "games_played": 10,
            "x_wins": True,
            "o_wins": 3,
            "ai_wins": 2,
            "draws": 2,
        }

        self.assertFalse(
            validate_statistics(
                data,
            )
        )

    def test_validate_statistics_non_dictionary(
        self,
    ) -> None:
        # Tests non-dictionary statistics data

        self.assertFalse(
            validate_statistics(
                []
            )
        )

        self.assertFalse(
            validate_statistics(
                None
            )
        )

        self.assertFalse(
            validate_statistics(
                "statistics"
            )
        )

    def test_validate_settings_valid_data(
        self,
    ) -> None:
        # Tests a valid settings dictionary

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": False,
            "difficulty": "Medium",
            "sound_enabled": True,
            "animations_enabled": True,
        }

        self.assertTrue(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_dark_theme(
        self,
    ) -> None:
        # Tests settings using the dark theme

        data = {
            "theme": DARK_THEME,
            "ai_enabled": True,
            "difficulty": "Impossible",
            "sound_enabled": False,
            "animations_enabled": False,
        }

        self.assertTrue(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_missing_key(
        self,
    ) -> None:
        # Tests settings with a missing key

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": False,
            "difficulty": "Medium",
            "sound_enabled": True,
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_extra_key(
        self,
    ) -> None:
        # Tests settings containing an unexpected key

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": False,
            "difficulty": "Medium",
            "sound_enabled": True,
            "animations_enabled": True,
            "extra_setting": True,
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_invalid_theme(
        self,
    ) -> None:
        # Tests settings with an unsupported theme

        data = {
            "theme": "Blue",
            "ai_enabled": False,
            "difficulty": "Medium",
            "sound_enabled": True,
            "animations_enabled": True,
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_invalid_ai_enabled(
        self,
    ) -> None:
        # Tests settings with a non-boolean AI value

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": "True",
            "difficulty": "Medium",
            "sound_enabled": True,
            "animations_enabled": True,
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_invalid_difficulty(
        self,
    ) -> None:
        # Tests settings with an unsupported difficulty

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": False,
            "difficulty": "Extreme",
            "sound_enabled": True,
            "animations_enabled": True,
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_invalid_sound_enabled(
        self,
    ) -> None:
        # Tests settings with a non-boolean sound setting

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": False,
            "difficulty": "Medium",
            "sound_enabled": 1,
            "animations_enabled": True,
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_invalid_animations_enabled(
        self,
    ) -> None:
        # Tests settings with a non-boolean animation setting

        data = {
            "theme": LIGHT_THEME,
            "ai_enabled": False,
            "difficulty": "Medium",
            "sound_enabled": True,
            "animations_enabled": "True",
        }

        self.assertFalse(
            validate_settings(
                data,
            )
        )

    def test_validate_settings_non_dictionary(
        self,
    ) -> None:
        # Tests non-dictionary settings data

        self.assertFalse(
            validate_settings(
                []
            )
        )

        self.assertFalse(
            validate_settings(
                None
            )
        )

        self.assertFalse(
            validate_settings(
                "settings"
            )
        )


if __name__ == "__main__":
    unittest.main()


__all__ = [
    "TestValidator",
] 

