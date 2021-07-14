import arcade
import random
from math_properties import constants
from math_properties.falling_item import FallingItem
from math_properties.scoreboard import Scoreboard
from math_properties.player import Player


class Director(arcade.View):
    def __init__(self):
        super().__init__()

        self.current_time = 0
        self.falling_item_list = arcade.SpriteList()
        self.player = None
        self.fallingItem = None
        self.background = None
        self.list_length = 0
        self.num_tries = 0
        self.basket_list = []
        self.score = 0

        # (AH) Instantiate Scoreboard Class so Scoreboard(self) != Director(self)
        self.scoreboard = Scoreboard()

        # (AH) LATER equation_length should be a variable depending on Property.
        self.equation_length = 4

        self.text = (
            "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ = + "
            % (0, 10, "")
        )

    def setup(self):
        self.player = Player()
        self.scoreboard = Scoreboard()
        # Load background texture
        self.background = arcade.load_texture(constants.BACKGROUND)
        # Load game sounds
        self.collision_sound = arcade.load_sound(constants.COLLISION_SOUND)
        self.move_up_sound = arcade.load_sound(constants.MOVE_UP_SOUND)
        self.move_down_sound = arcade.load_sound(constants.MOVE_DOWN_SOUND)
        self.background_music = arcade.load_sound(constants.BACKGROUND_MUSIC)

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
        self.scoreboard.draw_scoreboard()
        arcade.finish_render()

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
        """
        hit_list = arcade.check_for_collision_with_list(
            self.player, self.falling_item_list
        )"""
        hit_list = []  # List of fruits caught by paddle
        for fruit in self.falling_item_list:
            # Comparison in x axis
            if fruit.left > self.player.left and fruit.right < self.player.right:
                # Comparison in y axis
                if 50 < fruit.bottom < 120:
                    hit_list.append(fruit)

                    # (AH) click sound when collected in basket.
                    arcade.play_sound(self.collision_sound)
                    # (AH) basket_list is equation to compare with math property.
                    self.basket_list.append(fruit.get_type())
                    # (AH) remove to release object from memory.
                    fruit.remove_from_sprite_lists()
                    self.list_length = self.list_length + 1

        if len(hit_list) > 0:

            # (AH) pass in parameters for this Scoreboard Instance.
            self.scoreboard.update_scoreboard(self.basket_list)

        if self.list_length >= self.equation_length:

            # (AH) pass in parameters for this Scoreboard Instance.
            self.scoreboard.update_score(
                self.basket_list,
                self.equation_length,
                self.score,
                self.move_up_sound,
                self.move_down_sound,
            )
            hit_list.clear()
            self.list_length = 0
            # (AH) empty basket_list of fruit.
            # (AH) Note: list is modified/cleared in place without rebinding.
            self.basket_list.clear()

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        self.player.center_x = x
        # self.player.center_y = y

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT:
            self.player.change_x = -7
        elif symbol == arcade.key.RIGHT:
            self.player.change_x = 7

        if symbol == arcade.key.Q:
            # Quit immediately
            arcade.close_window()

    def on_key_release(self, symbol: int, modifiers: int):
        self.player.change_x = 0
