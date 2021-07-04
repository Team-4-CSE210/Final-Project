import arcade
import random
from math_properties import constants
from math_properties.falling_item import FallingItem
from math_properties.player import Player


class Director(arcade.View):

    # (AH) LATER change screen title depending on math property.

    # --- Other Data: block begins ---
    # (AH) initialize score to check for above 85% mastery of math property.
    score = 0
    # (AH) game ends when Player achieves above 85% mastery.
    num_tries = 0
    # (AH) Attributes for use in Collision block during Update.
    # (AH) initialize equation list to compare with math property.
    equation_list = []
    # (AH) LATER when doing all properties, equation_length is a var int.
    equation_length = 4
    # --- Other Data: block ends ---

    def __init__(self):
        # call the parent class initializer.
        super().__init__(
        )

        self.current_time = 0
        self.falling_item_list = arcade.SpriteList()
        self.player = None
        self.fallingItem = None
        self.background = None

    def setup(self):
        self.player = Player()
        # Load background texture
        self.background = arcade.load_texture(constants.BACKGROUND)

    def on_draw(self):
        """
        Render the screen and draw sprites
        """
        arcade.start_render()
        arcade.draw_texture_rectangle(
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2,
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            self.background,
        )
        self.player.draw()
        self.falling_item_list.draw()

    def on_update(self, delta_time: float):
        self.current_time += 1
        self.falling_item_list.update()
        if self.current_time % 120 == 0:
            fruit = FallingItem(
                random.choice(
                    ["apple", "banana", "strawberry", "watermelon", "pineapple", "kiwi"]
                )
            )
            self.falling_item_list.append(fruit)

        for fr in self.falling_item_list:
            fr.update()
            if fr.center_y < 0:
                fr.kill()
        self.player.update()

        # Collision
        hit_list = arcade.check_for_collision_with_list(
            self.player, self.falling_item_list
        )

        # (AH) Begin block to verify Math Property.
        # (AH) include collected fruit into equation list.
        self.equation_list.extend(hit_list)

        # (AH) check if enough fruit has been collected for the equation.
        # (AH) NOW only checking for Commutative Property of Addition.
        # (AH) LATER use Math Class to check for all math properties.
        if len(self.equation_list) == self.equation_length:
            if (
                self.equation_list[2] == self.equation_list[1]
                and self.equation_list[3] == self.equation_list[0]
            ):
                self.score += 1
            # (AH) DEBUGGING CODE
            # print(f"Checking equation: {self.score}")
            return

        # (AH) remove to release object from memory.
        for fruit in hit_list:
            # (AH) DEBUGGING CODE
            # print(f"Got {fruit.type}")
            fruit.remove_from_sprite_lists()

        # (AH) Conditional stmts to check for mastery.
        if len(self.equation_list) >= self.equation_length:
            self.num_tries += 1
            if self.score / self.num_tries > 0.85:
                # (AH) TODO Add Sound.
                # TODO print(Congratulation!)
                arcade.close_window()

        return
        # (AH) End block to verify Math Property.

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        pass

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.center_x = x
        # self.player.center_y = y

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player.change_x = -2
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = 2

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

    def on_key_release(self, symbol: int, modifiers: int):
        self.player.change_x = 0

