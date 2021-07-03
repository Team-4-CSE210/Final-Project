import arcade
from math_properties import constants
from math_properties.falling_item import FallingItem
from math_properties.scoreboard import Scoreboard

class Director(arcade.Window):

    SCREEN_TITLE = "Math game"

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.SCREEN_TITLE) 

        self.player_list = arcade.SpriteList()
        self.falling_item_list = arcade.SpriteList()

        self.player = None
        self.fallingItem = None
        self.background = None

    def setup(self):
        self.fallingItem = FallingItem()
        self.falling_item_list.append(self.fallingItem)

        #Load background texture
        #self.background = arcade.load_texture("Path")

    def on_draw(self):
        """
        Render the screen and draw sprites
        """
        arcade.start_render()

        self.falling_item_list.draw()

    def on_update(self, delta_time: float):
        self.falling_item_list.update()

        #Collision
        #arcade.check_for_collision_with_list(self.player, self.falling_item_list)

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.fallingItem.center_x = x
        #self.fallingItem.center_y = y

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.fallingItem.change_x = -5
        elif symbol == arcade.key.RIGHT:
            self.fallingItem.change_x = 5

    def on_key_release(self, symbol: int, modifiers: int):
        self.fallingItem.change_x = 0