import pygame
from pygame.sprite import Sprite

class Net(Sprite):
    """A class to manage the net thrown by the fisher"""

    def __init__(self, game):
        """Create a net object in the fisher's hand"""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.fisher = game.fisher
        self.screen_rect = game.screen.get_rect()

        # Load the net image and get its rect
        self.image = pygame.image.load("images/net.png").convert_alpha()
        self.image_rect = self.image.get_rect()

        # Define the net's hitbox
        self.rect = pygame.Rect(0, 0, self.image_rect.width * 0.4,
                self.image_rect.height * 0.4)

        # Start each net in the fisher's hand
        self.image_rect.x = game.fisher.rect.centerx + 25
        self.image_rect.y = game.fisher.rect.centery - 100

        # Store the net's position as a decimal value
        self.x = float(self.image_rect.x)
        self.y = float(self.image_rect.y)

        # Movement flag
        self.net_thrown = False

    def update_position(self):
        """Update the position of the net"""

        # The fisher has the net in their hand
        if not self.net_thrown:
            if (self.fisher.moving_right and self.fisher.rect.right <
                    self.screen_rect.right):
                self.x += self.settings.boat_speed
            if self.fisher.moving_left and self.fisher.rect.left > 0:
                self.x -= self.settings.boat_speed
            # Update rect position
            self.image_rect.x = self.x

        # The net has been thrown
        else:
            # Net is still flying across the screen
            if self.image_rect.bottom > 0:
                self.y -= self.settings.throwing_speed
                # Update rect position
                self.image_rect.y = self.y

            # Reset net location
            else:
                self.image_rect.x = self.fisher.rect.centerx + 25
                self.image_rect.y = self.fisher.rect.centery - 100
                self.x = float(self.image_rect.x)
                self.y = float(self.image_rect.y)
                self.net_thrown = False

        # Make sure hitbox stays centered on net
        self.rect.center = (self.image_rect.centerx, self.image_rect.centery)

    def display_net(self):
        """Display the net on the screen"""

        self.screen.blit(self.image, self.image_rect)