import arcade
from game import constants

class FallingItem(arcade.Sprite):

    FALLING_ITEM_SPEED = 0

    def __init__(self):
        super().__init__(
            # Sprite filename and scale
            constants.SHIP_SPRITE_PATH, .1
        )
        #
        self.width = 156
        self.height = 166
        # Set location of sprite in the window
        self.center_x = 500
        self.center_y = 100#constants.SCREEN_HEIGHT

        self.change_y = self.FALLING_ITEM_SPEED

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
        elif self.top > constants.SCREEN_HEIGHT - 1:
            self.top = constants.SCREEN_HEIGHT - 1