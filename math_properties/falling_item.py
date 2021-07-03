import arcade
import random
from math_properties import constants


fruits_info = {}
fruits_info["apple"] = [constants.APPLE]
fruits_info["banana"] = [constants.BANANA]
fruits_info["strawberry"] = [constants.STRAWBERRY]
fruits_info["watermelon"] = [constants.WATERMELON]
fruits_info["pineapple"] = [constants.PINEAPPLE]
fruits_info["kiwi"] = [constants.KIWI]
fruits_name_list = list(fruits_info.keys())


class FallingItem(arcade.Sprite):

    # FALLING_ITEM_SPEED = -1

    def __init__(self, type):
        filename = fruits_info[type][0]

        super().__init__(filename=filename)
        #
        self.width = 156
        self.height = 166
        # Set location of sprite in the window
        self.center_x = 500
        self.center_y = constants.SCREEN_HEIGHT  # 100

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

        '''if self.bottom < 0:
            self.bottom = 0
        elif self.top > constants.SCREEN_HEIGHT - 1:
            self.top = constants.SCREEN_HEIGHT - 1'''
