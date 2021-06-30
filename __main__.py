# program entry point

import arcade
import random
from math_properties import constants
from math_properties.director import Director
from math_properties.actor import Actor
from math_properties.point import Point
from math_properties.control_actors_action import ControlActorsAction
from math_properties.draw_actors_action import DrawActorsAction
from math_properties.handle_collisions_action import HandleCollisionsAction
from math_properties.move_actors_action import MoveActorsAction
from math_properties.input_service import InputService
from math_properties.output_service import OutputService
# from asciimatics.screen import Screen



def main(screen):



    """
    # create the cast {key: tag, value: list}
    cast = {}

    # (AH) Block for paddle/catcher Actor.
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Actor()
    # (AH) shortened paddle for Math Properties final proj game.
    paddle.set_text("======")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    # (AH) Block for falling fruits and numbers.
    # (AH) cast is a dictionary because there are different kinds of actors.
    cast["fruitNnumber"] = []
    # (AH) velocity is going straight down y-axis from whichever x-axis.
    velocity = Point(0, 1)
    # (AH) try 5 falling characters each time.
    for i in range(5):
        falling_char = random.choice(
            ["D", "E", "F", "G", "H", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
        )
        x = random.randint(constants.LEN_PADDLE, constants.MAX_X - constants.LEN_PADDLE)
        y = 0
        position = Point(x, y)
        fruit_num = Actor()
        fruit_num.set_text(falling_char)
        fruit_num.set_position(position)
        fruit_num.set_velocity(velocity)
        cast["fruitNnumber"].append(fruit_num)

    # (AH) not having single ball in Math Properties game.
    # x = int(constants.MAX_X / 2)
    # y = int(constants.MAX_Y / 2)
    # position = Point(x, y)
    # velocity = Point(1, -1)
    # ball = Actor()
    # ball.set_text("@")
    # ball.set_position(position)
    # ball.set_velocity(velocity)
    # cast["ball"] = [ball]

    # create the script {key: tag, value: list}
    script = {}

    input_service = InputService(screen)
    output_service = OutputService(screen)
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)

    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]
"""

    # start the game
    director = Director(cast, script)
    director.start_game()


Screen.wrapper(main)

