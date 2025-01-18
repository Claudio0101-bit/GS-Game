from PPlay.sprite import Sprite
from PPlay.gameimage import GameImage

class Build:

    def __init__(self, sprite, position_width, position_height):

        self.sprite = sprite
        self.hit_box = GameImage("Assets Resized/hit_explosao.png")
        self.hit_box.set_position(position_width, position_height)
        self.x = position_width
        self.y = position_height
        self.width = self.sprite.width
        self.height = self.sprite.height
        self.movable = False
        self.playable = False
        self.larga = False
        self.alta = False

        self.vel = 0

        self.vida = 10

    def play_n_drawn(self, d_time):
        self.sprite.set_position(self.x, self.y)
        if self.larga and self.alta:
            self.hit_box.set_position(self.x + 28, self.y + 115)
        elif self.alta:
            self.hit_box.set_position(self.x + 28, self.y + 115)
        else:
            self.hit_box.set_position(self.x + 28, self.y + 88)
        self.sprite.draw()
        self.hit_box.draw()


