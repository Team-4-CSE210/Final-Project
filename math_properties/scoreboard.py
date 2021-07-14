import arcade
import random
from math_properties import constants


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
        self.message = "Welcome!"
        self.point_percent = 0
        self.text = (
            "Scoreboard:\npercent of mastery: %d \nminimum percent needed:  85\n\n     +"
            "                      =                +\n\n\n%s"
            % (self.point_percent, self.message)
        )
        self.num_tries = 0
        self.list_length = 0
        self.start_x = constants.SCREEN_WIDTH - 200
        self.start_y = constants.SCREEN_HEIGHT - 60
        start_y2 = self.start_y - 15

        self.pineapple = arcade.load_texture(constants.PINEAPPLE)
        self.apple = arcade.load_texture(constants.APPLE)
        self.banana = arcade.load_texture(constants.BANANA)
        self.kiwi = arcade.load_texture(constants.KIWI)
        self.strawberry = arcade.load_texture(constants.STRAWBERRY)
        self.watermelon = arcade.load_texture(constants.WATERMELON)
        self.white = arcade.load_texture(constants.WHITESPRITE)

        self.firstSprite = arcade.Sprite(
            None, 0.08, 0, 0, 0, 0, self.start_x - 120, start_y2
        )
        self.firstSprite.texture = self.white

        self.secondSprite = arcade.Sprite(
            None, 0.08, 0, 0, 0, 0, self.start_x - 40, start_y2
        )
        self.secondSprite.texture = self.white

        self.thirdSprite = arcade.Sprite(
            None, 0.08, 0, 0, 0, 0, self.start_x + 40, start_y2
        )
        self.thirdSprite.texture = self.white

        self.fourthSprite = arcade.Sprite(
            None, 0.08, 0, 0, 0, 0, self.start_x + 120, start_y2
        )
        self.fourthSprite.texture = self.white

    def update_score(
        self, basket_list, equation_length, score, move_up_sound, move_down_sound
    ):
        """
            updates the current score

        Equation checking happens here for falling items collected in basket.

        Args:
            self (Director): an instance of Director.
                :param score:
                :param equation_length:
                :param basket_list:
        """
        # (AH) Begin block to verify Math Property.
        # (AH) include collected fruit into equation basket list.

        # (AH) check if enough fruit has been collected for the equation.
        # (AH) NOW only checking for Commutative Property of Addition.
        # (AH) LATER use Math Class to check for all math properties.
        if len(basket_list) == equation_length:

            # (AH) correct eqn for Commutative Property of Addition.
            if basket_list[2] == basket_list[1] and basket_list[3] == basket_list[0]:

                score += 1

                message_list = [
                    "Congrats! You got it right!",
                    "Yeah, another point!",
                    "Keep up the good work!",
                    "Yay! You're doing awesome!",
                ]
                self.message = message_list[random.randint(0, 3)]

                # (AH) applause sound when correct.
                arcade.play_sound(move_up_sound)

            # (AH) incorrect eqn for Commutative Property of Addition.
            else:
                message_list = [
                    "Keep trying!",
                    "You can do this!",
                    "awe, you'll get the point next time!",
                    "Keep at it!",
                ]
                self.message = message_list[random.randint(0, 3)]

                # (AH) gonk sound when incorrect.
                arcade.play_sound(move_down_sound)

        self.num_tries = self.num_tries + 1
        if self.num_tries > 0:
            self.point_percent = 100 * (score / self.num_tries)
        
        # if self.point_percent >= 85 and num_tries >= 3:
            #send to end screen or return a true so director can send to end screen.
        
        self.text = (
            "Scoreboard:\npercent of mastery: %d \nminimum percent needed: 85\n\n     +"
            "                      =                +\n\n\n%s"
            % (self.point_percent, self.message)
        )
        return score

    def draw_scoreboard(self):
        """draws the scoreboard

        Args:
            self (Director): an instance of Director.
        """
        arcade.draw_point(self.start_x, self.start_y, arcade.color.WHITE, 300)
        arcade.draw_text(
            self.text,
            self.start_x,
            self.start_y,
            arcade.color.BLACK,
            12,
            anchor_x="center",
            anchor_y="center",
        )
        self.firstSprite.draw()
        self.secondSprite.draw()
        self.thirdSprite.draw()
        self.fourthSprite.draw()

    def update_scoreboard(self, basket_list):
        """updates the scoreboard with fruit caught and current score as well as how many points left to win.

        Args:
            self (Director): an instance of Director.
            basket_list: a list of fruit that have hit the basket.
        """

        self.list_length = len(basket_list)
        sprite = self.white
        for fruit in basket_list:

            # (AH) see Director Class retrieve info from Falling_Item Class get_type Method.
            # self.basket_list.append(fruit.get_type())

            if fruit == "pineapple":
                sprite = self.pineapple

            elif fruit == "apple":
                sprite = self.apple

            elif fruit == "banana":
                sprite = self.banana

            elif fruit == "kiwi":
                sprite = self.kiwi

            elif fruit == "strawberry":
                sprite = self.strawberry

            elif fruit == "watermelon":
                sprite = self.watermelon

        # sets the texture
        if 1 == self.list_length:
            self.secondSprite.texture = arcade.load_texture(constants.WHITESPRITE)
            self.thirdSprite.texture = arcade.load_texture(constants.WHITESPRITE)
            self.fourthSprite.texture = arcade.load_texture(constants.WHITESPRITE)
            self.firstSprite.texture = sprite
        elif 2 == self.list_length:
            self.secondSprite.texture = sprite
        elif 3 == self.list_length:
            self.thirdSprite.texture = sprite
        elif 4 == self.list_length:
            self.fourthSprite.texture = sprite

        # sets the text shown
        self.text = (
            "Scoreboard:\npercent of mastery: %d \nminimum percent needed: 85\n\n     +"
            "                     =                +\n\n\n%s"
            % (self.point_percent, self.message)
        )
