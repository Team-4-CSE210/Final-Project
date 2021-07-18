import arcade

class Symbol(arcade.Sprite):
    def __init__(self, center_x, center_y):
        super().__init__(filename = None, center_x = center_x, center_y = center_y)
        self.height = 50
        self.width = 50

    
    def set_texture(self, texture):
        self.texture = texture
        self.height = 50
        self.width = 50