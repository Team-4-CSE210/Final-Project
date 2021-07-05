import arcade
from math_properties import constants
import time


class Scoreboard:
    """A class that keeps track of the scoreboard.

        Attributes:
        self: an instance of Scoreboard
        """

    def __init__(self):
        """The class constructor.

        Args:
            self (Scoreboard): an instance of Scoreboard.
        """
        self.score = 0
        self.basket_list = []
        self.move_up_sound = arcade.load_sound("math_properties/assets/applause.wav")

    def update_score(self):
        """updates the current score

        Args:
            self (Director): an instance of Director.
        """
        if (
            self.basket_list[0] == self.basket_list[3]
            and self.basket_list[1] == self.basket_list[2]
        ):
            self.score = self.score + 1
            arcade.play_sound(self.move_up_sound)
            # (AH) for Beta Release, stop after one correct equation.
            time.sleep(5)
            arcade.close_window()

        self.basket_list = []
        # self.num_tries += 1
        # if self.score / self.num_tries > 0.85:
        # (AH) TODO Add Sound.
        # TODO print(Congratulation!)
        # arcade.close_window()

    def draw_scoreboard(self):
        """draws the scoreboard

        Args:
            self (Director): an instance of Director.
        """

        start_x = constants.SCREEN_WIDTH - 150
        start_y = constants.SCREEN_HEIGHT - 30
        arcade.draw_point(start_x, start_y, arcade.color.WHITE, 300)
        arcade.draw_text(
            self.text,
            start_x,
            start_y,
            arcade.color.BLACK,
            12,
            anchor_x="center",
            anchor_y="center",
        )

    def update_scoreboard(self, hit_list):
        """updates the scoreboard with fruit caught and current score as well as how many points left to win.

        Args:
            self (Director): an instance of Director.
            hit_list: a list of fruit that have hit the basket.
        """
        for fruit in hit_list:
            if "watermelon" in fruit.texture.name:
                self.basket_list.append("watermelon")
            elif "strawberry" in fruit.texture.name:
                self.basket_list.append("strawberry")
            elif "pineapple" in fruit.texture.name:
                self.basket_list.append("pineapple")
            elif "apple" in fruit.texture.name:
                self.basket_list.append("apple")
            elif "banana" in fruit.texture.name:
                self.basket_list.append("banana")
            elif "kiwi" in fruit.texture.name:
                self.basket_list.append("kiwi")

        points_left = 10 - self.score
        length = len(self.basket_list)
        if length == 0:
            self.text = (
                "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ = + "
                % (self.score, points_left, "")
            )
        elif length == 1:
            self.text = (
                "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ = + "
                % (self.score, points_left, self.basket_list[0])
            )
        elif length == 2:
            self.text = (
                "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ %s= + "
                % (self.score, points_left, self.basket_list[0], self.basket_list[1])
            )
        elif length == 3:
            self.text = (
                "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ %s= %s+ "
                % (
                    self.score,
                    points_left,
                    self.basket_list[0],
                    self.basket_list[1],
                    self.basket_list[2],
                )
            )
        elif length == 4:
            self.text = (
                "Scoreboard:\nearned points: %d \npoints till next level: %d\n %s+ %s= %s+ %s"
                % (
                    self.score,
                    points_left,
                    self.basket_list[0],
                    self.basket_list[1],
                    self.basket_list[2],
                    self.basket_list[3],
                )
            )
