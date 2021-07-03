class Scoreboard(arcade):

def __init__(self):
        
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.WHITE)
        self.text_angle = 0
        self.time_elapsed = 0.0
        self.score = 0


def update_score(id_list, self):
    if (id_list[0] == id_list[3] and id_list[1] == id_list[2]):
        score = score + 1
        #display score +1

def draw_scoreboard(self):

        start_x = 50
        start_y = 400
        arcade.draw_point(start_x, start_y, arcade.color.BLUE, 5)
        arcade.draw_text("Text anchored 'top' and 'left'.",
                         start_x, start_y, arcade.color.BLACK, 12, anchor_x="left", anchor_y="top")
