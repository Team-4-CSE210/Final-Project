import arcade
import random
from math_properties import constants


fruits_info = {}
fruits_info["apple"] = [constants.APPLE, 0.15]
fruits_info["banana"] = [constants.BANANA, 0.15]
fruits_info["strawberry"] = [constants.STRAWBERRY, 0.15]
fruits_info["watermelon"] = [constants.WATERMELON, 0.15]
fruits_info["pineapple"] = [constants.PINEAPPLE, 0.2]
fruits_info["kiwi"] = [constants.KIWI, 0.15]
fruits_info["grapes"] = [constants.GRAPES, 0.05]

fruits_name_list = list(fruits_info.keys())


class FallingItem(arcade.Sprite):

    # FALLING_ITEM_SPEED = -1

    def __init__(self, type):
        filename = fruits_info[type][0]
        scale = fruits_info[type][1]

        super().__init__(filename=filename, scale=scale)
        #
        # self.width = 156
        # self.height = 166
        # Set location of sprite in the window
        # (AH) fruit on left margin of screen could not be caught.
        self.center_x = random.randrange(100, constants.SCREEN_WIDTH - 100)
        self.center_y = constants.SCREEN_HEIGHT

        self.change_y = -2  # self.FALLING_ITEM_SPEED
        self.type = type

    def get_type(self):
        return self.type

    def update(self):
        # Move player.
        # Remove these lines if physics engine is moving player.
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Check for out-of-bounds
        if self.left < 0:
            self.left = 0
        elif self.right > constants.SCREEN_WIDTH - 1:
            self.right = constants.SCREEN_WIDTH - 1

