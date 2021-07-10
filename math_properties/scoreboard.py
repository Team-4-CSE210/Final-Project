import arcade
from math_properties import constants
import random


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
        self.text = "Scoreboard:\npercent of mastery: %d \nminimum percent needed:  85\n\n     +" \
                    "                      =                +\n\n\n%s" % (self.point_percent, self.message)
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

        self.firstSprite = arcade.Sprite(None, .08, 0, 0, 0, 0, self.start_x - 120, start_y2)
        self.firstSprite = self.white

        self.secondSprite = arcade.Sprite(None, .08, 0, 0, 0, 0, self.start_x - 40, start_y2)
        self.secondSprite = self.white

        self.thirdSprite = arcade.Sprite(None, .08, 0, 0, 0, 0, self.start_x + 40, start_y2)
        self.thirdSprite = self.white

        self.fourthSprite = arcade.Sprite(None, .08, 0, 0, 0, 0, self.start_x + 120, start_y2)
        self.fourthSprite = self.white

    def update_score(self, basket_list, equation_length, score):
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
            if basket_list[2] == basket_list[1] and basket_list[3] == basket_list[0]:
                score += 1
                # (AH) applause sound when correct.
                constants.MOVE_UP_SOUND

            else:
                # (AH) gonk sound when incorrect.
                constants.MOVE_DOWN_SOUND

            message_list = ["congrats! you got it right!", "Yeah, another point!", "keep up the good work!",
                            "Yay! your doing awesome!"]
            self.message = message_list[random.randint(0, 3)]

            # if self.score / self.num_tries > 0.85 && num_tries >= 3:
            # go to end screen
        else:
            message_list = ["Keep trying!", "You can do this!", "awe, you'll get the point next time!", "keep at it!"]
            self.message = message_list[random.randint(0, 3)]
        if self.num_tries > 0:
            self.point_percent = 100 * (score / self.num_tries)
        self.num_tries = self.num_tries + 1
        self.text = "Scoreboard:\npercent of mastery: %d \nminimum percent needed: 85\n\n     +" \
                    "                      =                +\n\n\n%s" % (self.point_percent, self.message)

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
            # (SA) finds the right texture to use in the list.
            if ("pineapple" in fruit.texture.name):
                sprite = self.pineapple

            elif ("apple" in fruit.texture.name):
                sprite = self.apple

            elif ("banana" in fruit.texture.name):
                sprite = self.banana

            elif ("kiwi" in fruit.texture.name):
                sprite = self.kiwi

            elif ("strawberry" in fruit.texture.name):
                sprite = self.strawberry

            elif ("watermelon" in fruit.texture.name):
                sprite = self.watermelon

        # sets the texture
        if (1 == self.list_length):
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
        self.text = "Scoreboard:\npercent of mastery: %d \nminimum percent needed: 85\n\n     +" \
                    "                      =                +\n\n\n%s" % (self.point_percent, self.message)
