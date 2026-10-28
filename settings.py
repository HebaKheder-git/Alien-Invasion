class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Intializes the main settings of the game"""

        self.screen_width = 1550
        self.screen_height = 780
        self.bg_color = (230,230,230)
        #ship_settings
        self.ship_speed = 1.5
        #bullet_settings
        self.bullet_color = (60,0,0)
        self.bullet_speed = 1.0
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullets_allowed = 3
