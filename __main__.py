# program entry point

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
from asciimatics.screen import Screen

from math_properties import constants


def main(screen):

    # create the cast {key: tag, value: list}
    cast = {}

    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y - 1)
    position = Point(x, y)
    paddle = Actor()
    # (AH) shortened paddle for Math Properties final proj game.
    paddle.set_text("======")
    paddle.set_position(position)
    cast["paddle"] = [paddle]

    cast["number_letter"] = []
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
        num_let = Actor()
        num_let.set_text(falling_char)
        num_let.set_position(position)
        num_let.set_velocity(velocity)
        cast["number_letter"].append(num_let)

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

    # start the game
    director = Director(cast, script)
    director.start_game()


Screen.wrapper(main)
