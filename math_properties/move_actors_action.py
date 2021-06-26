from math_properties import constants
from math_properties.action import Action
from math_properties.point import Point

class MoveActorsAction(Action):
    """A code template for moving actors. The responsibility of this class of
    objects is move any actor that has a velocity more than zero.

    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def execute(self, cast, choice_list):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        for group in cast.values():
            for actor in group:
                if not actor.get_velocity().is_zero():
                    self._move_actor(actor)

    def _move_actor(self, actor):
        """ (AH).
        Moves the given actor to its next position according to its
        velocity.

        In the Robot finds Kitten program:
        Will wrap the position from one side of the screen to the
        other when it reaches the edge in either direction.

        (AH). However, in this Batter program:
        the paddle will stop at the left and right side walls.

        Args:
            actor (Actor): The actor to move.
        """
        position = actor.get_position()
        velocity = actor.get_velocity()
        x1 = position.get_x()
        y1 = position.get_y()
        x2 = velocity.get_x()
        y2 = velocity.get_y()

        # (AH) Paddle Actor will move left and right between walls - No wrap.
        # x = 1 + (x1 + x2 - 1) % (constants.MAX_X - 1)
        # y = 1 + (y1 + y2 - 1) % (constants.MAX_Y - 1)
        x = 1 + (x1 + x2 - 1)
        y = 1 + (y1 + y2 - 1)

        position = Point(x, y)
        actor.set_position(position)
