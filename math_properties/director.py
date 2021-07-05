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
        self.text = "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ = + " %(0, 10, '')
        Scoreboard.__init__(self)

    def setup(self):
        self.player = Player()
        # Load background texture
        self.background = arcade.load_texture(constants.BACKGROUND)
        # Load game sounds
        self.collision_sound = arcade.load_sound("math_properties/assets/sd_0.wav")
        # self.move_down_sound = arcade.load_sound(".wav")
        self.background_music = arcade.load_sound("math_properties/assets/guitar-1.wav")

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
        # Collision: list and sound.
        hit_list = arcade.check_for_collision_with_list(
            self.player, self.falling_item_list
        )

        # (AH) remove to release object from memory.
        for fruit in hit_list:
            fruit.remove_from_sprite_lists()
            arcade.play_sound(self.collision_sound)
            self.list_length = self.list_length + 1
        if (len(hit_list) > 0):

            Scoreboard.update_scoreboard(self, hit_list) 
        
        if (self.list_length >= 4):

            Scoreboard.update_score(self)
            hit_list = []
            self.list_length = 0

        # (AH) for Beta Release, stop after one correct equation.
        # (AH) Conditional stmts to check for mastery.
        # if len(self.equation_list) >= self.equation_length:
            # self.num_tries += 1
            # if self.score / self.num_tries > 0.85:
                # (AH) End Sound.
               #  arcade.play_sound(self.background_music)
               #  arcade.close_window()

        # return
        # (AH) End block to verify Math Property.


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

