import os

# (AH) Arcade RGB screen colors work on additive process.
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (127, 127, 127)

# (AH) Arcade screen dimentions.
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
# (AH) for random below screen range.
Y_RANDOM_MIN = -300
Y_RANDOM_MAX = -20
# (AH) player sprite centered
PLAYER_CENTER = 50

# (AH) Arcade movement speed.
MOVEMENT_SPEED = 3

# # (AH) Game screen dimensions.
# MAX_X = 80
# MAX_Y = 20
FRAME_LENGTH = 0.1
PATH = os.path.dirname(os.path.abspath(__file__))

# (AH) Paddle length shortened for Math Properties final proj game.
# LEN_PADDLE = 6
# (AH) Artifacts and Messages from Robot finds Kitten program.
# MESSAGES = open(PATH + "/messages.txt").read().splitlines()
# ARTIFACTS = 30
