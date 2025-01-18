from PPlay.window import *
from PPlay.gameimage import *
from PPlay.animation import *
from GameObjects.player import Player
from GameObjects.builds import Build
from PPlay.collision import Collision
from colisao import colision
from GameWindows.functions import *


# Definição da Função JOGO
def jogo(janela, mouse):
    # Mapa
    cena = GameImage("Assets Resized/MapaQ-Completo.png")

    # Pontos Limites da Terra/Colisão com a água
    ponto1_terra = [192, 128]
    ponto2_terra = [3520, 1984]

    # Definição de Variáveis de Controle
    teclado = Window.get_keyboard()  #Teclado
    voltar = False  #Voltar à Tela inicial
    vel = 300  #Velocidade dos personagens

    # Variáveis de Dificuldade
    onda = 1
    configs = pega_config()

    vida_tuple = ("Assets Resized/Vida1.png", "Assets Resized/Vida2.png", "Assets Resized/Vida3.png",
                  "Assets Resized/Vida4.png", "Assets Resized/Vida5.png")

    barra_vida = Sprite(vida_tuple[4])
    barra_vida.x = 30
    barra_vida.y = 30

    base_vida = Sprite("Assets Resized/Base-vida.png")
    base_vida.set_position(25, 25)

    colisor = Collision()

    #Sprite do Player/Warrior e Lista de Goblins
    player = Player(janela.width, janela.height, vel)
    lista_goblins = preenche_lista_goblins(configs[0], onda, janela.width, janela.height, vel)

    # -------------------- Construções -----------------------
    cabana_goblin = GameImage("Tiny Swords (Update 010)/Factions/Goblins/Buildings/Wood_House/Goblin_House.png")
    casa_h = GameImage("Tiny Swords (Update 010)/Factions/Knights/Buildings/House/House_Blue.png")
    torre = GameImage("Tiny Swords (Update 010)/Factions/Knights/Buildings/Tower/Tower_Blue.png")
    castelo_h = GameImage("Tiny Swords (Update 010)/Factions/Knights/Buildings/Castle/Castle_Blue.png")

    cabana_1 = Build(cabana_goblin, 7 * 64, 19 * 64)
    cabana_3 = Build(cabana_goblin, 7 * 64, 23 * 64)
    cabana_4 = Build(cabana_goblin, 12 * 64, 23 * 64)
    torre_1 = Build(torre, 36 * 64, 4 * 64)
    torre_2 = Build(torre, 47 * 64, 4 * 64)
    castelo = Build(castelo_h, 40 * 64, 3 * 64)
    casa_1 = Build(casa_h, 39 * 64, 7 * 64)
    casa_2 = Build(casa_h, 39 * 64, 11 * 64)
    casa_3 = Build(casa_h, 46 * 64, 7 * 64)
    casa_4 = Build(casa_h, 46 * 64, 11 * 64)

    torre_2.alta = True
    torre_1.alta = True
    castelo.larga = True
    castelo.alta = True

    castelo.hit_box = GameImage("Assets Resized/hit_castelo.png")
    torre_2.hit_box = GameImage("Assets Resized/hit_torre.png")
    torre_1.hit_box = GameImage("Assets Resized/hit_torre.png")

    lista_builds = [cabana_1, cabana_3, cabana_4, castelo, torre_2, torre_1,
                    casa_1, casa_2, casa_3, casa_4]

    # Estatísticas de Goblins Derrotados para Tela de Game Over
    num_mortos = 0



    # GAME Loop do JOGO
    while True:
        cena.draw()
        # Cronômetro
        import time
        tempo_inicial = time.time()
        tempo_final = 0

        # Função de Movimento do Player
        player.run(janela.width, janela.height, vel, janela.delta_time())

#-------------------------------- Colisão com a água ------------------------------
        if player.hit_box.x < ponto1_terra[0]:
            player.x += vel * janela.delta_time()

        if player.hit_box.x + player.hit_box.width > ponto2_terra[0]:
            player.x -= vel * janela.delta_time()

        if player.hit_box.y < ponto1_terra[1]:
            player.y += vel * janela.delta_time()

        if player.hit_box.y + player.hit_box.height > ponto2_terra[1]:
            player.y -= vel * janela.delta_time()
#---------------------------------------------------------------------------


#-------------- Câmera do Mapa e atualização da posição de GameObjects -------------
        if player.hit_box.x - 256 < 0:
            # Atualização da posição de GameObjects
            player.x += vel * janela.delta_time()
            for goblin in lista_goblins:
                goblin.x += vel * janela.delta_time()
            for b in lista_builds:
                b.x += vel * janela.delta_time()
            # Movimento do mapa
            cena.x += vel * janela.delta_time()
            ponto1_terra[0] += vel * janela.delta_time()
            ponto2_terra[0] += vel * janela.delta_time()

        if player.hit_box.x + player.hit_box.width + 256 > janela.width:
            # Atualização da posição de GameObjects
            player.x -= vel * janela.delta_time()
            for goblin in lista_goblins:
                goblin.x -= vel * janela.delta_time()
            for b in lista_builds:
                b.x -= vel * janela.delta_time()
            # Movimento do mapa
            cena.x -= vel * janela.delta_time()
            ponto1_terra[0] -= vel * janela.delta_time()
            ponto2_terra[0] -= vel * janela.delta_time()

        if player.hit_box.y - 256 < 0:
            # Atualização da posição de GameObjects
            player.y += vel * janela.delta_time()
            for goblin in lista_goblins:
                goblin.y += vel * janela.delta_time()
            for b in lista_builds:
                b.y += vel * janela.delta_time()
            # Movimento do mapa
            cena.y += vel * janela.delta_time()
            ponto1_terra[1] += vel * janela.delta_time()
            ponto2_terra[1] += vel * janela.delta_time()

        if player.hit_box.y + player.hit_box.height + 256 > janela.height:
            # Atualização da posição de GameObjects
            player.y -= vel * janela.delta_time()
            for goblin in lista_goblins:
                goblin.y -= vel * janela.delta_time()
            for b in lista_builds:
                b.y -= vel * janela.delta_time()
            # Movimento do mapa
            cena.y -= vel * janela.delta_time()
            ponto1_terra[1] -= vel * janela.delta_time()
            ponto2_terra[1] -= vel * janela.delta_time()

        # Função de Ataque do Player
        player.attack_action(janela.delta_time())

        # Função de Movimento de todos os Goblins
        for goblin in lista_goblins:
            goblin.run(janela.width, janela.height, janela.delta_time(), player.hit_box.x, player.hit_box.y,
                       player.hit_box.width, player.hit_box.height)

            # Dano do Player aos Goblins
            if player.tempo_atq_forte > 0 and colisor.collided(player.hit_attack, goblin.hit_box) and goblin.took_damage <= 0:
                goblin.vida -= player.dano
                if player.direcao == 0:
                    goblin.x += 128                  # Repulsão após ataque
                else:
                    goblin.x -= 128                  # Repulsão após ataque
                goblin.took_damage = 2

            # Dano dos Goblins ao Player
            if goblin.tempo_atq_forte > 0 and colisor.collided(player.hit_box, goblin.hit_attack) and player.took_damage <= 0:
                player.vida -= goblin.dano
                player.took_damage = 2

            # Colisão dos Goblins com a água
            if goblin.hit_box.x < ponto1_terra[0]:
                goblin.x += vel * janela.delta_time() * 0.75

            if goblin.hit_box.x + goblin.hit_box.width > ponto2_terra[0]:
                goblin.x -= vel * janela.delta_time() * 0.75

            if goblin.hit_box.y < ponto1_terra[1]:
                goblin.y += vel * janela.delta_time() * 0.75

            if goblin.hit_box.y + goblin.hit_box.height > ponto2_terra[1]:
                goblin.y -= vel * janela.delta_time() * 0.75

            janela.draw_text(str(goblin.vida), janela.width / 2 - 150, goblin.y,
                             color="black", font_name="Times New Roman", bold=True, italic=False)

            # Função de Ataque dos Goblins
            goblin.attack_action(janela.delta_time(), player.hit_box.x, player.hit_box.y,
                       player.hit_box.width, player.hit_box.height)

            # Morte dos Goblins/ Retirado da Lista
            if goblin.vida <= 0:
                num_mortos += 1
                goblin.dead(janela.delta_time())
                lista_goblins.remove(goblin)


        # Fim de uma Horda / Melhoria (com pausa no tempo)/ Geração de Nova Horda de Goblins
        if len(lista_goblins) == 0:
            tempo_final += tempo_inicial
            tempo_inicial = 0
            melhoria(janela, mouse, player)
            onda += 1
            lista_goblins = preenche_lista_goblins(configs[0], onda, janela.width, janela.height, vel)

        # Lista Completa de Game objects e colisão entre eles
        objetos = lista_goblins.copy()
        objetos += lista_builds
        colision(objetos, janela.delta_time())
        colisao_player_buid = lista_builds.copy()
        colisao_player_buid.append(player)
        colision(colisao_player_buid, janela.delta_time())
        objetos.append(player)
        objetos.sort(key=chave_y)

        for o in objetos:
            o.play_n_drawn(janela.delta_time())

        janela.draw_text(str(player.vida), janela.width / 2 - 150, janela.height / 2 - 50, 28,
                         color="black", font_name="Times New Roman", bold=True, italic=False)

        base_vida.draw()
        # Desenho da vida do Player e Morte do Player
        if player.vida >= 1:
            barra_vida.image = pygame.image.load(vida_tuple[player.vida - 1])
        else:
            game_over(janela, mouse, num_mortos, tempo_final)
        barra_vida.draw()

        # Interromper Jogo com Esc
        if teclado.key_pressed("esc"):
            break

        janela.update()
