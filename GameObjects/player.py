from PPlay.sprite import Sprite
from PPlay.gameobject import GameObject
from PPlay.gameimage import GameImage
from PPlay.keyboard import Keyboard
import pygame


class Player:

    def __init__(self, w_width, w_height, vel):

        self.idle = ("Warrior_Blue_FILAS/Warrior_Blue_Parado_1x1.png",
                     "Warrior_Blue_FILAS/Warrior_Blue_Parado_Left_1x1.png")

        self.walking = ("Warrior_Blue_FILAS/Warrior_Blue_Correndo_2x1.png",
                        "Warrior_Blue_FILAS/Warrior_Blue_Left_Correndo_2x1.png")

        self.attack = (
        ("Warrior_Blue_FILAS/Warrior_Blue_Atk-1-RIGHT_3x1.png", "Warrior_Blue_FILAS/Warrior_Blue_Atk-1-LEFT_3x1.png"),
        ("Warrior_Blue_FILAS/Warrior_Blue_Atk-2-RIGHT_4x1.png", "Warrior_Blue_FILAS/Warrior_Blue_Atk-2-LEFT_4x1.png"))


        self.sprite = Sprite(self.idle[0], 6)
        self.sprite.set_sequence_time(0, 1152, 100, True)
        self.sprite.set_position(w_width / 2 - 200, w_height / 2 - 200)

        self.hit_box = GameImage("Assets Resized/hitbox.png")
        self.hit_attack = GameImage("Assets Resized/hit_explosao.png")

        self.x = w_width / 2 - 350
        self.y = w_height / 2 - 200

        self.hit_box.x = self.x + 72
        self.hit_box.y = self.y + 80

        self.movable = False
        self.playable = True

        self.tempo_animacao = 50/6
        self.tempo_atq_forte = 0

        self.vida = 5
        self.dano = 1
        self.took_damage = 0
        self.vel = vel

        self.direcao = 0

        self.atacou_forte = False
        self.cooldown_forte = 0
        self.cooldown_atq_forte = 2

    def run(self, w_width, w_height, vel, delta_time):
        teclado = Keyboard()
        x = self.x
        y = self.y
        if (teclado.key_pressed("d") and self.hit_box.x < w_width - self.hit_box.width and not teclado.key_pressed("a")
                and self.tempo_atq_forte <= 0):
            self.direcao = 0
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.x += (vel * delta_time)

        if (teclado.key_pressed("a") and self.hit_box.x >= 0 and not teclado.key_pressed("d")
                and self.tempo_atq_forte <= 0):
            self.direcao = 1
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.x += (vel * delta_time * (-1))

        if (teclado.key_pressed("s") and self.hit_box.y <= w_height - self.hit_box.height and not teclado.key_pressed("w")
                and self.tempo_atq_forte <= 0):
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.y += (vel * delta_time)

        if (teclado.key_pressed("w") and self.hit_box.y >= 0 and not teclado.key_pressed("s")
                and self.tempo_atq_forte <= 0):
            self.sprite.image = pygame.image.load(self.walking[self.direcao]).convert_alpha()
            self.y += (vel * delta_time * (-1))

        if x == self.x and y == self.y and self.tempo_atq_forte <= 0:
            self.sprite.image = pygame.image.load(self.idle[self.direcao]).convert_alpha()

    def attack_action(self, delta_time):
        teclado = Keyboard()
        self.cooldown_forte -= delta_time

        if teclado.key_pressed("e") and not self.atacou_forte:
            self.hit_attack.y = self.hit_box.y - (self.hit_attack.height - self.hit_box.height)/2
            if self.direcao == 0:
                self.hit_attack.x = self.hit_box.x + self.hit_attack.width/2
            else:
                self.hit_attack.x = self.hit_box.x - (self.hit_attack.width - self.hit_box.width) - self.hit_attack.width/2

            self.sprite.image = pygame.image.load(self.attack[0][self.direcao]).convert_alpha()
            self.atacou_forte = True
            self.cooldown_forte = self.cooldown_atq_forte
            self.tempo_atq_forte = 50/6

        self.tempo_atq_forte -= (100/6) * delta_time

        if self.cooldown_forte <= 0:
            self.atacou_forte = False

    def play_n_drawn(self, delta_time):

        if self.tempo_animacao <= 0:
            self.sprite.stop()
            self.tempo_animacao = 50/6
        self.tempo_animacao -= delta_time * (100/6)

        self.sprite.set_position(self.x, self.y)

        self.hit_box.x = self.x + 72
        self.hit_box.y = self.y + 80

        self.took_damage -= delta_time

        self.sprite.play()
        self.sprite.update()

        if (self.took_damage < 0.25 or (self.took_damage > 0.5 and self.took_damage <= 0.75)
                or (self.took_damage > 1 and self.took_damage <= 1.25) or (self.took_damage > 1.75)):
            self.sprite.draw()

        if not True:
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

