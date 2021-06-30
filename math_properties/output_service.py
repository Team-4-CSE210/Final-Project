import sys
import arcade
from math_properties import constants
# from asciimatics.widgets import Frame

class OutputService:
    """Outputs the game state.
    The responsibility of the class of objects is to
    draw the game state on the terminal.

    Stereotype:
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, screen):
        """The class constructor.

        Args:
            screen (Screen): An Asciimatics Screen.
        """
        self._screen = screen

    def clear_screen(self):
        """Clears the Asciimatics buffer for the next rendering."""
        # self._screen.clear_buffer(7, 0, 0)
        # self._screen.print_at("-" * constants.MAX_X, 0, 0, 7)
        # self._screen.print_at("-" * constants.MAX_X, 0, constants.MAX_Y, 7)

    def draw_actor(self, actor):
        """
        Draw the sprite lists here.
        Typically sprite are divided into different groups.
        Other game engines might call these 'sprite layers' or 'sprite'groups'.
        Sprites that don't move should be drawn in their own group
        for the best performance, as Arcade can tell the graphics card
        to just redraw them at the same spot.
        Try to avoid drawing sprites on their own, use a SpriteList
        because there are many performance improvements in that code.

        Args:
            actor (Actor): The actor to render.
        """
        # text = actor.get_text()
        position = actor.get_position()
        x = position.get_x()
        y = position.get_y()
        # self._screen.print_at(text, x, y, 7) # WHITE

        # def on_draw(self):

        # (AH) Arcade start drawing.
        arcade.start_render()
        self.player_list.draw()
        self.falling_item_list.draw()
        # (AH) Arcade finish drawing.
        arcade.finish_render()


    def draw_actors(self, actors):
        """Renders the given list of actors on the screen.

        Args:
            actors (list): The actors to render.
        """
        for actor in actors:
            self.draw_actor(actor)

    def flush_buffer(self):
        """Renders the screen."""
        # self._screen.refresh()