from PPlay.gameimage import GameImage
from PPlay.sprite import Sprite
from PPlay.keyboard import Keyboard
import pygame


class Goblin:

    def __init__(self, w_width, w_height, vel):

        self.idle = ("Goblin_Red_FILAS/Parado_Right.png", "Goblin_Red_FILAS/Parado_Left.png")

        self.walking = ("Goblin_Red_FILAS/Andando_Right.png", "Goblin_Red_FILAS/Andando_Left.png")

        self.attack = ("Goblin_Red_FILAS/Atacando_Right.png", "Goblin_Red_FILAS/Atacando_Left.PNG")


        self.sprite = Sprite(self.idle[0], 6)
        self.sprite.set_sequence_time(0, 1152, 100, True)

        self.hit_box = GameImage("Assets Resized/hitbox.png")
        self.hit_attack = GameImage("Assets Resized/hit_attack.png")

        self.x = 10 * 64
        self.y = 20 * 64

        self.hit_box.x = self.x + 72
        self.hit_box.y = self.y + 80

        self.movable = True
        self.playable = False

        self.tempo_animacao = 50 / 6
        self.tempo_atq_forte = 0
        self.tempo_animacao_morte = 50 / 7

        self.vida = 5
        self.dano = 1
        self.took_damage = 0
        self.vel = vel * 0.5

        self.direcao = 0

        self.atacou_forte = False
        self.cooldown_forte = 0

    def run(self, w_width, w_height, delta_time, p_x, p_y, p_w, p_h):
        vel = self.vel
        x = self.x
        y = self.y
        if self.hit_box.x + self.hit_box.width < p_x and self.hit_box.x < w_width - self.hit_box.width and self.tempo_atq_forte <= 0:
            self.direcao = 0
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.x += (vel * delta_time)

        if self.hit_box.x > p_x + p_w and self.hit_box.x >= 0 >= self.tempo_atq_forte:
            self.direcao = 1
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.x += (vel * delta_time * (-1))

        if self.hit_box.y + self.hit_box.height < p_y and self.hit_box.y <= w_height - self.hit_box.height and self.tempo_atq_forte <= 0:
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.y += (vel * delta_time)

        if self.hit_box.y > p_y + p_h and self.hit_box.y >= 0 >= self.tempo_atq_forte:
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.y += (vel * delta_time * (-1))

        if x == self.x and y == self.y and self.tempo_atq_forte <= 0:
            self.sprite.image = pygame.image.load(self.idle[self.direcao]).convert_alpha()

    def attack_action(self, delta_time, p_x, p_y, p_w, p_h):
        teclado = Keyboard()
        self.cooldown_forte -= delta_time
        if teclado.key_pressed("q") and not self.atacou_forte:
            self.hit_attack.y = self.hit_box.y - (self.hit_attack.height - self.hit_box.height)/2
            if self.direcao == 0:
                self.hit_attack.x = self.hit_box.x + self.hit_attack.width/2
            else:
                self.hit_attack.x = self.hit_box.x - (self.hit_attack.width - self.hit_box.width) - self.hit_attack.width/2
            self.sprite.image = pygame.image.load(self.attack[self.direcao]).convert_alpha()
            self.atacou_forte = True
            self.cooldown_forte = 1
            self.tempo_atq_forte = 50 / 6

        self.tempo_atq_forte -= (100 / 6) * delta_time

        if self.cooldown_forte <= 0:
            self.atacou_forte = False

    def play_n_drawn(self, delta_time):

        if self.tempo_animacao <= 0:
            self.sprite.stop()
            self.tempo_animacao = 50 / 6
        self.tempo_animacao -= delta_time * (100 / 6)

        self.sprite.set_position(self.x, self.y)

        self.hit_box.x = self.x + 72
        self.hit_box.y = self.y + 80

        self.took_damage -= delta_time

        self.sprite.play()
        self.sprite.update()

        if (self.took_damage < 0.25 or (self.took_damage > 0.5 and self.took_damage <= 0.75)
                or (self.took_damage > 1 and self.took_damage <= 1.25) or (self.took_damage > 1.75)):
            self.sprite.draw()


        if True:
            if self.tempo_atq_forte > 0:
                self.hit_attack.draw()
            self.hit_box.draw()



    def dead(self, delta_time):
        morte_1 = Sprite("../GameAssets Goblin-Slayer/Dead Animation/Dead_1.png", 7)
        morte_2 = Sprite("../GameAssets Goblin-Slayer/Dead Animation/Dead_2.png", 7)

        self.sprite = morte_1
        self.sprite.set_sequence_time(0, 896, 100, True)
        self.sprite.set_position(self.x, self.y + 100)
        '''
        if self.tempo_animacao_morte <= 0:
            self.sprite.stop()
            self.tempo_animacao_morte = 50 / 7
        self.tempo_animacao_morte -= delta_time * (100 / 7)
        '''

        self.sprite.play()
        self.sprite.update()
        self.sprite.draw()



