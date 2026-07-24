# constants.py 
# Stores project-wide constants used throughout the game 
# Easier to maintain and avoids hardcoding values throughout project 

from pathlib import Path

# Application Information

APP_NAME = "Advanced Tic Tac Toe"
APP_VERSION = "1.0.0"

# Project Directories

PROJECT_ROOT = Path(__file__).resolve().parent.parent

ASSETS_DIRECTORY = PROJECT_ROOT / "assets"
DATA_DIRECTORY = PROJECT_ROOT / "data"

AUDIO_DIRECTORY = ASSETS_DIRECTORY / "audio"
FONTS_DIRECTORY = ASSETS_DIRECTORY / "fonts"
ICONS_DIRECTORY = ASSETS_DIRECTORY / "icons"
IMAGES_DIRECTORY = ASSETS_DIRECTORY / "images"
LOGO_DIRECTORY = ASSETS_DIRECTORY / "logo"

# Data Files

SETTINGS_FILE = DATA_DIRECTORY / "settings.json"
STATISTICS_FILE = DATA_DIRECTORY / "statistics.json"

# Window Configuration

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 700

WINDOW_MIN_WIDTH = 700
WINDOW_MIN_HEIGHT = 550

# Board Configuration

BOARD_SIZE = 3

EMPTY_CELL = ""

PLAYER_X = "X"
PLAYER_O = "O"

# AI Difficulty Levels

AI_EASY = "Easy"
AI_MEDIUM = "Medium"
AI_IMPOSSIBLE = "Impossible"

AI_DIFFICULTIES = (
    AI_EASY,
    AI_MEDIUM,
    AI_IMPOSSIBLE,
)

# Themes

LIGHT_THEME = "Light"
DARK_THEME = "Dark"

DEFAULT_THEME = DARK_THEME

# Default Player Names

DEFAULT_PLAYER_ONE = "Player 1"
DEFAULT_PLAYER_TWO = "Player 2"

# Colors

BACKGROUND_COLOR = "#1E1E1E"
PRIMARY_COLOR = "#3A7AFE"
SECONDARY_COLOR = "#2ECC71"
TEXT_COLOR = "#FFFFFF"
GRID_COLOR = "#555555"
WIN_COLOR = "#FFD700"

# Fonts

TITLE_FONT = ("Segoe UI", 24, "bold")
BUTTON_FONT = ("Segoe UI", 12)
GAME_FONT = ("Segoe UI", 34, "bold")
SMALL_FONT = ("Segoe UI", 10)

# Default Settings

DEFAULT_SETTINGS = {
    "theme": DEFAULT_THEME,
    "sound": True,
    "difficulty": AI_MEDIUM,
    "player_one": DEFAULT_PLAYER_ONE,
    "player_two": DEFAULT_PLAYER_TWO,
}

# Default Statistics

DEFAULT_STATISTICS = {
    "games_played": 0,
    "player_one_wins": 0,
    "player_two_wins": 0,
    "draws": 0,
}

# Animation

ANIMATION_DELAY = 15

# Sound Files

BUTTON_CLICK_SOUND = AUDIO_DIRECTORY / "button_click.wav"
WIN_SOUND = AUDIO_DIRECTORY / "win.wav"
DRAW_SOUND = AUDIO_DIRECTORY / "draw.wav" 