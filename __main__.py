import arcade
from math_properties.menu_view import MenuView
from math_properties.constants import SCREEN_HEIGHT, SCREEN_TITLE, SCREEN_WIDTH


window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
start_view = MenuView()
window.show_view(start_view)
arcade.run()
