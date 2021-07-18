import arcade
from math_properties import constants

# (AH) to avoid Circular Import Error.
import math_properties.instruction_view


class WinGameView(arcade.View):
    def __init__(self, score, current_time):
        super().__init__()
        self.time_taken = current_time / 60
        self.score = score

        # (AH) load win game over sound.
        self.background_music = arcade.load_sound(constants.BACKGROUND_MUSIC)
        # (AH) play concert hall applause win game over sound.
        arcade.play_sound(self.background_music)

    def on_show(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text(
            "YOU WON!",
            constants.SCREEN_WIDTH / 2,
            400,
            arcade.color.SCHOOL_BUS_YELLOW,
            54,
            anchor_x="center",
        )
        arcade.draw_text(
            "Click to restart",
            constants.SCREEN_WIDTH / 2,
            300,
            arcade.color.BLACK,
            24,
            anchor_x="center",
        )

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(
            f"Time taken: {time_taken_formatted}",
            constants.SCREEN_WIDTH / 2,
            200,
            arcade.color.BLACK,
            font_size=15,
            anchor_x="center",
        )

        output_total = f"Total Score: {self.score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.BLACK, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        instruction_view = math_properties.instruction_view.InstructionView()
        self.window.show_view(instruction_view)

