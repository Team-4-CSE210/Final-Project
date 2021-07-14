import arcade
from math_properties import constants
from math_properties.director import Director


class InstructionView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.ORANGE_PEEL)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(
            "Instructions Screen",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2,
            arcade.color.BLACK,
            font_size=50,
            anchor_x="center",
        )
        arcade.draw_text(
            "Commutative Property of Addition: A + B = B + A",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - 75,
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Collect fruit matching the pattern:  A + B = B + A",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - (2 * 75),
            arcade.color.PURPLE,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Type 'q' to quit.",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - (3 * 75),
            arcade.color.RED,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Click to advance",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - (4 * 75),
            arcade.color.GRAY,
            font_size=20,
            anchor_x="center",
        )

    def on_mouse_press(self, x: float, y: float, dx: float, dy: float):
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)
