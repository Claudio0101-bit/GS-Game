from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from player import Player
from goblin import Goblin



# Definição da Função JOGO
def jogo(janela):


    agua = GameImage("Assets Resized/mapa-agua.png")
    terra = GameImage("Assets Resized/mapa-terra.png")

    terra.x = 64 * 2
    terra.y = 64 * 1

    # Definição de Variáveis de Controle
    teclado = Window.get_keyboard()         #Teclado
    mouse = Window.get_mouse()              #Mouse
    voltar = False                          #Voltar à Tela inicial
    vel = 300                               #Velocidade dos personagens

    idle = ("Warrior_Blue_FILAS/Warrior_Blue_Parado_1x1.png",
            "Warrior_Blue_FILAS/Warrior_Blue_Parado_Left_1x1.png")

    walking = ("Warrior_Blue_FILAS/Warrior_Blue_Correndo_2x1.png",
               "Warrior_Blue_FILAS/Warrior_Blue_Left_Correndo_2x1.png")

    atack = (("Warrior_Blue_FILAS/Warrior_Blue_Atk-1-RIGHT_3x1.png", "Warrior_Blue_FILAS/Warrior_Blue_Atk-1-LEFT_3x1.png"),
             ("Warrior_Blue_FILAS/Warrior_Blue_Atk-2-RIGHT_4x1.png", "Warrior_Blue_FILAS/Warrior_Blue_Atk-2-LEFT_4x1.png"))

    # Variáveis com "_g" referentes ao Goblin
    idle_g = ("Goblin_Red_FILAS/Parado_Right.png", "Goblin_Red_FILAS/Parado_Left.png")

    walking_g = ("Goblin_Red_FILAS/Andando_Right.png", "Goblin_Red_FILAS/Andando_Left.png")

    atack_g = ("Goblin_Red_FILAS/Atacando_Right.png", "Goblin_Red_FILAS/Atacando_Left.PNG")

    vida_tuple = ("GameAssets Goblin-Slayer/Barras-Buttons-Etc/rhombusMeters 64x16/redMeter1.png",
                  "GameAssets Goblin-Slayer/Barras-Buttons-Etc/rhombusMeters 64x16/redMeter2.png",
                  "GameAssets Goblin-Slayer/Barras-Buttons-Etc/rhombusMeters 64x16/redMeter3.png",
                  "GameAssets Goblin-Slayer/Barras-Buttons-Etc/rhombusMeters 64x16/redMeter4.png",
                  "GameAssets Goblin-Slayer/Barras-Buttons-Etc/rhombusMeters 64x16/redMeter5.png")
    barra_vida = Sprite(vida_tuple[4])
    barra_vida.x = 100
    barra_vida.y = 100

    #Sprite do Player/Warrior e do Goblin
    player = Player(idle, walking, atack, janela.width, janela.height)
    goblin = Goblin(idle_g, walking_g, atack_g, janela.width, janela.height)


    # GAME Loop do JOGO
    while True:
        agua.draw()
        terra.draw()
        barra_vida.draw()

        player.run(janela.width, janela.height, vel, janela.delta_time())
        player.attack_action(janela.delta_time())
        player.play_n_drawn(janela.delta_time())
        goblin.run(janela.width, janela.height, vel, janela.delta_time())
        goblin.attack_action(janela.delta_time())
        goblin.play_n_drawn(janela.delta_time())
        janela.update()
