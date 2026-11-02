class Gamestats:
    """a class that tracks statistics for Alien Invasion"""

    def __init__(self , ai_game):
        """intializes the game state"""

        self.settings = ai_game.settings
        self.reset_stats()
        self.game_active = False
        self.highest_score = 0

    def reset_stats(self):
        """reset the game state"""

        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
