import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """a class that defines one single alien of a fleet"""

    def __init__(self , ai_game):
        """initializes the alien and sets its first position"""

        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        #load the alien image and set its rect attribute
        original_image = pygame.image.load("images/alien.bmp")
        current_size = original_image.get_size()
        new_size = ((current_size[0] // (1.5)) , (current_size[1] // (1.5)))
        self.image = pygame.transform.scale(original_image, new_size)
        self.rect = self.image.get_rect()

        #start each new alien near the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        #stores the alien exact horizontal position
        self.x = float(self.rect.x)

    def update(self):
        """moves the alien right"""

        self.x += (self.settings.fleet_direction * self.settings.alien_speed)
        self.rect.x = self.x

    def check_edges(self):
        """return True if alien at the edge of the screen"""

        screen_rect = self.screen.get_rect()
        if (self.rect.left <= 0) or (self.rect.right >= screen_rect.right):
            return True