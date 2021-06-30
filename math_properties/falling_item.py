import pygame
import random
from math_properties import constants

from math_properties.actor import Actor
from math_properties.point import Point


class FallingItem(pygame.sprite.Sprite):
    """
    Falling Items for Player to choose from to build an equation.
    In this case, the Falling Items will be colored shapes.

    The responsibility of FallingItems is to keep track of its
    appearance and position.
    NO: A ChoiceOption can move around randomly if asked to do so.

    Stereotype:
        Information Holder

    Attributes:  *** AGNES:  NOT NEEDED ***
        _points (integer): The number of points the fruit is worth.
    """

    def __init__(self):
        """The class constructor.
        Invokes the superclass constructor,
        moves the colored shape to a random position
        within the boundary of the screen.

        Args:
            self (Actor): an instance of Actor.
        """

        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([20, 20])

        # (AH) ???HELP want to fill in with red, green, blue.
        self.image.fill(constants.BLACK)
        self.rect = self.image.get_rect()

        # super().__init__()
        # self.set_text("@")
        # self.reset()

    # (AH) Method when item is collected by Player or falls off the screen.
    def reset_pos(self):
        # (AH) y range is below game screen dimensions.
        self.rect.y = random.randrange(constants.Y_RANDOM_MIN, constants.Y_RANDOM_MAX)
        self.rect.x = random.randrange(constants.SCREEN_WIDTH)

    # def reset(self):
    #     """
    #     Resets the fruit by moving it to a random position within the boundaries of the screen and reassigning the points to a random number.

    #     Args:
    #         self (Fruit): an instance of Fruit.
    #     """
    #     self._points = random.randint(1, 5)
    #     x = random.randint(1, constants.MAX_X - 2)
    #     y = random.randint(1, constants.MAX_Y - 2)
    #     position = Point(x, y)
    #     self.set_position(position)

    # (AH) Method to move item.
    def update(self):
        self.rect.y += 1

        if self.rect.y > SCREEN_HEIGHT + self.rect.height:
            self.reset_pos()
