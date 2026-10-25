import sys

import pygame

class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initiates the game, and creates game resources"""

        pygame.init()
        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """starts the main loop for the game"""

        while True:
            """watch for keyboard and mouse events"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    """makes a game instance, and runs the game"""

    ai = AlienInvasion()
    ai.run_game()