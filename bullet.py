from pygame.sprite import Sprite
import pygame

class Bullet(Sprite):
    """a class that represents a bullet"""

    def __init__(self , ai_game):
        """creats a bullet object at the ship's position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        self.rect = pygame.Rect(0,0,self.settings.bullet_width , self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        self.y = float(self.rect.y)

    def update (self):
        """moves the bullet up straight """

        #if self.rect.top > 0:
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """draws the bullet on the screen"""

        pygame.draw.rect(self.screen , self.color , self.rect)