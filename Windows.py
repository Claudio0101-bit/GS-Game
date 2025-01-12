from PPlay.window import *
from jogo import *


def objetivo(janela, mouse):

    # Elementos estéticos da Tela de Objetivos
    cartaz_objetivo = Sprite("Assets Resized/Ribbon_Blue_Mod.600x90.png", 1)
    x = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_01.png")
    bordas = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png")
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Vertical_Mod.1000x650.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.350x280.png", 1)

    # Seta para Voltar
    seta = Sprite("Assets Resized/Red_Arrow_96x96.png")
    seta.set_position(30, 30)

    seta_hover = Sprite("Assets Resized/Yellow_Arrow_96x96.png")

#---------------------- Atribuição de Coordenadas aos Elementos da Tela de Objetivos ---------------------------
    cartaz_objetivo.x = janela.width / 2 - cartaz_objetivo.width / 2
    cartaz_objetivo.y = 100

    banner_buttons.x = janela.width / 2 - banner_buttons.width / 2
    banner_buttons.y = 100

    tela_buttons.x = janela.width / 2 - tela_buttons.width / 2
    tela_buttons.y = banner_buttons.y + 160

    x.x = tela_buttons.x + 10
    x.y = tela_buttons.y + tela_buttons.height - bordas.height - 5

    bordas.x = tela_buttons.x + 10 - 1
    bordas.y = tela_buttons.y + tela_buttons.height - 5 - bordas.height

    while True:

        # Desenhando Elementos da Tela de Objetivos
        cenario_menu.draw()
        cartaz_objetivo.draw()
        banner_buttons.draw()
        tela_buttons.draw()
        bordas.draw()
        x.draw()
        seta.draw()


#------------------------------ Escrevendo Textos na Tela de Objetivos -------------------------
        # Título do Cartaz
        janela.draw_text("Objetivos", (janela.width / 2) - (192 / 2) + 5, 110, size=36,
                         color="white", font_name="Times New Roman", bold=True, italic=False)

        # 1° Objetivo - Defender o reino
        janela.draw_text("- Defenda o reino.", janela.width / 2 - 150, janela.height / 2 - 100, 28,
                         color="black", font_name="Times New Roman", bold=True, italic=False)

        # 2° Objetivo - Não ser derrotado
        janela.draw_text("- Não seja derrotado.", janela.width / 2 - 150, janela.height / 2 - 50, 28,
                         color="black", font_name="Times New Roman", bold=True, italic=False)

#--------------------- Interação com o Botão de Fechar Objetivos e Iniciar Jogo ---------------------
        if mouse.is_over_area([bordas.x, bordas.y], [bordas.x + bordas.width, bordas.y + bordas.height]):

            if mouse.is_button_pressed(1):
                jogo(janela)

        # Interação com a Seta de Voltar
        if mouse.is_over_object(seta):
            seta_hover.set_position(seta.x, seta.y)
            seta_hover.draw()

            if mouse.is_button_pressed(1):
                from menu import menu
                menu(janela, mouse)

        # Escondendo Cursor do Mouse padrão
        mouse.hide()

        # Atribuição de Novo Mouse dentro da Janela
        if mouse.is_over_area([0, 0], [janela.width, janela.height]):
            cords_mouse = mouse.get_position()
            a = Sprite("Tiny Swords (Update 010)/UI/Pointers/01.png", 1)
            a.set_position(cords_mouse[0] - 30, cords_mouse[1] - 25)
            a.draw()

        janela.update()


def configurar(janela, mouse):
    # Detecção do Mouse


#--------------- Cartazes e Banners estéticos da Tela de Configurações ------------------------
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    cartaz_config = Sprite("Assets Resized/Ribbon_Yellow_Mod.600x90.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Horizontal_Mod.1600x900.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.630x400.png", 1)


#------------------------- Botões/Elementos da Tela de Configurações ----------------------------
    # Sprite de Botão com Cursor em cima
    botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover.png")

    # Música e Efeitos Sonoros
    botao_musica = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)
    botao_efeitos = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)

    botao_musica_on_1 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)
    botao_musica_on_2 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)

    botao_musica_off_1 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)
    botao_musica_off_2 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)

    icone_musica = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_03.png")
    icone_efeitos = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_03.png")

    icone_musica_on_1 = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_03.png")
    icone_musica_on_2 = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_03.png")

    icone_musica_off_1 = Sprite("Tiny Swords (Update 010)/UI/Icons/Pressed_03.png")
    icone_musica_off_2 = Sprite("Tiny Swords (Update 010)/UI/Icons/Pressed_03.png")

    # Dificuldade
    botao_diff = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover.png", 1)
    lista_num_diff = ["Tiny Swords (Update 010)/UI/Icons/Regular_04.png",
                      "Tiny Swords (Update 010)/UI/Icons/Regular_05.png",
                      "Tiny Swords (Update 010)/UI/Icons/Regular_06.png"]

    botao_mais = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)
    botao_menos = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)
    botao_disable = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Disable.png")
    mais = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_08.png")
    menos = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_09.png")
    nivel = 0

    # Seta para Voltar
    seta = Sprite("Assets Resized/Red_Arrow_96x96.png")
    seta.set_position(30, 30)

    seta_hover = Sprite("Assets Resized/Yellow_Arrow_96x96.png")

#--------------------- Atribuição das coordenadas de cada Elemento ---------------------------
    # Cartazes e Banners estéticos da Tela de Configurações
    cartaz_config.x = janela.width / 2 - cartaz_config.width / 2
    cartaz_config.y = 50

    banner_buttons.x = janela.width / 2 - banner_buttons.width / 2
    banner_buttons.y = -20

    tela_buttons.x = janela.width / 2 - tela_buttons.width / 2
    tela_buttons.y = banner_buttons.y + 250

    # Música e Efeitos Sonoros
    botao_musica.x = tela_buttons.x + 135
    botao_musica.y = tela_buttons.y + 20

    botao_efeitos.x = botao_musica.x
    botao_efeitos.y = botao_musica.y + 90

    icone_musica.set_position(botao_musica.x, botao_musica.y)
    icone_efeitos.set_position(botao_efeitos.x, botao_efeitos.y)

    # Dificuldade
    botao_diff.x = tela_buttons.x + 450
    botao_diff.y = tela_buttons.y + 100

    botao_mais.x = botao_diff.x + botao_diff.width/2 + 5
    botao_mais.y = botao_diff.y + botao_diff.height + 10

    botao_menos.x = botao_diff.x - botao_diff.width/2 - 5
    botao_menos.y = botao_diff.y + botao_diff.height + 10

    mais.set_position(botao_mais.x, botao_mais.y)
    menos.set_position(botao_menos.x, botao_menos.y)

    num_diff = Sprite(lista_num_diff[nivel])
    num_diff.set_position(botao_diff.x, botao_diff.y)



    # Intervalo de Tempo entre Clicks em Botões
    delay_de_click = 0

    while True:

        # Desenhando Elementos na Tela de Configurações
        cenario_menu.draw()
        cartaz_config.draw()
        banner_buttons.draw()
        tela_buttons.draw()
        botao_musica.draw()
        icone_musica.draw()
        botao_efeitos.draw()
        icone_efeitos.draw()
        botao_diff.draw()
        botao_mais.draw()
        botao_menos.draw()
        mais.draw()
        menos.draw()
        num_diff.draw()
        seta.draw()

#----------------------- Escrevendo Textos na Tela de Configurações ------------------------------
        # Título
        janela.draw_text("Configurações", (janela.width / 2) - (192 / 2) - 20, 60, size=36,
                         color="white", font_name="Times New Roman", bold=True, italic=False)
        # Música
        janela.draw_text("Música:", tela_buttons.x + 30, tela_buttons.y + 35, 28, color="black",
                         font_name="Times New Roman", bold=True, italic=False)
        # Efeitos
        janela.draw_text("Efeitos:", tela_buttons.x + 30, tela_buttons.y + 115, 28,
                        color="black", font_name="Times New Roman", bold=True, italic=False)

        # Controles
        janela.draw_text("Controles (Imutáveis):", tela_buttons.x + 30, tela_buttons.y + 200, 28,
                         color="black", font_name="Times New Roman", bold=True, italic=False)

        janela.draw_text("- 'W,A,S,D' para se mover.", tela_buttons.x + 30, tela_buttons.y + 250, 28,
                         color="black", font_name="Arial", bold=False, italic=True)

        janela.draw_text("- 'E' para atacar.", tela_buttons.x + 30, tela_buttons.y + 300, 28,
                         color="black", font_name="Arial", bold=False, italic=True)

        janela.draw_text("- 'ESC' para interromper jogo.", tela_buttons.x + 30, tela_buttons.y + 350, 28,
                         color="black", font_name="Arial", bold=False, italic=True)

        # Dificuldade
        janela.draw_text("Dificuldade:", tela_buttons.x + 400, tela_buttons.y + 35, 28, color="black",
                         font_name="Times New Roman", bold=True, italic=False)

        janela.draw_text("- 1: Fácil", tela_buttons.x + 425, tela_buttons.y + 250, 28,
                         color="black", font_name="Arial", bold=False, italic=True)

        janela.draw_text("- 2: Médio", tela_buttons.x + 425, tela_buttons.y + 290, 28,
                         color="black", font_name="Arial", bold=False, italic=True)

        janela.draw_text("- 3: Difícil", tela_buttons.x + 425, tela_buttons.y + 330, 28,
                         color="black", font_name="Arial", bold=False, italic=True)

# --------------------------------- Interações com os Botões da Tela de Configurações ----------------------------
        # Interação com o Botão de Música
        if mouse.is_over_object(botao_musica):
            botao_hover.set_position(botao_musica.x, botao_musica.y)
            botao_hover.draw()
            icone_musica.draw()

            if mouse.is_button_pressed(1):
                if botao_musica == botao_musica_on_1 and delay_de_click <= 0:
                    x,y = botao_musica.x, botao_musica.y
                    botao_musica = botao_musica_off_1
                    botao_musica.set_position(x, y)

                    icone_musica = icone_musica_off_1
                    icone_musica.set_position(x, y)

                    delay_de_click = 0.2

                else:
                    if delay_de_click <= 0:
                        x,y = botao_musica.x, botao_musica.y
                        botao_musica = botao_musica_on_1
                        botao_musica.set_position(x, y)

                        icone_musica = icone_musica_on_1
                        icone_musica.set_position(x, y)

                        delay_de_click = 0.2

        # Interação com o Botão de Efeitos
        if mouse.is_over_object(botao_efeitos):
            botao_hover.set_position(botao_efeitos.x, botao_efeitos.y)
            botao_hover.draw()
            icone_efeitos.draw()

            if mouse.is_button_pressed(1):
                if botao_efeitos == botao_musica_on_2 and delay_de_click <= 0:
                    x,y = botao_efeitos.x, botao_efeitos.y
                    botao_efeitos = botao_musica_off_2
                    botao_efeitos.set_position(x, y)

                    icone_efeitos = icone_musica_off_2
                    icone_efeitos.set_position(x, y)

                    delay_de_click = 0.2

                else:
                    if delay_de_click <= 0:
                        x,y = botao_efeitos.x, botao_efeitos.y
                        botao_efeitos = botao_musica_on_2
                        botao_efeitos.set_position(x, y)

                        icone_efeitos = icone_musica_on_2
                        icone_efeitos.set_position(x, y)

                        delay_de_click = 0.2

        delay_de_click -= janela.delta_time()

        # Interação com os Botões de Dificuldade
        if (mouse.is_over_object(botao_mais) and mouse.is_button_pressed(1)
                and nivel <= 1 and delay_de_click <= 0):
            nivel += 1
            num_diff = Sprite(lista_num_diff[nivel])
            num_diff.set_position(botao_diff.x, botao_diff.y)
            delay_de_click = 0.2

        if nivel == 2:
            botao_disable.set_position(botao_mais.x, botao_mais.y - 3)
            botao_disable.draw()
            mais.draw()

        if (mouse.is_over_object(botao_menos) and mouse.is_button_pressed(1)
                and nivel >= 1 and delay_de_click <= 0):
            nivel -= 1
            num_diff = Sprite(lista_num_diff[nivel])
            num_diff.set_position(botao_diff.x, botao_diff.y)
            delay_de_click = 0.2

        if nivel == 0:
            botao_disable.set_position(botao_menos.x, botao_menos.y - 3)
            botao_disable.draw()
            menos.draw()

        # Interação com a Seta de Voltar
        if mouse.is_over_object(seta):
            seta_hover.set_position(seta.x, seta.y)
            seta_hover.draw()

            if mouse.is_button_pressed(1):
                from menu import menu
                menu(janela, mouse)

        # Escondendo Cursor do Mouse padrão
        mouse.hide()

        # Atribuição de Novo Mouse dentro da Janela
        if mouse.is_over_area([0, 0], [janela.width, janela.height]):
            cords_mouse = mouse.get_position()
            a = Sprite("Tiny Swords (Update 010)/UI/Pointers/01.png", 1)
            a.set_position(cords_mouse[0] - 30, cords_mouse[1] - 25)
            a.draw()

        janela.update()

def game_over(janela, mouse):

    # Elementos estéticos da Tela de Game Over
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    cartaz_game_over = Sprite("Assets Resized/Ribbon_Red_Mod.600x90.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Vertical_Mod.1000x650.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.350x280.png", 1)

    # Botões da Tela de Game Over
    botao_jogar = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png", 1)
    botao_menu = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides.png",1)

    # Botão selecionado
    botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover_3Slides.png",1)

#------------------ Atribuição de coordenadas aos Elementos do Game Over -----------------------------
    cartaz_game_over.x = janela.width/2 - cartaz_game_over.width/2
    cartaz_game_over.y = 100

    banner_buttons.x = janela.width/2 - banner_buttons.width/2
    banner_buttons.y = 100

    tela_buttons.x = janela.width/2 - tela_buttons.width/2
    tela_buttons.y = banner_buttons.y + 160

    botao_jogar.x = janela.width/2 - botao_jogar.width/2
    botao_jogar.y = tela_buttons.y + 150

    botao_menu.x = janela.width / 2 - botao_menu.width / 2
    botao_menu.y = tela_buttons.y + 210

    while True:
        cenario_menu.draw()
        cartaz_game_over.draw()
        banner_buttons.draw()
        tela_buttons.draw()
        botao_jogar.draw()
        botao_menu.draw()

# ----------------------- Interações com os Botões da Tela de Game Over ----------------------------
        # Tentar de novo
        if mouse.is_over_object(botao_jogar):
            botao_hover.set_position(botao_jogar.x, botao_jogar.y)
            botao_hover.draw()
            if mouse.is_button_pressed(1):
                jogo(janela)

        # Menu
        if mouse.is_over_object(botao_menu):
            botao_hover.set_position(botao_menu.x, botao_menu.y)
            botao_hover.draw()
            if mouse.is_button_pressed(1):
                from menu import menu
                menu(janela, mouse)


# ----------------------- Escrevendo Textos na Tela de Configurações ------------------------------
        # Título
        janela.draw_text("Game Over", janela.width / 2 - botao_jogar.width / 2, 110, size=36,
                         color="white", font_name="Times New Roman", bold=True, italic=False)

        # Jogar de novo
        janela.draw_text("Tentar de novo", botao_jogar.x + botao_jogar.width / 2 - 70, botao_jogar.y + 10, size=24,
                         color="black", font_name="Arial", bold=True, italic=False)

        # Voltar ao Menu
        janela.draw_text("Menu", botao_menu.x + botao_menu.width / 2 - 30, botao_menu.y + 10, size=24,
                         color="black", font_name="Arial", bold=True, italic=False)


        # Escondendo Cursor do Mouse padrão
        mouse.hide()

        # Atribuição de Novo Mouse dentro da Janela
        if mouse.is_over_area([0, 0], [janela.width, janela.height]):
            cords_mouse = mouse.get_position()
            a = Sprite("Tiny Swords (Update 010)/UI/Pointers/01.png", 1)
            a.set_position(cords_mouse[0] - 30, cords_mouse[1] - 25)
            a.draw()

        janela.update()
