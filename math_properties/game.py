# (AH) Import a library of functions called 'pygame'.
import pygame
import arcade
import random
from math_properties import constants
from math_properties import falling_item
from math_properties import player


class Game:
    """ (AH).
    This class represents an instance of the game.
    If we need to reset the game, we'd just need to create
    a new instance of this class.
    """

    # --- Class attributes.
    # In this case, all the data needed to run game.

    # (AH). Sprite lists.
    falling_item_list = None
    all_sprites_list = None
    player = None
    game_over = False

    # (AH) Other data.
    score = 0

    # --- Class methods.
    # Set up the game.
    def __init__(self):
        self.score = 0
        self.game_over = False

        # (AH) Create sprite lists.
        self.falling_item_list = pygame.sprite.Group()
        self.all_sprites_list = pygame.sprite.Group()

        # AGNES NEEDS HELP!
        # (AH) Create the falling_item sprites.
        for i in range(50):
            self.falling_item = FallingItem()

            self.falling_item.rect.x = random.randrange(constants.SCREEN_WIDTH)
            self.falling_item.rect.x = random.randrange(
                constants.Y_RANDOM_MIN, constants.SCREEN_HEIGHT
            )

            self.falling_item_list.add(self.falling_item)
            self.all_sprites_list.add(self.falling_item)

        # (AH) Create player.
        self.player = Player()
        self.all_sprites_list.add(self.player)

    # (AH) Process all of the events.  Return "True" if we need to close window.
    # def process_events(self):

    def on_key_press(self, key, modifiers):
        """ Called whenever a key is pressed.  """

        # (BL) If the player presses a key, update the speed.
        if key == arcade.key.UP:
            self.player_sprite.change_y = constants.MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -constants.MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = -constants.MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called when the user releases a key.  """

        # (BL) If the player releases a key, zero out the speed.
        #       This doesn't work well if multiple keys are pressed.
        #       Use 'better move by keyboard' eg if you need to handle this.
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


    # (AH) Method is run each time through frame,
    #       updates positions and checks for collisions.
    # ??
    falling_item_hit_list = []
    def run_logic(self):

        if not self.game_over:
            # (AH) Move all the sprites.
            self.all_sprites_list.update()

            # (AH) See if the player block has collided with anything.
            falling_item_hit_list = pygame.sprite.spritecollide(self.player, self.block_list, True)

            # (AH) Check the list of collisions.
            # ?? self. ?
            for self.falling_item in falling_item_hit_list:
                # (AH) ??? score differently.
                self.score += 1
                print(self.score)

            if len(self.falling_item_list) == 0:
                self.game_over = True

    # (AH) Display everything to the screen for the game.
    def display_frame(self, screen):

        # (AH) screen background is white color.
        screen.fill(constants.WHITE)

        if self.game_over:
            # font = pygame.font.Font("Serif", 25)
            font = pygame.font.SysFont("serif", 25)
            text = font.render("Game Over, click to restart", True, constants.BLACK)
            # (AH) center text.
            x = (constants.SCREEN_WIDTH // 2) - (text.get_width() // 2)
            y = (constants.SCREEN_HEIGHT // 2) - (text.get_height() // 2)
            screen.blit(text, [x, y])

        if not self.gamve_over:
            self.all_sprites_list.draw(screen)

        pygame.display.flip()


# --- Main Function ---
def main():

    # (AH) Initialize Pygame and set up the window.
    pygame.init()

    # (AH) Set the width and height of the screen.
    size = [constants.SCREEN_WIDTH, constants, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Math Properties Game")
    pygame.mouse.set_visible(False)

    # Create our objects and set the data.
    done = False
    clock = pygame.time.Clock()
    game = Game()

    # (AH) Main game loop.
    while not done:

        # (AH) Process events (keystrokes, mouse clicks, etc).
        done = game.process_events()

        # (AH) Update object positions, check for collisions.
        game.run_logic()

        # (AH) Draw the current frame.
        game.display_frame(screen)

        # (AH) Pause for the next frame.
        clock.tick(60)

    # (AH) Close window and exit.
    pygame.quit()

# (AH) Call the main function, start up the game.
if __name__ == "__main__":
    main()




