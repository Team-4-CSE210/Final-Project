import arcade
from math_properties import constants
from math_properties.instruction_view import InstructionView


class MenuView(arcade.View):

    def on_show(self):
        arcade.set_background_color(arcade.color.DARK_GREEN)

    def on_draw(self):
        arcade.start_render()
        # title of current game.
        arcade.draw_text(
            "Fruit Math: Learn a Math Property",
            constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2,
            arcade.color.WHITE, font_size=50, anchor_x="center"
        )
        arcade.draw_text(
            "Click to advance",
            constants.SCREEN_WIDTH/2, constants.SCREEN_HEIGHT/2-75,
            arcade.color.GRAY, font_size=20, anchor_x="center"
        )

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        instructions_view = InstructionView()
        self.window.show_view(instructions_view)
