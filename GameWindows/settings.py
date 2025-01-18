from GameWindows.functions import *


def configurar(janela, mouse):
    # Detecção do Mouse


#--------------- Cartazes e Banners estéticos da Tela de Configurações ------------------------
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    cartaz_config = Sprite("Assets Resized/Ribbon_Yellow_Mod.600x90.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Horizontal_Mod.1600x900.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.630x400.png", 1)


#------------------------- Botões/Elementos da Tela de Configurações (Com base nelas) ----------------------------
    # Pegando Configurações
    configs_pri = pega_config()

    # Sprite de Botão com Cursor em cima
    botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover.png")

    # Música e Efeitos Sonoros
    if configs_pri[2] == 1:
        botao_musica = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)
    else:
        botao_musica = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)
    if configs_pri[1] == 1:
        botao_efeitos = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)
    else:
        botao_efeitos = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)

    botao_musica_on_1 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)
    botao_musica_on_2 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue.png", 1)

    botao_musica_off_1 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)
    botao_musica_off_2 = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red.png", 1)

    if configs_pri[2] == 1:
        icone_musica = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_03.png")
    else:
        icone_musica = Sprite("Tiny Swords (Update 010)/UI/Icons/Pressed_03.png")
    if configs_pri[1] == 1:
        icone_efeitos = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_03.png")
    else:
        icone_efeitos = Sprite("Tiny Swords (Update 010)/UI/Icons/Pressed_03.png")

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
    nivel = configs_pri[0] - 1

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

            # Desligando Música
            if mouse.is_button_pressed(1) and delay_de_click <= 0:
                if botao_musica == botao_musica_on_1:
                    x,y = botao_musica.x, botao_musica.y
                    botao_musica = botao_musica_off_1
                    botao_musica.set_position(x, y)

                    icone_musica = icone_musica_off_1
                    icone_musica.set_position(x, y)

                    delay_de_click = 0.2

                    # Alteração no arquivo (Desligando a Música)
                    alterar_config("musica=1", "musica=0")

                # Ligando Música
                else:
                    x,y = botao_musica.x, botao_musica.y
                    botao_musica = botao_musica_on_1
                    botao_musica.set_position(x, y)

                    icone_musica = icone_musica_on_1
                    icone_musica.set_position(x, y)

                    delay_de_click = 0.2

                    # Alteração no arquivo (Ligando a Música)
                    alterar_config("musica=0", "musica=1")

        # Interação com o Botão de Efeitos
        if mouse.is_over_object(botao_efeitos):
            botao_hover.set_position(botao_efeitos.x, botao_efeitos.y)
            botao_hover.draw()
            icone_efeitos.draw()


            if mouse.is_button_pressed(1) and delay_de_click <= 0:
                # Desligando Efeitos
                if botao_efeitos == botao_musica_on_2:
                    x,y = botao_efeitos.x, botao_efeitos.y
                    botao_efeitos = botao_musica_off_2
                    botao_efeitos.set_position(x, y)

                    icone_efeitos = icone_musica_off_2
                    icone_efeitos.set_position(x, y)

                    delay_de_click = 0.2

                    # Alteração no arquivo (Desligando os Efeitos)
                    alterar_config("efeitos=1", "efeitos=0")

                # Ligando Efeitos
                else:
                    x,y = botao_efeitos.x, botao_efeitos.y
                    botao_efeitos = botao_musica_on_2
                    botao_efeitos.set_position(x, y)

                    icone_efeitos = icone_musica_on_2
                    icone_efeitos.set_position(x, y)

                    delay_de_click = 0.2

                    # Alteração no arquivo (Ligando os Efeitos)
                    alterar_config("efeitos=0", "efeitos=1")

        delay_de_click -= janela.delta_time()

        # Interação com os Botões de Dificuldade
        # Aumentando Dificuldade
        if (mouse.is_over_object(botao_mais) and mouse.is_button_pressed(1)
                and nivel <= 1 and delay_de_click <= 0):
            nivel += 1
            num_diff = Sprite(lista_num_diff[nivel])
            num_diff.set_position(botao_diff.x, botao_diff.y)
            delay_de_click = 0.2

            # Alteração no arquivo (Aumentando a Dificuldade)
            configs = pega_config()
            alterar_config("dificuldade="+str(configs[0]), "dificuldade="+str(configs[0]+1))

        if nivel == 2:
            botao_disable.set_position(botao_mais.x, botao_mais.y - 3)
            botao_disable.draw()
            mais.draw()

        # Diminuindo Dificuldade
        if (mouse.is_over_object(botao_menos) and mouse.is_button_pressed(1)
                and nivel >= 1 and delay_de_click <= 0):
            nivel -= 1
            num_diff = Sprite(lista_num_diff[nivel])
            num_diff.set_position(botao_diff.x, botao_diff.y)
            delay_de_click = 0.2

            # Alteração no arquivo (Diminuindo a Dificuldade)
            configs = pega_config()
            alterar_config("dificuldade=" + str(configs[0]), "dificuldade=" + str(configs[0] - 1))

        if nivel == 0:
            botao_disable.set_position(botao_menos.x, botao_menos.y - 3)
            botao_disable.draw()
            menos.draw()

        # Interação com a Seta de Voltar
        if mouse.is_over_object(seta):
            seta_hover.set_position(seta.x, seta.y)
            seta_hover.draw()

            if mouse.is_button_pressed(1):
                from GameWindows.menu import menu
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

