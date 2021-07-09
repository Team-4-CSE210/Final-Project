import os
import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 700
SCREEN_TITLE = "FRUIT MATH: Commutative Property of Addition: A + B = B + A"

PATH = os.path.dirname(os.path.abspath(__file__))
PADDLE_SPRITE_PATH = PATH + "/assets/paddle.png"
BACKGROUND = PATH + "/assets/jungle.jpg"
APPLE = PATH + "/assets/apple.png"
BANANA = PATH + "/assets/banana.png"
GRAPES = PATH + "/assets/grapes.png"
KIWI = PATH + "/assets/kiwi.png"
PINEAPPLE = PATH + "/assets/pineapple.png"
STRAWBERRY = PATH + "/assets/strawberry.png"
WATERMELON = PATH + "/assets/watermelon.png"

# (AH) Game Sounds:
# collision_sound when fruit collected in basket.
COLLISION_SOUND = arcade.load_sound("math_properties/assets/sd_0.wav")
# move_up_sound when equation is correct.
MOVE_UP_SOUND = arcade.load_sound("math_properties/assets/applause.wav")
# move_down_sound when equation is incorrect.
MOVE_DOWN_SOUND = arcade.load_sound("math_properties/assets/gong.wav")
# using background_music as end of game sound.
BACKGROUND_MUSIC = arcade.load_sound("math_properties/assets/Won!.wav")

# (AH) Arcade RGB screen colors work on additive process.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (127, 127, 127)
