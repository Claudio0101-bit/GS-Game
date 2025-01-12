from PPlay.sprite import Sprite

class Build:

    def __init__(self, sprite, posicion_width, posicion_height):

        self.sprite = Sprite(sprite, 1)
        self.sprite.set_position(posicion_width, posicion_height)

        self.vida = 10



