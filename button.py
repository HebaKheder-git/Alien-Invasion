import pygame.font

class Button:
    """a class that defines buttons inside Alien Invasion"""

    def __init__(self , ai_game , msg):
        """intializes the button attributes"""

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        #set the dimensions and properties of the button
        self.width , self.height = (200 , 50)
        self.button_color = (0 , 0 , 130)
        self.text_color = (255 , 255 , 255)
        self.font = pygame.font.SysFont(None , 48)

        #build the button's rect object and center it
        self.rect = pygame.Rect(0 , 0 , self.width , self.height)
        self.rect.center = self.screen_rect.center

        #the button message need to be prepped only once
        self._prep_msg(msg)

    def _prep_msg(self , msg):
        """Turn msg into a rendured image , and center text on the button"""

        self.msg_image = self.font.render (msg , True , self.text_color , self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.screen_rect.center

    def draw_button(self):
        """draws blank button then draw msg"""

        self.screen.fill(self.button_color , self.rect)
        self.screen.blit(self.msg_image , self.msg_image_rect)
