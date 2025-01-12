from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *
from player import Player
from goblin import Goblin
from PPlay.collision import Collision

# Definição da Função JOGO
def jogo(janela):

    # Mapa
    cena = GameImage("Assets Resized/MapaQ-Completo.png")

    # Pontos Limites da Terra/Colisão com a água
    ponto1_terra = [192, 128]
    ponto2_terra = [3520, 1984]

    # Definição de Variáveis de Controle
    teclado = Window.get_keyboard()         #Teclado
    mouse = Window.get_mouse()              #Mouse
    voltar = False                          #Voltar à Tela inicial
    vel = 300                               #Velocidade dos personagens



    # Variáveis com "_g" referentes ao Goblin
    idle_g = ("Goblin_Red_FILAS/Parado_Right.png", "Goblin_Red_FILAS/Parado_Left.png")

    walking_g = ("Goblin_Red_FILAS/Andando_Right.png", "Goblin_Red_FILAS/Andando_Left.png")

    atack_g = ("Goblin_Red_FILAS/Atacando_Right.png", "Goblin_Red_FILAS/Atacando_Left.PNG")

    vida_tuple = ("Assets Resized/Vida1.png", "Assets Resized/Vida2.png", "Assets Resized/Vida3.png",
                  "Assets Resized/Vida4.png", "Assets Resized/Vida5.png")

    barra_vida = Sprite(vida_tuple[4])
    barra_vida.x = 30
    barra_vida.y = 30

    colisao = Collision()

    #Sprite do Player/Warrior e do Goblin
    player = Player(janela.width, janela.height)
    goblin = Goblin(idle_g, walking_g, atack_g, janela.width, janela.height)


    # GAME Loop do JOGO
    while True:
        cena.draw()
        barra_vida.draw()
        player.run(janela.width, janela.height, vel, janela.delta_time())
        if player.sprite.x < ponto1_terra[0]:
            player.sprite.x += vel * janela.delta_time()

        if player.sprite.x + player.sprite.width > ponto2_terra[0]:
            player.sprite.x -= vel * janela.delta_time()

        if player.sprite.y < ponto1_terra[1]:
            player.sprite.y += vel * janela.delta_time()

        if player.sprite.y + player.sprite.height > ponto2_terra[1]:
            player.sprite.y -= vel * janela.delta_time()

        if player.sprite.x - 64 < 0:
            player.sprite.x += vel * janela.delta_time()
            cena.x += vel * janela.delta_time()
            ponto1_terra[0] += vel * janela.delta_time()
            ponto2_terra[0] += vel * janela.delta_time()
        if player.sprite.x + player.sprite.width + 64 > janela.width:
            player.sprite.x -= vel * janela.delta_time()
            cena.x -= vel * janela.delta_time()
            ponto1_terra[0] -= vel * janela.delta_time()
            ponto2_terra[0] -= vel * janela.delta_time()
        if player.sprite.y - 64 < 0:
            player.sprite.y += vel * janela.delta_time()
            cena.y += vel * janela.delta_time()
            ponto1_terra[1] += vel * janela.delta_time()
            ponto2_terra[1] += vel * janela.delta_time()
        if player.sprite.y + player.sprite.height + 64 > janela.height:
            player.sprite.y -= vel * janela.delta_time()
            cena.y -= vel * janela.delta_time()
            ponto1_terra[1] -= vel * janela.delta_time()
            ponto2_terra[1] -= vel * janela.delta_time()

        player.attack_action(janela.delta_time())

        goblin.run(janela.width, janela.height, vel, janela.delta_time())
        goblin.attack_action(janela.delta_time())
        if player.sprite.y < goblin.sprite.y:
            player.play_n_drawn(janela.delta_time())
            goblin.play_n_drawn(janela.delta_time())
        else:
            goblin.play_n_drawn(janela.delta_time())
            player.play_n_drawn(janela.delta_time())

        # Interromper Jogo com Esc
        if teclado.key_pressed("esc"):
            break

        janela.update()
