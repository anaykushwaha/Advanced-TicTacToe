# minimax.py
# Implements the Minimax algorithm used by the Impossible AI

from typing import Optional, Tuple
from game.board import Board


def minimax(
    board: Board,
    ai_symbol: str,
    opponent_symbol: str,
    maximizing: bool,
    depth: int = 0,
) -> int:
    # Recursively evaluates every possible game state

    winner = board.check_winner()

    if winner == ai_symbol:
        return 10 - depth
    if winner == opponent_symbol:
        return depth - 10
    if board.is_draw():
        return 0
    available_moves = board.get_available_moves()
    if maximizing:
        best_score = float("-inf")
        for row, col in available_moves:
            board.set_cell(
                row,
                col,
                ai_symbol,
            )
            move_score = minimax(
                board,
                ai_symbol,
                opponent_symbol,
                False,
                depth + 1,
            )
            board.clear_cell(
                row,
                col,
            )
            best_score = max(
                best_score,
                move_score,
            )
        return best_score

    best_score = float("inf")
    for row, col in available_moves:
        board.set_cell(
            row,
            col,
            opponent_symbol,
        )
        move_score = minimax(
            board,
            ai_symbol,
            opponent_symbol,
            True,
            depth + 1,
        )
        board.clear_cell(
            row,
            col,
        )
        best_score = min(
            best_score,
            move_score,
        )
    return best_score


def find_best_move(
    board: Board,
    ai_symbol: str,
    opponent_symbol: str,
) -> Optional[Tuple[int, int]]:
    # Determines the best move for the AI
    # using the Minimax algorithm

    available_moves = board.get_available_moves()
    if not available_moves:
        return None
    best_move = None
    best_score = float("-inf")
    for row, col in available_moves:
        # Simulate the move

        board.set_cell(
            row,
            col,
            ai_symbol,
        )
        move_score = minimax(
            board,
            ai_symbol,
            opponent_symbol,
            maximizing=False,
            depth=1,
        )

        # Undo the move

        board.clear_cell(
            row,
            col,
        )

        # Keep the highest-scoring move

        if move_score > best_score:
            best_score = move_score
            best_move = (
                row,
                col,
            )
    return best_move


__all__ = [
    "minimax",
    "find_best_move",
] 
