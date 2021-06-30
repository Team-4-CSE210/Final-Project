# (AH) Arcade for final project game.
import random
import arcade

from time import sleep
from math_properties import constants


class Director(arcade.Window):
    """
    A code template for a person who directs the game.
    The responsibility of this class of objects is to
    control the sequence of play.

    Stereotype:
        Controller

    Attributes:
        _cast (dictionary): The game actors {key: name, value: object}
        _script (dictionary): The game actions {key: tag, value: object}
        _choice_list (list): The characters chosen by Player to form equation.
    """

    def __init__(self, cast, script):
        """ The class constructor.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
            script (dict): The game actions {key: tag, value: list}.
        """
        # (AH) Call the parent class initializer.
        # (AH) title is "Math Properties".
        # ??? AGNES ???
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Math Properties")

        # (AH) Variables that will hold sprite lists.
        self.falling_items_list = None
        self.player_list = None

        # (AH) Set up the player info.
        self.player_sprite = None
        self.score = 0

        # (AH) Don't show the mouse cursor -- NO NEED!
        # self.set_mouse_visible(False)

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed.  """

        # (BL) If the player presses a key, update the speed.
        if key == arcade.key.UP:
            self.player_sprite.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key.  """

        # (BL) If the player releases a key, zero out the speed.
        #       This doesn't work well if multiple keys are pressed.
        #       Use 'better move by keyboard' eg if you need to handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


        # arcade.open_window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, "Math Properties")

        # (AH) Set the background color.
        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # (AH) Sprites lists.
        self.falling_item_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()

        # (AH) Score
        self.score = 0

        # (AH) Set up the player.
        # (AH) Character image from kenney.nl
        self.player_sprite = arcade.Sprite("character.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = constants.PLAYER_CENTER_
        self.player_sprite.center_y = constants.PLAYER_CENTER
        self.player_list.append(self.player_sprite)

        # (AH) Create the colored shapes instance.
        # (AH) Images on kenney.nl
        # ??? AGNES CREATE LIST OF COLORED SHAPES ???
        #falling_item = arcade.Sprite("coin_01.png", SPRITE_SCALING_COIN)


        # (AH) Position the falling items.
        coin.center_x = random.randrange(constants.SCREEN_WIDTH)
        coin.center_y = random.randrange(constants.SCREEN_HEIGHT)

        # (AH) Add the coin to the list.
        self.coin_list.append(coin)

        # self._cast = cast
        # self._script = script
        # self._choice_list = []

    # # moved to OutputService().
    # def on_draw(self):
    #     """
    #     Draw the sprite lists here.
    #     Typically sprite are divided into different groups.
    #     Other game engines might call these 'sprite layers' or 'sprite'groups'.
    #     Sprites that don't move should be drawn in their own group
    #     for the best performance, as Arcade can tell the graphics card
    #     to just redraw them at the same spot.
    #     Try to avoid drawing sprites on their own, use a SpriteList
    #     because there are many performance improvements in that code.
    #     """
    #     # (AH) Start drawing.
    #     arcade.start_render()
    #     self.player_list.draw()
    #     self.falling_item_list.draw()
    #     # (AH) Finish drawing.
    #     arcade.finish_render()

    # def on_mouse_motion

    def update(self, delta_time):
        """ Movement and game logic. """

def main():
    """ Main method """
    window = MathProperties()
    window.setup()
    # (AH) Keep window up until someone closes it.
    arcade.run()

if __name__ == "__main__":
    main()


#     def start_game(self):
#         """Starts the game loop to control the sequence of play."""
#         while True:
#             self._cue_action("input")
#             self._cue_action("update")
#             self._cue_action("output")
#             sleep(constants.FRAME_LENGTH)

#     def _cue_action(self, tag):
#         """Executes the actions with the given tag.

#         Args:
#             tag (string): The given tag.
#         """
#         for action in self._script[tag]:
#             action.execute(self._cast, self._choice_list)
#
