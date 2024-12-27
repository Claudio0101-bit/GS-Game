from PPlay.window import *
from PPlay.keyboard import *
from PPlay.mouse import *
from PPlay.gameimage import *
from PPlay.sprite import *
from PPlay.animation import *



# Definição da Função JOGO
def jogo(janela):

    #agua = GameImage("Tiny Swords (Update 010)/Terrain/Water/Water.png")

    cena = GameImage("Assets Resized/map.png")

    # Definição de Variáveis de Controle
    teclado = Window.get_keyboard()         #Teclado
    mouse = Window.get_mouse()              #Mouse
    voltar = False                          #Voltar à Tela inicial
    vel = 300                               #Velocidade dos personagens

    idle = ("Warrior_Blue_FILAS/Warrior_Blue_Parado_Right_1x1.png",
            "Warrior_Blue_FILAS/Warrior_Blue_Parado_Left_1x1.png")

    walking = ("Warrior_Blue_FILAS/Warrior_Blue_Correndo_2x1.png",
               "Warrior_Blue_FILAS/Warrior_Blue_Left_Correndo_2x1.png")

    atack = (("Warrior_Blue_FILAS/Warrior_Blue_Atk-1-RIGHT_3x1.png", "Warrior_Blue_FILAS/Warrior_Blue_Atk-1-LEFT_3x1.png"),
             ("Warrior_Blue_FILAS/Warrior_Blue_Atk-2-RIGHT_4x1.png", "Warrior_Blue_FILAS/Warrior_Blue_Atk-2-LEFT_4x1.png"))

    # Variáveis com "_g" referentes ao Goblin
    idle_g = ("Torch_Red_Goblin_FILAS/Torch_Red_Parado_RIGHT_1x1.png",
            "Torch_Red_Goblin_FILAS/Torch_Red_Parado_LEFT_1x1.png")

    walking_g = ("Torch_Red_Goblin_FILAS/Torch_Red_Right_Correndo_2x1.png",
               "Torch_Red_Goblin_FILAS/Torch_Red_Left_Correndo_2x1.png")

    atack_g = ("Torch_Red_Goblin_FILAS/Torch_Red_Atk-RIGHT_3x1.png", "Torch_Red_Goblin_FILAS/Torch_Red_Atk-LEFT_3x1.png")

    #Sprite do Player/Warrior
    player = Sprite(idle[0], 6)
    player.set_sequence_time(0, 1152, 100, True)
    player.set_position(janela.width/2 - 200, janela.height/2 - 200)

    #Sprite do Inimigo/Goblin com tocha
    goblin = Sprite(idle[0], 7)
    goblin.set_sequence_time(0, 1344, 100, True)
    goblin.set_position(1000, 600)

    tempo_animacao = 50/6
    tempo_animacao_g = 50/7
    tempo_ataque = 50 / 6
    direcao = 0
    direcao_g = 0
    cooldown_forte = 0
    cooldown_fraco = 0
    atacou_forte = False
    atacou_fraco = False

    # GAME Loop do JOGO

    while True:
        cena.draw()
        # Condicional para Voltar à tela anterior
        if teclado.key_pressed("esc"):
            voltar = True
        if voltar == True:
            voltar = False
            break;

        '''for i in range(0, janela.width, agua.width):
            for j in range(0, janela.height, agua.height):
                agua.x = i
                agua.y = j
                agua.draw()'''

        if teclado.key_pressed("d") and player.x < janela.width - player.width:
            direcao = 0
            player.image = pygame.image.load(walking[direcao]).convert_alpha()
            player.move_x(vel * janela.delta_time())

        if teclado.key_pressed("a") and player.x >= 0:
            direcao = 1
            player.image = pygame.image.load(walking[direcao]).convert_alpha()
            player.move_x(vel * janela.delta_time() * (-1))

        if teclado.key_pressed("s") and player.y <= janela.height - player.height:
            player.image = pygame.image.load(walking[direcao]).convert_alpha()
            player.move_y(vel * janela.delta_time())

        if teclado.key_pressed("w") and player.y >= 0:
            player.image = pygame.image.load(walking[direcao]).convert_alpha()
            player.move_y(vel * janela.delta_time() * (-1))

        cooldown_forte -= janela.delta_time()
        cooldown_fraco -= janela.delta_time()

        if teclado.key_pressed("e"):
            atacou_forte = True
        if atacou_forte and cooldown_forte <= 0:
            player.image = pygame.image.load(atack[0][direcao]).convert_alpha()
            cooldown_forte = 1.5
            atacou_forte = False

        if teclado.key_pressed("q"):
            atacou_fraco = True
        if atacou_fraco and cooldown_fraco <= 0:
            player.image = pygame.image.load(atack[1][direcao]).convert_alpha()
            cooldown_fraco = 0.5
            atacou_fraco = False
        '''if teclado.key_pressed("q") and cooldown_forte <= 0:
            while tempo_ataque > 0:
                player.image = pygame.image.load(atack[0][direcao]).convert_alpha()
                tempo_ataque -= (100 / 6) * janela.delta_time()
            tempo_ataque = 50/6
            cooldown_forte = 1.5

        if teclado.key_pressed("e") and cooldown_fraco <= 0:

            while tempo_ataque > 0:
                player.image = pygame.image.load(atack[1][direcao]).convert_alpha()
                tempo_ataque -= (100 / 6) * janela.delta_time()
            tempo_ataque = 50 / 6
            cooldown_fraco = 0.5'''

        if (not teclado.key_pressed("w") and not teclado.key_pressed("a") and not teclado.key_pressed("s") and
                                            not teclado.key_pressed("d") and not teclado.key_pressed("q")
                                            and not teclado.key_pressed("e")):
            player.image = pygame.image.load(idle[direcao]).convert_alpha()


        # Movimentação do Goblin, ainda sem atacar
        if teclado.key_pressed("right") and goblin.x < janela.width - goblin.width:
            direcao_g = 0
            goblin.image = pygame.image.load(walking_g[direcao_g]).convert_alpha()
            goblin.move_x(vel * janela.delta_time())

        if teclado.key_pressed("left") and goblin.x >= 0:
            direcao_g = 1
            goblin.image = pygame.image.load(walking_g[direcao_g]).convert_alpha()
            goblin.move_x(vel * janela.delta_time() * (-1))

        if teclado.key_pressed("down") and goblin.y <= janela.height - goblin.height:
            goblin.image = pygame.image.load(walking_g[direcao_g]).convert_alpha()
            goblin.move_y(vel * janela.delta_time())

        if teclado.key_pressed("up") and goblin.y >= 0:
            goblin.image = pygame.image.load(walking_g[direcao_g]).convert_alpha()
            goblin.move_y(vel * janela.delta_time() * (-1))

        if (not teclado.key_pressed("up") and not teclado.key_pressed("right") and not teclado.key_pressed("down") and
                                            not teclado.key_pressed("left")):
            goblin.image = pygame.image.load(idle_g[direcao_g]).convert_alpha()

        if tempo_animacao <= 0:
            player.stop()
            goblin.stop()
            tempo_animacao = 50/6
            tempo_animacao_g = 50/7

        tempo_animacao -= (100/6) * janela.delta_time()
        tempo_animacao_g -= (100/7) * janela.delta_time()

        player.play()
        goblin.play()

        player.update()
        goblin.update()

        player.draw()
        goblin.draw()

        janela.update()
