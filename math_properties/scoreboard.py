import arcade
import random
from math_properties import constants
from math_properties.symbol import Symbol


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

        ##  Game vars
        self.times_wrong = 0
        self.points_left = 10
        self.list_length = 0
        self.score = 0


        ##  Texts for display
        self.text_score = "Scoreboard:\nScore: %d \nScore to win: 8" % (self.score)
        self.text_equation = "+              =              +"
        self.text_message = "Welcome!"

        ##  Textures Construction
        self.textures = {}

        self.textures["pineapple"] = arcade.load_texture(constants.PINEAPPLE)
        self.textures["apple"] = arcade.load_texture(constants.APPLE)
        self.textures["banana"] = arcade.load_texture(constants.BANANA)
        self.textures["kiwi"] = arcade.load_texture(constants.KIWI)
        self.textures["strawberry"] = arcade.load_texture(constants.STRAWBERRY)
        self.textures["watermelon"] = arcade.load_texture(constants.WATERMELON)
        self.textures["grapes"] = arcade.load_texture(constants.GRAPES)
        self.textures["checkbox"] = arcade.load_texture(constants.CHECKBOX)


        ##  Symbols Construction

        self.start_x = constants.SCREEN_WIDTH - 200
        self.start_y = constants.SCREEN_HEIGHT - 60

        it_pos_x = self.start_x - 120
        var_x = 80

        start_y2 = self.start_y - 42 #32
        self.symbols_list = arcade.SpriteList()
        for i in range(4):
            sprite = Symbol(it_pos_x, start_y2)
            sprite.set_texture(self.textures["checkbox"])
            self.symbols_list.append(sprite)

            it_pos_x += var_x


    def update_score(
        self, basket_list, equation_length, move_up_sound, move_down_sound
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


        #   If basket is full
        if len(basket_list) == equation_length:

            # (AH) correct eqn for Commutative Property of Addition.
            if basket_list[2] == basket_list[1] and basket_list[3] == basket_list[0]:

                self.score += 1

                message_list = [
                    "Congrats! You got it right!",
                    "Yeah, another point!",
                    "Keep up the good work!",
                    "Yay! You're doing awesome!",
                ]
                self.text_message = message_list[random.randint(0, 3)]

                # (AH) applause sound when correct.
                arcade.play_sound(move_up_sound)

            # (AH) incorrect eqn for Commutative Property of Addition.
            else:
                self.times_wrong += 1
                message_list = [
                    "Keep trying!",
                    "You can do this!",
                    "awe, you'll get the point next time!",
                    "Keep at it!",
                ]
                self.text_message = message_list[random.randint(0, 3)]

                # (AH) gonk sound when incorrect.
                arcade.play_sound(move_down_sound)

        self.text_score = "Scoreboard:\nScore: %d \nScore to win: 8" % (self.score)

        return

    def update_scoreboard(self, basket_list):
        """updates the scoreboard with fruit caught and current score as well as how many points left to win.

        Args:
            self (Director): an instance of Director.
            basket_list: a list of fruit that have hit the basket.
        """

        self.list_length = len(basket_list)
        sprite = self.textures["checkbox"]
        for fruit in basket_list:

            # (AH) see Director Class retrieve info from Falling_Item Class get_type Method.
            # self.basket_list.append(fruit.get_type())
            sprite = self.textures[fruit]

        # sets the texture
        if 1 == self.list_length:
            for i in self.symbols_list[1:]:
                i.set_texture(self.textures["checkbox"])
            self.symbols_list[0].set_texture(sprite)

        else:
            self.symbols_list[self.list_length -1].set_texture(sprite)


        # sets the text shown
        self.text_score = (
            "Scoreboard:\nScore: %d \nScore to win: 8\n"
            % (self.score)
        )

    def draw_scoreboard(self):
        """draws the scoreboard

        Args:
            self (Director): an instance of Director.
        """
        #Draw Rectangle Background
        arcade.draw_point(self.start_x, self.start_y, arcade.color.WHITE, 300)


        #Draw Sprites
        self.symbols_list.draw()


        #Draw Texts
        #Score
        arcade.draw_text(self.text_score, self.start_x, self.start_y + 20, \
        arcade.color.BLACK, 16, anchor_x='center', anchor_y='center', bold = True)

        #Equation
        arcade.draw_text(self.text_equation, self.start_x, self.start_y - 50, \
        arcade.color.BLACK, 18, anchor_x='center', anchor_y='center', bold = True)

        #Message
        arcade.draw_text(self.text_message, self.start_x, self.start_y - 100, \
        arcade.color.BLACK, 15, anchor_x='center', anchor_y='center', bold = True)
