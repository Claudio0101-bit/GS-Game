from jogo import *
from Functions import *
from PPlay.window import *

def menu(janela, mouse):

#---------------------------- Elementos estéticos da Tela de Menu -------------------------------------
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    titulo = Sprite("Assets Resized/Ribbon_Red_Mod.600x90.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Vertical_Mod.1000x650.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.350x280.png", 1)

    # Botões da Tela de Menu
    botao_jogar = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png",1)
    botao_press = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides_Pressed.png",1)
    botao_config = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png", 1)
    botao_sair = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides.png",1)
    botao_sair_press = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides_Pressed.png",1)
    botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover_3Slides.png",1)

#------------------------------ Atribuição de coordenadas aos Elementos do Menu -----------------------------
    titulo.x = janela.width/2 - titulo.width/2
    titulo.y = 100

    banner_buttons.x = janela.width/2 - banner_buttons.width/2
    banner_buttons.y = 100

    tela_buttons.x = janela.width/2 - tela_buttons.width/2
    tela_buttons.y = banner_buttons.y + 160

    botao_jogar.x = janela.width/2 - botao_jogar.width/2
    botao_jogar.y = tela_buttons.y + 20

    botao_config.x = janela.width / 2 - botao_config.width / 2
    botao_config.y = botao_jogar.y + botao_jogar.height + 20

    botao_sair.x = janela.width / 2 - botao_config.width / 2
    botao_sair.y = botao_config.y + botao_config.height + 20
    botao_sair_press.x = botao_sair.x
    botao_sair_press.y = botao_sair.y

    # Game Loop !!!!!!
    while True:
        # Desenhando Elementos da Tela de Menu
        cenario_menu.draw()
        titulo.draw()
        banner_buttons.draw()
        tela_buttons.draw()
# ----------------------- Interações com os Botões da Tela de Menu ----------------------------
        # Jogar
        if mouse.is_over_area([botao_jogar.x, botao_jogar.y], [botao_jogar.x + botao_jogar.width,
                                                              botao_jogar.y + botao_jogar.height]):
            botao_hover.set_position(botao_jogar.x, botao_jogar.y)
            botao_hover.draw()

            if mouse.is_button_pressed(1):

                objetivo(janela, mouse)
        else:
            botao_jogar.draw()

        # Configurações
        if mouse.is_over_area([botao_config.x, botao_config.y], [botao_config.x + botao_config.width,
                                                                 botao_config.y + botao_config.height]):
            botao_hover.set_position(botao_config.x, botao_config.y)
            botao_hover.draw()

            if mouse.is_button_pressed(1):
                configurar(janela, mouse)

        else:
            botao_config.draw()

        # Sair
        if mouse.is_over_area([botao_sair.x, botao_sair.y], [botao_sair.x + botao_sair.width,
                                                              botao_sair.y + botao_sair.height]):
            botao_hover.set_position(botao_sair.x, botao_sair.y)
            botao_hover.draw()

            if mouse.is_button_pressed(1):
                janela.close()

        else:
            botao_sair.draw()

# ----------------------- Escrevendo Textos na Tela de Configurações ------------------------------
        # Título Goblin Slayer
        janela.draw_text("Goblin Slayer",janela.width/2 - botao_jogar.width/2, 110, size=36,
                              color="white", font_name="Times New Roman", bold=True, italic=False)
        # Jogar
        janela.draw_text("Jogar", botao_jogar.x + botao_jogar.width/2 - 25, botao_jogar.y + 10, size=24,
                         color="black", font_name="Arial", bold=True, italic=False)
        # Configurações
        janela.draw_text("Configurações", botao_config.x + botao_config.width / 2 - 70, botao_config.y + 10, size=24,
                         color="black", font_name="Arial", bold=True, italic=False)
        # Sair
        janela.draw_text("Sair", botao_sair.x + botao_sair.width / 2 - 15, botao_sair.y + 10, size=24,
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
