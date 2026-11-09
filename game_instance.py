import sys
import pygame

from random import randint
from settings import Settings
from points import Points
from fisher import Fisher
from net import Net
from fish import Fish

class GameInstance:
    """Class to manage game execution"""

    def __init__(self):
        """Initialize game and set up the screen"""

        pygame.init()
        self.settings = Settings()
        self.clock = pygame.time.Clock()

        # Create game window
        self.screen = pygame.display.set_mode((self.settings.screen_width,
                self.settings.screen_height))

        # Game window title
        pygame.display.set_caption("@fish.net")

        # Initialize point tracking
        self.points = Points(self)

        # Create assets
        self.fisher = Fisher(self)
        self.fishes = pygame.sprite.Group()
        self.net = Net(self)
        self._spawn_fish()

    def _check_events(self):
        """Check for keyboard and mouse events"""

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_mouse_events(mouse_pos)

    def _check_keydown_events(self, event):
        """Check for keypresses"""

        # Player moving fisher to the right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.fisher.moving_right = True
        # Player moving fisher to the left
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.fisher.moving_left = True
        # Player throws net
        elif event.key == pygame.K_SPACE:
            if not self.net.net_thrown:
                self.net.net_thrown = True

    def _check_keyup_events(self, event):
        """Check for keys being released"""

        # Player stops moving fisher to the right
        if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
            self.fisher.moving_right = False
        # Player stops moving fisher to the left
        elif event.key == pygame.K_LEFT or event.key == pygame.K_a:
            self.fisher.moving_left = False

    def _check_mouse_events(self, mouse_pos):
        """Check for mouse events"""

    def _spawn_fish(self):
        """Create fish"""

        while len(self.fishes.sprites()) < self.settings.fish_limit:
            new_fish = Fish(self)
            self.fishes.add(new_fish)

    def _update_fish_spawns(self):
        """Remove fish that have despawned"""

        # See if anything was caught
        self._check_catches()

        for fish in self.fishes.copy():
            if (fish.screen_lengths >= fish.max_screen_lengths
                    or (fish.caught and fish.rect.bottom <= 0)):
                self.fishes.remove(fish)

        # Replace removed fish
        self._spawn_fish()

    def _check_catches(self):
        """Check for fish that have been caught"""

        collisions = pygame.sprite.spritecollide(self.net, self.fishes,
                False)
        if collisions:
            for fish in collisions:
                if not fish.caught:
                    self.points.available_points += fish.points_value
                    fish.caught = True

    def _update_screen(self):
        """Update screen with locations of images and display them"""

        # Redraw the screen
        self.screen.fill((self.settings.bg_color))
        self.fisher.display_fisher()
        for fish in self.fishes.sprites():
            fish.display_fish()
        self.net.display_net()

        # Display points
        self.points.display_points()

        # Make the most recently drawn screen visible
        pygame.display.flip()

    def start_game(self):
        """Start the game loop"""

        while True:
            self.clock.tick(self.settings.fps)
            self._check_events()

            # Update fishing boat position
            self.fisher.update_position()

            # Update fish position
            for fish in self.fishes.sprites():
                fish.update_position()
            self._update_fish_spawns()

            # Update net position
            self.net.update_position()

            # Draw changes to screen
            self._update_screen()

if __name__ == "__main__":
    game_instance = GameInstance()
    game_instance.start_game()