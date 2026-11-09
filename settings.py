class Settings():
    """Class containing all settings used in the game"""

    def __init__(self):
        """Initialize the game settings"""

        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 255)
        self.fps = 120

        # Fishing boat settings
        self.boat_speed = 5

        # Net throwing speed
        self.number_of_nets = 1
        self.throwing_speed = 3

        # Fish settings
        # Fish only spawn in the top half of the screen
        self.fish_spawn_y_limit = self.screen_height / 2
        self.fish_limit = 10