import arcade
from math_properties import constants

fruits_info = {}
fruits_info["apple"] = ["images/apple.png", 0.1, "The apple is nice"]
fruits_info["banana"] = ["images/banana.png", 0.2, "The banana is awesome"]
fruits_info["orange"] = ["images/grapes.png", 0.02, "The grapes are delicious"]
fruits_info["strawberry"] = ["images/strawberry.png", 0.02, "The grapes are delicious"]
fruits_info["sandia"] = ["images/sandia.png", 0.02, "The strawberry looks shiny"]
fruits_info["pineapple"] = ["images/pineapple.png", 0.02, "The pineapple is big"]
fruits_info["kiwi"] = ["images/kiwi.png", 0.02, "The kiwi looks yummy"]

class FallingItem(arcade.Sprite):

    FALLING_ITEM_SPEED = 0

    def __init__(self, type):
        filename = fruits_info[type][0]
        scale = fruits_info[type][1]

        super().__init__(filename = filename, scale = scale)
        #
        self.width = 156
        self.height = 166
        # Set location of sprite in the window
        self.center_x = 500
        self.center_y = 100#constants.SCREEN_HEIGHT

        self.change_y = self.FALLING_ITEM_SPEED
        self.description = fruits_info[type][2]
        self.type = type

    def get_description(self):
        return self.description
  
    def get_type(self):
        return self.type

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