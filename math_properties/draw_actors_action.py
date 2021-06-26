from math_properties.action import Action

# TODO: Define the DrawActorsAction class here


class DrawActorsAction(Action):
    """ (AH).
    NO ARTIFACTS

    Outputs the screen with artifacts.
    The responsibility of the class of objects is to draw the game state
    on the terminal.

    Stereotype:
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self, output_service):
        """
        The class constructor.

        Args:
            screen (Screen): An Asciimatics Screen.
        """

        # (AH) from _main.py, we know we need output_service as parameter.
        # (AH) draw_actors_action = DrawActorsAction(output_service)

        # (AH) the Action parent class has no init method, so delete.
        # super().__init__()

        self._output_service = output_service

    # (AH) ToDo: override Action.execute Method.
    # (AH) Copied from Action.execute Method.
    def execute(self, cast, choice_list):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        # raise NotImplementedError("execute not implemented in superclass")

        # (AH) see Agnes' Snake program, Director Class, _do_outputs Method.

        # (AH) clear_screen() before drawing loop.
        self._output_service.clear_screen()
        for actor in cast.values():

            # self._output_service.draw_actor(actor)

            self._output_service.draw_actors(actor)
            # (AH) loop through draw_actors.

            # self._output_service.draw_actor(self._score)
            # (AH) don't keep score in Robot finds Kitten.

        # (AH) flush_buffer after drawing loop.
        self._output_service.flush_buffer()
