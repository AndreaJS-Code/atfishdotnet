import pygame.font
from pygame.sprite import Group

class Points():
    """Class to display player points"""

    def __init__(self, game):
        """Initialize scorekeeping attributes"""
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.available_points = 0

        # Font settings for scoring information
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont('Arial', 48)

    def display_points(self):
        """Turn points into rendered image"""

        points_str = "{:,}".format(int(self.available_points))
        self.points_image = self.font.render(
                "Points: " + points_str, True,
                self.text_color, self.settings.bg_color)

        # Position points at the bottom right
        self.points_rect = self.points_image.get_rect()
        self.points_rect.right = self.screen_rect.right - 20
        self.points_rect.bottom = self.screen_rect.bottom - 20

        # Display points total
        self.screen.blit(self.points_image, self.points_rect)

