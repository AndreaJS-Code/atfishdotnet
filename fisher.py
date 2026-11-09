import pygame
from pygame.sprite import Sprite

class Fisher(Sprite):
    """Class to represent the fisher (the player)"""

    def __init__(self, game):
        """Construct fisher character in starting position"""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()

        # Load the fisher image and get its rect
        self.image = pygame.image.load("images/fisher.png").convert_alpha()
        self.rect = self.image.get_rect()

        # Start each fishing boat at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # Store a decimal value for the ship's horizontal position
        self.x = float(self.rect.x)

        # Movement flags
        self.moving_right = False
        self.moving_left = False

    def update_position(self):
        """Update position of the fishing boat based on movement flag"""

        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.boat_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.boat_speed

        # Update rect object from self.x
        self.rect.x = self.x

    def display_fisher(self):
        """Draw fishing boat on the screen at its current position"""

        self.screen.blit(self.image, self.rect)