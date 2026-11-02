class Settings:
    """A class to store all settings for Alien Invasion"""

    def __init__(self):
        """Intializes the main settings of the game"""

        self.screen_width = 1550
        self.screen_height = 780
        self.bg_color = (230,230,230)
        #ship_settings
        self.ship_limit = 3
        #bullet_settings
        self.bullet_color = (60,0,0)
        self.bullet_height = 15
        self.bullet_width = 3
        self.bullets_allowed = 10
        #alien_settings
        self.fleet_drop_speed = 7

        #How quickly the game speed up
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """initializes settings the=at chamge through the game"""

        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 0.5

        #fleet_direction = 1 >>> right , self_direction = -1 >>> left
        self.fleet_direction = 1

        #Scoring
        self.alien_points = 50

    def increase_speed(self):
        """increases the game speed and alien point value"""

        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)


        
