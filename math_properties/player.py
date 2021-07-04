import arcade
from math_properties import constants


class Player(arcade.Sprite):

    FALLING_ITEM_SPEED = 0

    def __init__(self):
        super().__init__(
            # Sprite filename and scale
            constants.PADDLE_SPRITE_PATH, .1)
        #
        self.width = 160
        self.height = 160
        # Set location of sprite in the window
        self.center_x = constants.SCREEN_WIDTH/2
        self.center_y = 100  # constants.SCREEN_HEIGHT

        self.change_y = self.FALLING_ITEM_SPEED

    def set_velocity_x(self, v):
        self.change_x = v
        
    def update(self):
        """ Move the player """
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > constants.SCREEN_WIDTH - 1:
            self.right = constants.SCREEN_WIDTH - 1

        if self.bottom < 0:
            self.bottom = 0
        elif self.top > constants.SCREEN_HEIGHT - 2:
            self.top = constants.SCREEN_HEIGHT - 2