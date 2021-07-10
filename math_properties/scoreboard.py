import arcade
import time
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
                self.score = 0
                self.basket_list = []
        self.message = "Welcome!"
        self.point_percent = 0
        self.text = "Scoreboard:\npercent of mastery: %d \nminimum percent needed:  85\n\n     +                      =                +\n\n\n%s" %(self.point_percent,self.message)
        self.num_tries = 0
        self.sprites = arcade.SpriteList(None,128,True)
        self.list_length = 0
        self.start_x = constants.SCREEN_WIDTH - 200
        self.start_y = constants.SCREEN_HEIGHT - 60
        start_y2 = self.start_y - 15

        firstSprite = arcade.Sprite(constants.KIWI, .07, 0, 0, 40, 40,self.start_x-120, start_y2)
        self.sprites.append(firstSprite)
        secondSprite = arcade.Sprite(constants.KIWI, .07, 0, 0, 40, 40,self.start_x-40, start_y2)
        self.sprites.append(secondSprite)
        thirdSprite = arcade.Sprite(constants.KIWI, .07, 0, 0, 40, 40,self.start_x+40, start_y2)
        self.sprites.append(thirdSprite)
        fourthSprite = arcade.Sprite(constants.KIWI, .07, 0, 0, 40, 40, self.start_x+120, start_y2)
        self.sprites.append(fourthSprite)

        for sprite in self.sprites:
            sprite.append_texture(arcade.load_texture(constants.PINEAPPLE))
            sprite.append_texture(arcade.load_texture(constants.APPLE))
            sprite.append_texture(arcade.load_texture(constants.BANANA))
            sprite.append_texture(arcade.load_texture(constants.KIWI))
            sprite.append_texture(arcade.load_texture(constants.STRAWBERRY))
            sprite.append_texture(arcade.load_texture(constants.WATERMELON))
            sprite.append_texture(arcade.load_texture(constants.WHITE))

    def update_score(self, basket_list, equation_length, score):
                """updates the current score

        Equation checking happens here for falling items collected in basket.

        Args:
            self (Director): an instance of Director.
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

                        message_list = ["congrats! you got it right!", "Yeah, another point!", "keep up the good work!", "Yay! your doing awesome!"]
                        self.message = message_list[random.randint(0, 3)]

                        #if self.score / self.num_tries > 0.85 && num_tries >= 3:
                                #go to end screen
                else:
                        message_list = ["Keep trying!", "You can do this!", "awe, you'll get the point next time!", "keep at it!"]
                        self.message = message_list[random.randint(0, 3)]
                if(self.num_tries > 0) : self.point_percent = 100*(self.score/self.num_tries)
                self.basket_list = []
                self.num_tries = self.num_tries + 1
                self.text = "Scoreboard:\npercent of mastery: %d \nminimum percent needed: 85\n\n     +                      =                +\n\n\n%s" %(self.point_percent,self.message)
               
                for sprite in self.sprites:
                        sprite.set_texture(0)
                        
                self.sprites.update()
               

        def draw_scoreboard(self):
                """draws the scoreboard
        
        Args:
            self (Director): an instance of Director.
        """
                arcade.draw_point(self.start_x, self.start_y, arcade.color.WHITE, 300)
        arcade.draw_text(
            self.text,
            start_x,
            start_y,
            arcade.color.BLACK,
            12,
            anchor_x="center",
            anchor_y="center",
        )
                self.sprites.draw()

        def update_scoreboard(self, fruit):
                """updates the scoreboard with fruit caught and current score as well as how many points left to win.
        
        Args:
            self (Director): an instance of Director.
            hit_list: a list of fruit that have hit the basket.
        """
                self.list_length = len(self.basket_list)
                texture = -1

                # (SA) finds the right texture to use in the list.
                if ("pineapple" in fruit.texture.name):
                        texture = 1
                        self.basket_list.append("pineapple")
                elif ("apple" in fruit.texture.name):
                        texture = 2
                        self.basket_list.append("apple")
                elif ("banana" in fruit.texture.name):
                        texture = 3
                        self.basket_list.append("banana")
                elif ("kiwi" in fruit.texture.name):
                        texture = 4
                        self.basket_list.append("kiwi")
                elif ("strawberry" in fruit.texture.name):
                        texture = 5
                        self.basket_list.append("strawberry")
                elif ("watermelon" in fruit.texture.name):
                        texture = 6
                        self.basket_list.append("watermelon")

                # sets the texture
                self.list_length = len(self.basket_list)
                self.sprites.sprite_list[self.list_length-1].set_texture(texture)

                #sets the text shown
               
                self.text = "Scoreboard:\npercent of mastery: %d \nminimum percent needed: 85\n\n     +                      =                +\n\n\n%s" %(self.point_percent,self.message)
                self.sprites.update()
                
