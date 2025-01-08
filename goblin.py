from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
import pygame


class Goblin:

    def __init__(self, idle, walking, attack, w_width, w_height):
        self.sprite = Sprite(idle[0], 6)
        self.sprite.set_sequence_time(0, 1148, 100, True)
        self.sprite.set_position(w_width / 2 - 200, w_height / 2 - 200)
        self.tempo_animacao = 50/6
        self.tempo_atq_forte = 0
        self.tempo_atq_fraco = 0

        self.idle = idle
        self.walking = walking
        self.attack = attack

        self.vida = 3
        self.dano = 1

        self.direcao = 0

        self.atacou_forte = False

        self.cooldown_forte = 0


    def run(self, w_width, w_height, vel, delta_time):
        teclado = Keyboard()
        x = self.sprite.x
        y = self.sprite.y
        if (teclado.key_pressed("right") and self.sprite.x < w_width - self.sprite.width and not teclado.key_pressed("left")
                and self.tempo_atq_fraco <= 0 and self.tempo_atq_forte <= 0):
            self.direcao = 0
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.sprite.move_x(vel * delta_time)

        if (teclado.key_pressed("left") and self.sprite.x >= 0 and not teclado.key_pressed("right")
                and self.tempo_atq_fraco <= 0 and self.tempo_atq_forte <= 0):
            self.direcao = 1
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.sprite.move_x(vel * delta_time * (-1))

        if (teclado.key_pressed("down") and self.sprite.y <= w_height - self.sprite.height and not teclado.key_pressed("up")
                and self.tempo_atq_fraco <= 0 and self.tempo_atq_forte <= 0):
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.sprite.move_y(vel * delta_time)

        if (teclado.key_pressed("up") and self.sprite.y >= 0 and not teclado.key_pressed("down")
                and self.tempo_atq_fraco <= 0 and self.tempo_atq_forte <= 0):
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.sprite.move_y(vel * delta_time * (-1))

        if (x == self.sprite.x and y == self.sprite.y and not teclado.key_pressed("e") and not teclado.key_pressed("q")
                and self.tempo_atq_fraco <= 0 and self.tempo_atq_forte <= 0):
            self.sprite.image = pygame.image.load(self.idle[self.direcao]).convert_alpha()

    def attack_action(self, delta_time):
        teclado = Keyboard()
        self.cooldown_forte -= delta_time

        if teclado.key_pressed("e") and not self.atacou_forte:
            self.sprite.image = pygame.image.load(self.attack[self.direcao]).convert_alpha()
            self.atacou_forte = True
            self.cooldown_forte = 2
            self.tempo_atq_forte = 50 / 6

        self.tempo_atq_forte -= (100 / 6) * delta_time

        if self.cooldown_forte <= 0:
            self.atacou_forte = False

    def play_n_drawn(self, delta_time):

        if self.tempo_animacao <= 0:
            self.sprite.stop()
            self.tempo_animacao = 50/6
        self.tempo_animacao -= delta_time * (100/6)

        self.sprite.play()
        self.sprite.update()
        self.sprite.draw()
