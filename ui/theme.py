"""
theme.py

Contains all visual constants used by the Tkinter interface.
Keeping colors, fonts, dimensions, and spacing in one place
makes the interface easier to maintain and customize.
"""

# Window Configuration

WINDOW_TITLE = "Advanced Tic Tac Toe"

WINDOW_WIDTH = 700
WINDOW_HEIGHT = 850

WINDOW_RESIZABLE = False

# Colors

BACKGROUND_COLOR = "#F4F6F8"

PRIMARY_COLOR = "#1E88E5"
SECONDARY_COLOR = "#1565C0"

SUCCESS_COLOR = "#43A047"
WARNING_COLOR = "#FB8C00"
ERROR_COLOR = "#E53935"

TEXT_COLOR = "#212121"
LIGHT_TEXT_COLOR = "#757575"

BOARD_BACKGROUND = "#FFFFFF"

BUTTON_COLOR = "#FFFFFF"
BUTTON_HOVER_COLOR = "#E3F2FD"

GRID_COLOR = "#D0D0D0"

X_COLOR = "#1976D2"
O_COLOR = "#D32F2F"

WIN_HIGHLIGHT_COLOR = "#A5D6A7"

# Fonts

TITLE_FONT = (
    "Segoe UI",
    24,
    "bold",
)

HEADER_FONT = (
    "Segoe UI",
    16,
    "bold",
)

BODY_FONT = (
    "Segoe UI",
    12,
)

BUTTON_FONT = (
    "Segoe UI",
    12,
    "bold",
)

BOARD_FONT = (
    "Segoe UI",
    34,
    "bold",
)

SMALL_FONT = (
    "Segoe UI",
    10,
)

# Board Configuration

BOARD_SIZE = 3

CELL_WIDTH = 4
CELL_HEIGHT = 2

BOARD_PADDING = 20

CELL_PADDING = 4

# Button Configuration

DEFAULT_BUTTON_WIDTH = 15
DEFAULT_BUTTON_HEIGHT = 2

# Layout Spacing

OUTER_PADDING = 20

SECTION_SPACING = 15

LABEL_PADDING = 5

BUTTON_PADDING = 10

# Scoreboard

SCORE_LABEL_WIDTH = 15

# Status Messages

STATUS_READY = "Ready to Play"

STATUS_PLAYER_TURN = "{}'s Turn"

STATUS_DRAW = "It's a Draw!"

STATUS_WINNER = "{} Wins!"

STATUS_AI_THINKING = "AI is Thinking..."

# Difficulty Labels

DIFFICULTY_EASY = "Easy"

DIFFICULTY_MEDIUM = "Medium"

DIFFICULTY_IMPOSSIBLE = "Impossible"

# Dialog Titles

GAME_OVER_TITLE = "Game Over"

RESET_TITLE = "Reset Game"

ABOUT_TITLE = "About"

STATISTICS_TITLE = "Statistics"

# Miscellaneous

PLAYER_X = "X"

PLAYER_O = "O"

EMPTY_STRING = ""

# Module Exports

__all__ = [
    # Window
    "WINDOW_TITLE",
    "WINDOW_WIDTH",
    "WINDOW_HEIGHT",
    "WINDOW_RESIZABLE",

    # Colors
    "BACKGROUND_COLOR",
    "PRIMARY_COLOR",
    "SECONDARY_COLOR",
    "SUCCESS_COLOR",
    "WARNING_COLOR",
    "ERROR_COLOR",
    "TEXT_COLOR",
    "LIGHT_TEXT_COLOR",
    "BOARD_BACKGROUND",
    "BUTTON_COLOR",
    "BUTTON_HOVER_COLOR",
    "GRID_COLOR",
    "X_COLOR",
    "O_COLOR",
    "WIN_HIGHLIGHT_COLOR",

    # Fonts
    "TITLE_FONT",
    "HEADER_FONT",
    "BODY_FONT",
    "BUTTON_FONT",
    "BOARD_FONT",
    "SMALL_FONT",

    # Board
    "BOARD_SIZE",
    "CELL_WIDTH",
    "CELL_HEIGHT",
    "BOARD_PADDING",
    "CELL_PADDING",

    # Buttons
    "DEFAULT_BUTTON_WIDTH",
    "DEFAULT_BUTTON_HEIGHT",

    # Layout
    "OUTER_PADDING",
    "SECTION_SPACING",
    "LABEL_PADDING",
    "BUTTON_PADDING",

    # Scoreboard
    "SCORE_LABEL_WIDTH",

    # Status
    "STATUS_READY",
    "STATUS_PLAYER_TURN",
    "STATUS_DRAW",
    "STATUS_WINNER",
    "STATUS_AI_THINKING",

    # Difficulty
    "DIFFICULTY_EASY",
    "DIFFICULTY_MEDIUM",
    "DIFFICULTY_IMPOSSIBLE",

    # Dialogs
    "GAME_OVER_TITLE",
    "RESET_TITLE",
    "ABOUT_TITLE",
    "STATISTICS_TITLE",

    # Misc
    "PLAYER_X",
    "PLAYER_O",
    "EMPTY_STRING",
]
