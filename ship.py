import pygame

class Ship:
    """a class to manage the ship of alien invasion"""

    def __init__(self , ai_game):
        """initiates the ship and sets its starting position"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        original_image = pygame.image.load('images/ship.bmp')
        current_size = original_image.get_size()
        new_size = (int(current_size[0] // 15), int(current_size[1] // 15))
        self.image = pygame.transform.scale(original_image, new_size)
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.moving_right = False
        self.moving_left = False
        self.settings = ai_game.settings
        self.x = float(self.rect.x)

    def blitme(self):
        """draws the ship shape on the screen"""

        self.screen.blit(self.image , self.rect)

    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x

    def center_ship(self):
        """returns the ship the cemter of the screen"""

        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)