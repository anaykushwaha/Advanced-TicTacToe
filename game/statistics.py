# statistics.py 
# Records wins, draws and games played, allowing statistics to persist between application sessions 

from game.file_manager import FileManager


class StatisticsManager: 
    # Handles loading, saving, updating and resetting game statistics 

    DEFAULT_STATISTICS = {
        "games_played": 0,
        "x_wins": 0,
        "o_wins": 0,
        "ai_wins": 0,
        "draws": 0,
    }

    def __init__(self) -> None: 
        # Initializes the statistics manager 

        self.statistics = {}

        self.load_statistics()

    def load_statistics(self) -> None: 
        # Loads statistics from the JSON file 

        data = FileManager.load_json(
            "data/statistics.json"
        )

        if isinstance(data, dict):

            self.statistics = data

        else:

            self.reset_statistics()

    def save_statistics(self) -> None: 
        # Saves the current statistics to the JSON file 

        FileManager.save_json(
            "data/statistics.json",
            self.statistics,
        )

    def record_win(
        self,
        winner: str,
        ai_game: bool = False,
    ) -> None: 
        # Records a completed game with a winner 

        self.statistics["games_played"] += 1

        if winner == "X":

            self.statistics["x_wins"] += 1

        elif winner == "O":

            if ai_game:

                self.statistics["ai_wins"] += 1

            else:

                self.statistics["o_wins"] += 1

        self.save_statistics()

    def record_draw(self) -> None: 
        # Records a drawn game 

        self.statistics["games_played"] += 1
        self.statistics["draws"] += 1

        self.save_statistics()

    def get_statistic(
        self,
        key: str,
    ): 
        # Returns a single statistic 

        return self.statistics.get(key)

    def get_all_statistics(self) -> dict: 
        # Returns a copy of all statistics 

        return self.statistics.copy()

    def reset_statistics(self) -> None: 
        # Resets every statistic back to zero 

        self.statistics = (
            self.DEFAULT_STATISTICS.copy()
        )

        self.save_statistics()


__all__ = [
    "StatisticsManager",
] 

