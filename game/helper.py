# helper.py 
# Contains reusable helper functions that are used throughout the game 
# These functions perform common tasks such as creating game boards, 
# formatting data, validating positions and generating useful values 
# for multiple modules to share 

from pathlib import Path 
from typing import List, Tuple 
from game.constants import BOARD_SIZE, EMPTY_CELL 

def create_empty_board() -> List[List[str]]: 
    # Creates and returns a new empty board 

    return [
        [EMPTY_CELL for _ in range(BOARD_SIZE)] 
        for _ in range(BOARD_SIZE) 
    ] 

def get_available_moves(board: List[List[str]]) -> List[Tuple[int, int]]: 
    # Returns all empty positions on the board 
    # Args: board - the current game board 
    # Returns: list of (row, column) tuples representing empty cells 

    available_moves = [] 

    for row in range(BOARD_SIZE): 
        for col in range(BOARD_SIZE): 
            if board[row][col] == EMPTY_CELL: 
                available_moves.append((row, col)) 
    return available_moves 

def is_board_full(board: List[List[str]]) -> bool: 
    # Checks whether every board cell has been filled 
    # Args: board - the current game board 
    # Returns True if no empty cells remain, otherwise False 

    return len(get_available_moves(board)) == 0 

def format_time(seconds: int) -> str: 
    # Convert seconds into MM:SS format 
    # Args: seconds - total number of seconds 
    # Returns formatted time string 

    minutes = seconds // 60 
    remaining_seconds = seconds % 60 
    return f"{minutes:02}:{remaining_seconds:02}" 

def get_project_root() -> Path: 
    # Returns the project's root directory 

    return Path(__file__).resolve().parent.parent 

def clamp(value: int, minimum: int, maximum: int) -> int: 
    # Restricts a number so it stays within a given range 

    return max(minimum, min(value, maximum)) 

def opposite_player(symbol: str) -> str: 
    # Returns the opposite player's symbol  

    return "O" if symbol == "X" else "X" 

