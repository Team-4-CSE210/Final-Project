import arcade
import random
from math_properties import constants
from math_properties.falling_item import FallingItem
from math_properties.scoreboard import Scoreboard
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
        self.score = 0
        self.basket_list = []
        self.text = "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ = + " %(0, 10, '')

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
        Scoreboard.draw_scoreboard(self)

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

        #Collision
        hit_list = arcade.check_for_collision_with_list(self.player, self.falling_item_list)
        for fruit in hit_list:
            # (AH) DEBUGGING CODE
            # print(f"Got {fruit.type}")
            fruit.remove_from_sprite_lists()
        if (len(hit_list) > 0):
            Scoreboard.update_scoreboard(self, hit_list)
        print(len(self.basket_list))  
        length = len(self.basket_list)  
        if (length >= 4):
            Scoreboard.update_score(self)
            hit_list = []

        # (AH) Conditional stmts to check for mastery.
        if len(self.equation_list) >= self.equation_length:
            self.num_tries += 1
            if self.score / self.num_tries > 0.85:
                # (AH) TODO Add Sound.
                # TODO print(Congratulation!)
                arcade.close_window()

        return
        # (AH) End block to verify Math Property.


        Scoreboard.update_scoreboard(hit_list, self)
        if(len(hit_list) == 4):
            Scoreboard.update_score(hit_list, self)

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

