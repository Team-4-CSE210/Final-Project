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
        self.basket_list = []
        # self.score = 0


        # (AH) Instantiate Scoreboard Class so Scoreboard(self) != Director(self)
        self.scoreboard = Scoreboard()

        # (AH) LATER equation_length should be a variable depending on Property.
        self.equation_length = 4

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

    def on_update(self, delta_time: float):
        self.current_time += 1

        self.falling_item_list.update()
        if self.current_time % 50 == 0:
            fruit = FallingItem(
                random.choice(
                    constants.FRUITLIST
                )
            )
            self.falling_item_list.append(fruit)

        for fr in self.falling_item_list:
            fr.update()
            if fr.center_y < 0:
                fr.kill()
        self.player.update()

        # Collision
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
                self.move_up_sound,
                self.move_down_sound,
            )
            hit_list.clear()
            self.list_length = 0
            # (AH) empty basket_list of fruit.
            # (AH) Note: list is modified/cleared in place without rebinding.
            self.basket_list.clear()

        # Game Over if >= 5 incorrect.
        if  self.scoreboard.times_wrong >= 5:
            game_view = GameOverView(self.scoreboard.score, self.current_time)
            self.window.show_view(game_view)

        # Win Game if >= 8 correct.
        if self.scoreboard.score >= 8:
            game_view = WinGameView(self.scoreboard.score, self.current_time)
            self.window.show_view(game_view)



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



####    Game Over View    ####
class GameOverView(arcade.View):
    def __init__(self, score, current_time):
        super().__init__()
        self.time_taken = current_time/60
        self.score = score



    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)
        # (AH) load game over sound.
        self.background_music = arcade.load_sound(constants.BACKGROUND_MUSIC)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH/2, 400, arcade.color.WHITE, 54, anchor_x="center")
        arcade.draw_text("Click to restart", constants.SCREEN_WIDTH/2, 300, arcade.color.WHITE, 24, anchor_x="center")

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         constants.SCREEN_WIDTH/2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

        # (AH) play fanfare game over sound.
        #arcade.play_sound(self.background_music)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)



### Win Game View  ###
class WinGameView(arcade.View):
    def __init__(self, score, current_time):
        super().__init__()
        self.time_taken = current_time/60
        self.score = score

    def on_show(self):
        arcade.set_background_color(arcade.color.BLUEBERRY)
        # (AH) load game over sound.
        self.background_music = arcade.load_sound(constants.MOVE_UP_SOUND)

    def on_draw(self):
        arcade.start_render()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("YOU WON!", constants.SCREEN_WIDTH/2, 400, \
        arcade.color.SCHOOL_BUS_YELLOW, 54, anchor_x = 'center')
        arcade.draw_text("Click to restart", constants.SCREEN_WIDTH/2, 300, arcade.color.BLACK, 24, anchor_x="center")

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         constants.SCREEN_WIDTH/2,
                         200,
                         arcade.color.BLACK,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.BLACK, 14)

        # (AH) play fanfare game over sound.
        #arcade.play_sound(self.background_music)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)
