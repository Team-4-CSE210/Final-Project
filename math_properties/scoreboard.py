import arcade
from math_properties import constants

class Scoreboard():


        def update_score(fruit_list, self):
                if (fruit_list[0] == fruit_list[3] and fruit_list[1] == fruit_list[2]):
                        self.score = self.score + 1
                #display score +1

        def draw_scoreboard(self):

                start_x = constants.SCREEN_WIDTH - 150
                start_y = constants.SCREEN_HEIGHT - 30
                arcade.draw_point(start_x, start_y, arcade.color.WHITE, 200)
                arcade.draw_text("Scoreboard:\nearned points: 0\npoints till next level: 10\n + = +",
                start_x, start_y, arcade.color.BLACK, 12, anchor_x="center", anchor_y="center")

        def update_scoreboard(basket_list, self):
                start_x = constants.SCREEN_WIDTH - 150
                start_y = constants.SCREEN_HEIGHT - 30
                arcade.draw_point(start_x, start_y, arcade.color.WHITE, 200)
                points_left = 10 -self.score
                length = len(basket_list)
                if (length == 0):
                        text = "Scoreboard:\nearned points: 0\npoints till next level: 10\n + = +"
                elif(length == 1):
                         text = ("Scoreboard:\nearned points: {self.score}\npoints till next level: {points_left}\n {basket_list[0]}+ = + ")
                elif(length == 2):
                         text = ("Scoreboard:\nearned points: {self.score}\npoints till next level: {points_left}\n {basket_list[0]}+ {basket_list[1]}= + ")
                elif(length == 3):
                         text = ("Scoreboard:\nearned points: {self.score}\npoints till next level: {points_left}\n {basket_list[0]}+ {basket_list[1]}= {basket_list[2]}+ ")
                elif(length == 4):
                        text = ("Scoreboard:\nearned points: {self.score}\npoints till next level: {points_left}\n {basket_list[0]}+ {basket_list[1]}= {basket_list[2]}+{basket_list[3]}")
                arcade.draw_text(text, start_x, start_y, arcade.color.BLACK, 12, anchor_x="center", anchor_y="center")
