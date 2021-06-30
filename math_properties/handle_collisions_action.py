import random
from math_properties import constants
from math_properties.action import Action
from math_properties.point import Point


class HandleCollisionsAction(Action):
    """
    A code template for handling collisions.
    The responsibility of this class of objects is to
    update the game state when actors collide.

    Stereotype:
        Controller
    """

    def execute(self, cast, choice_list):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._fruitNnumber_paddle_collision(cast, choice_list)

        # paddle = cast["paddle"][0]  # there's only one

    def _fruitNnumber_paddle_collision(self, cast, choice_list):
        """
        Handles the collision of the fruitNnumber hitting the paddle/catcher.

        Args:
            cast (dict): the game actors {key: tag, value: list}.
        """
        fruitNnumber_list = cast["fruitNnumber"]
        paddle = cast["paddle"][0]

        # (AH) cannot use paddle.get_position() because paddle not a pt.
        paddle_pt = paddle.get_position()
        paddle_pt_x = paddle_pt.get_x()
        paddle_pt_y = paddle_pt.get_y()
        # fruitNnumber_vel = fruitNnumber.get_velocity()
        # (AH) don't care about velocity of fruitNnumber.

        # (AH) Loop to find position of individual number or letter.
        for index, fruit_num in enumerate(fruitNnumber_list):

            # (AH) check if ball and paddle on same y-coord.
            if fruit_num.get_position().get_y() == paddle_pt_y:

                # (AH) check if ball is between left and right edges of paddle.
                if (
                    paddle_pt_x
                    <= fruit_num.get_position().get_x()
                    <= paddle_pt_x + constants.LEN_PADDLE - 1
                ):

                    choice_list.append(fruit_num)

                    # (AH) math_property game: fruit won't bounce off catcher.
                    # (AH) change ball velocity to opposite y-direction.
                    # opp_vel = Point(ball_vel.get_x(), -ball_vel.get_y())
                    # ball.set_velocity(opp_vel)

                    # (AH) Delete brick when ball collides.
                    # (AH) then exit loop because loop has changed after pop.
                    fruitNnumber_list.pop(index)
                    break
