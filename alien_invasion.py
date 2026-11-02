import sys
from time import sleep
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from game_stats import Gamestats
from button import Button
from scoreboard import ScoreBoard
import pygame

class AlienInvasion:
    """overall class to manage game assets and behavior"""

    def __init__(self):
        """initiates the game, and creates game resources"""

        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width , self.settings.screen_height))
        #self.screen = pygame.display.set_mode((0 , 0) , pygame.FULLSCREEN)
        #self.settings.screen_width = self.screen.get_rect().width
        #self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Alien Invasion")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        #creates an instance to store game statistics
        # , and create a score board
        self.gamestate = Gamestats(self)
        self.sb = ScoreBoard(self)

        self._create_fleet()
        self.play_button = Button(self , "Play")
        

    def run_game(self):
        """starts the main loop for the game"""

        while True:
            self._check_events()
            if self.gamestate.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            self._update_screen()

    def _check_events(self):
        """watch for keyboard and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP :
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_keydown_events(self , event):
        """Respond to keypresses."""

        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_SPACE:
            self._fire_bullets()
        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self , event):
        """Respond to key releases."""
        
        if event.key == pygame.K_RIGHT :
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _update_screen(self):
        """updates the screen and its elements"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        self.aliens.draw(self.screen)
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.sb.draw_score()
        if not self.gamestate.game_active:
            self.play_button.draw_button()
        pygame.display.flip()

    def _fire_bullets(self):
        """creates a new bullet and adds it to bullets group"""

        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        """removes the bullets when they go outside the the game's screen boundaries"""

        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0 :
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()
        
        
        

    def _create_fleet(self):
        """creates a fleet of aliens"""

        #clculating how many aliens fit in one row
        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_x = int(self.settings.screen_width - 1.5 * alien_width)
        available_space_y = self.settings.screen_height - (5 * alien_height) - ship_height
        alien_numbers_x = (available_space_x) // (alien_width * 2)
        row_numbers = (available_space_y) // (alien_height * 2)

        #creates the full fleet of aliens
        for row_number in range(row_numbers):
            for alien_number in range(alien_numbers_x) :
                self._create_alien(row_number , alien_number)

    def _create_alien(self , row_number ,  alien_number):
        """creates an alien and position it horizontally"""

        alien = Alien(self)
        alien_width , alien_height = alien.rect.size
        alien.x = alien_width +  2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)
        

    def _update_aliens(self):
        """checks if the fleet reached the edge AND moves the aliens"""

        self.aliens.update()
        self._check_fleet_edges()
        #checks if alien reached the ship
        if pygame.sprite.spritecollideany(self.ship , self.aliens):
            self._ship_hit()

        self._check_aliens_bottom()


    def _check_fleet_edges(self):
        """checks if the fleet reached the edge and changes the fleet direction if so"""

        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """drop the entire fleet AND change the fleet direction from left to right OR right to left"""

        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= (-1)


    def _check_bullet_alien_collision(self):
        """respond to bullet_alien collision"""
        
        collisions = pygame.sprite.groupcollide(self.bullets , self.aliens , True , True)
        #updates the score value
        if collisions:
            for aliens in collisions.values():
                self.gamestate.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        #creating a new fleet each time the alien group is empty
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            #increase speed
            self.settings.increase_speed()
            #level up
            self.gamestate.level +=1
            self.sb.prep_level()

    def _ship_hit(self):
        """responds to a ship hit by any alien"""

        if self.gamestate.ships_left > 0:
            #decrease the number of left ships by 1
            self.gamestate.ships_left -= 1
            self.sb.prep_ship()

            #remove all aliens and bullets
            self.bullets.empty()
            self.aliens.empty()

            #starts the game again
            self._create_fleet()
            self.ship.center_ship()

            #pauses the game for 1
            sleep(1)

        else:
            self.gamestate.game_active = False
            pygame.mouse.set_visible(True)


    def _check_aliens_bottom(self):
        """checks if any alien reaches the bottom"""

        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _check_play_button(self,mouse_pos):
        """checks if the mouse is clicked over the play button and starts the game if so"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.gamestate.game_active:
            #reset the game statistics
            self.gamestate.reset_stats()
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ship()
            self.settings.initialize_dynamic_settings()
            self.gamestate.game_active = True
            pygame.mouse.set_visible(False)
            #get rid of any remaining aliens and bullets
            self.aliens.empty()
            self.bullets.empty()

            #creates a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
if __name__ == '__main__':
    """makes a game instance, and runs the game"""

    ai = AlienInvasion()
    ai.run_game()