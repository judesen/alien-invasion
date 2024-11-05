class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        self.screen_width = 600
        self.screen_height = 400
        self.bg_color = (230, 230, 230)
        
        # Ship settings.
        self.ship_speed = 10
        
        # Bullet settings.
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed =  100
        self.bullet_destructible = True
        # Alien settings.
        self.alien_speed = 1.0
        self.alien_drop_speed = 10
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
