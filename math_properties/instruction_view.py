import arcade
from math_properties import constants
from math_properties.director import Director


class ExampleSymbol(arcade.Sprite):
    def __init__(self, filename, center_x, center_y):
        super().__init__(filename=filename, center_x = center_x, center_y=center_y)

        self.height = 50
        self.width = 50


class ExamplePath():
    def __init__(self, center_x, center_y):
        
        self.sprites = arcade.SpriteList()
        
        filenames = [constants.BANANA, constants.ADDITION, constants.APPLE, \
        constants.EQUAL, constants.APPLE, constants.ADDITION, constants.BANANA]
        
        it_pos = center_x
        var_x = 50

        for filename in filenames:
            sp = ExampleSymbol(filename, it_pos, center_y)
            self.sprites.append(sp)
            
            it_pos += var_x
        
        
    def draw(self):
        self.sprites.draw()
        

class InstructionView(arcade.View):
    def __init__(self):
        super().__init__()

        self.equation1 = ExamplePath(450, 230)
        

    def on_show(self):
        arcade.set_background_color(arcade.color.PASTEL_ORANGE)

    def on_draw(self):
        arcade.start_render()

        self.equation1.draw()
        arcade.draw_text(
            "Instructions",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 1.5,
            arcade.color.BLACK,
            font_size=50,
            anchor_x="center",
        )

        arcade.draw_text(
            "Commutative Property of Addition: A + B = B + A",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 1.9, #75
            arcade.color.BLACK,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Collect fruit matching the pattern:",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - 45,
            arcade.color.PURPLE,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Type 'q' to quit.",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - (3 * 75),
            arcade.color.RED,
            font_size=20,
            anchor_x="center",
        )
        arcade.draw_text(
            "Click to advance",
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2 - (4 * 75),
            arcade.color.GRAY,
            font_size=20,
            anchor_x="center",
        )

       

    def on_mouse_press(self, x: float, y: float, dx: float, dy: float):
        game_view = Director()
        game_view.setup()
        self.window.show_view(game_view)
