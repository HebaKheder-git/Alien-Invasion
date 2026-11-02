import pygame.font
from ship import Ship
from pygame.sprite import Group

class ScoreBoard:
    """a class that defines the scoreboard"""

    def __init__(self , ai_game):
        """initializes the scoreboard attribute"""

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        self.state = ai_game.gamestate   

        #setting text color and font
        self.text_color = (30 , 30 , 30)
        self.font = pygame.font.SysFont(None , 48)

        #prepering the score
        self.prep_score()
        #preparing the highest score
        self.prep_high_score()
        #preparing the level to be shown
        self.prep_level()
        #prepares left ships to be shown
        self.prep_ship()


    def prep_score(self):
        """prepars the scores to be shown"""

        #prepares the current score
        rounded_score = round(self.state.score , -1)
        score_part_str = "{:,}".format(rounded_score)
        score_str = "Score: " + score_part_str
        self.score_img = self.font.render(score_str , True , self.text_color , self.settings.bg_color)
        self.score_rect = self.score_img.get_rect()

        #position the score on the screen
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 5

    def prep_high_score(self):
        """prepares the highest score to be shown"""

        rounded_score = round(self.state.highest_score)
        high_score_part_str = "{:,}".format(rounded_score , -1)
        high_score_str = "Highest Score: " + high_score_part_str
        self.high_score_img = self.font.render(high_score_str , True , self.text_color , self.settings.bg_color)
        self.high_score_rect = self.high_score_img.get_rect()
        #position the high score on the screen
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top 

    def prep_level(self):
        """prepares the level to be printed"""

        level_str = "Level: " + str(self.state.level)
        self.level_img = self.font.render(level_str , True , self.text_color , self.settings.bg_color )
        #position the level on the screen
        self.level_rect = self.level_img.get_rect()
        self.level_rect.right = self.score_rect.left - 200
        self.level_rect.top = self.score_rect.top

    
    def draw_score(self):
        """draws the score and level on the screen"""

        self.screen.blit(self.score_img , self.score_rect)
        self.screen.blit(self.high_score_img , self.high_score_rect)
        self.screen.blit(self.level_img , self.level_rect)
        self.ships.draw(self.screen)

    def check_high_score(self):
        """updates the high score"""

        if self.state.score > self.state.highest_score:
            self.state.highest_score = self.state.score
            self.prep_high_score()

    def prep_ship(self):
        """prepars left ships to be drawn on the screen"""

        self.ships = Group()
        for ship_number in range(self.state.ships_left):
            ship = Ship(self.ai_game)
            ship.rect.x = 10 + ship.rect.width * ship_number
            ship.rect.y = self.score_rect.top
            self.ships.add(ship)