import pygame
from pygame.sprite import Sprite

from random import choice, choices, randint

class FishType():
    """Establish fish superclass for fish subclass objects to inherit from."""

    FISH_TYPES = {
            1: {
                    'image': pygame.image.load("images/pink_clownfish.png"),
                    'points': 1,
                    'base_speed': 1,
                    'spawn_weight': 75,
                    # max_screen_lengths is the number of times the fish will
                    # cross the screen before despawning
                    'max_screen_lengths': 20
            },
            2: {
                    'image': pygame.image.load("images/orange_clownfish.png"),
                    'points': 2,
                    'base_speed': 1.5,
                    'spawn_weight': 50,
                    'max_screen_lengths': 15
            },
            3: {
                    'image': pygame.image.load("images/yellow_clownfish.png"),
                    'points': 3,
                    'base_speed': 2,
                    'spawn_weight': 20,
                    'max_screen_lengths': 12
            },
            4: {
                    'image': pygame.image.load("images/green_clownfish.png"),
                    'points': 5,
                    'base_speed': 3,
                    'spawn_weight': 10,
                    'max_screen_lengths': 10
            },
            5: {
                    'image': pygame.image.load("images/blue_clownfish.png"),
                    'points': 7,
                    'base_speed': 4,
                    'spawn_weight': 5,
                    'max_screen_lengths': 8
            },
            6: {
                    'image': pygame.image.load("images/purple_clownfish.png"),
                    'points': 10,
                    'base_speed': 5,
                    'spawn_weight': 2,
                    'max_screen_lengths': 6
            },
            7: {
                    'image': pygame.image.load("images/clown_fish.png"),
                    'points': 50,
                    'base_speed': 2,
                    'spawn_weight': 1,
                    'max_screen_lengths': 1
            }
    }

class Fish(Sprite, FishType):
    """Fish class for actual fish caught by player"""

    def __init__(self, game):
        """Create a new fish object with specific attributes pulled based on
        fish type"""

        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Assign fish identity based on rarity
        self.fish_id = choices(
                list(self.FISH_TYPES.keys()),
                weights = [fish['spawn_weight'] for fish in
                        self.FISH_TYPES.values()],
                k = 1
        )[0]

        # Assign fish attributes
        self.image = self.FISH_TYPES[self.fish_id]['image']
        self.points_value = self.FISH_TYPES[self.fish_id]['points']
        self.fish_speed = self.FISH_TYPES[self.fish_id]['base_speed']
        self.max_screen_lengths = self.FISH_TYPES[self.fish_id][
            'max_screen_lengths']
        self.screen_lengths = 0
        self.caught = False


        # Assign a random direction to the fish
        # -1 means the fish is moving right to left
        # 1 means the fish is moving left to right
        self.swim_direction = choice([-1,1])

        if self.swim_direction == -1:
            # Start the fish just beyond the right edge of the screen
            # Spawn a random y value between screen top and lower limit
            self.rect = self.image.get_rect()
            self.rect.x = randint(self.settings.screen_width + 5,
                    self.settings.screen_width + 250)

        else:
            # Start the fish just beyond the left edge of the screen
            # Spawn a random y value between screen top and lower limit
            self.rect = self.image.get_rect()
            self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x = randint(-250,-5)

        self.rect.y = randint(5, int(self.settings.fish_spawn_y_limit))

        # Store the fish's horizontal and vertical position
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update_position(self):
        """Move the fish"""

        # If fish has been caught, drag the fish along with the net
        if self.caught:
            self.y -= self.settings.throwing_speed
            self.rect.y = self.y

        # Flip the image and reverse swim direction if fish has reached the
        # edge of the screen
        else:
            if ((self.swim_direction == -1 and self.rect.right < 0) or
                    (self.swim_direction == 1 and self.rect.left > self.settings.screen_width)):
                self.image = pygame.transform.flip(self.image, True, False)
                self.swim_direction *= -1
                self.screen_lengths += 1

            self.x += (self.fish_speed * self.swim_direction)
            self.rect.x = self.x

    def display_fish(self):
        """Draw fish to the screen"""

        self.screen.blit(self.image, self.rect)
