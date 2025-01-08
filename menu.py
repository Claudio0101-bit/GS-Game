from jogo import *
from Functions import *
from PPlay.window import *

# Definição da Janela do MENU, seu título e tamanho
janela = Window(1500, 800)
janela.set_title("Goblin Slayer")
janela.set_background_color([0, 0, 0])
mouse = Window.get_mouse()

cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
titulo = Sprite("Assets Resized/Ribbon_Red_Mod.600x90.png", 1)
banner_buttons = Sprite("Assets Resized/Banner_Vertical_Mod.1000x650.png", 1)
tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.350x280.png", 1)

botao_jogar = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png",1)
botao_press = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides_Pressed.png",1)
botao_opcoes = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png",1)
botao_sair = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides.png",1)
botao_sair_press = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides_Pressed.png",1)
botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover_3Slides.png",1)

titulo.x = janela.width/2 - titulo.width/2
titulo.y = 100

banner_buttons.x = janela.width/2 - banner_buttons.width/2
banner_buttons.y = 100

tela_buttons.x = janela.width/2 - tela_buttons.width/2
tela_buttons.y = banner_buttons.y + 160

botao_jogar.x = janela.width/2 - botao_jogar.width/2
botao_jogar.y = tela_buttons.y + 20

botao_opcoes.x = janela.width/2 - botao_opcoes.width/2
botao_opcoes.y = botao_jogar.y + botao_jogar.height + 20

botao_sair.x = janela.width/2 - botao_opcoes.width/2
botao_sair.y = botao_opcoes.y + botao_opcoes.height + 20
botao_sair_press.x = botao_sair.x
botao_sair_press.y = botao_sair.y

while True:

    cenario_menu.draw()
    titulo.draw()
    banner_buttons.draw()
    tela_buttons.draw()

    if mouse.is_over_area([0,0], [janela.width,janela.height]):
        a = Sprite("Tiny Swords (Update 010)/UI/Pointers/01.png", 1)


    if mouse.is_over_area([botao_jogar.x, botao_jogar.y], [botao_jogar.x + botao_jogar.width,
                                                          botao_jogar.y + botao_jogar.height]):
        botao_hover.set_position(botao_jogar.x, botao_jogar.y)
        botao_hover.draw()

        if mouse.is_button_pressed(1):

            tutorial(janela)
    else:
        botao_jogar.draw()

    if mouse.is_over_area([botao_opcoes.x, botao_opcoes.y], [botao_opcoes.x + botao_opcoes.width,
                                                           botao_opcoes.y + botao_opcoes.height]):
        botao_hover.set_position(botao_opcoes.x, botao_opcoes.y)
        botao_hover.draw()

        #if mouse.is_button_pressed(1):

    else:
        botao_opcoes.draw()

    if mouse.is_over_area([botao_sair.x, botao_sair.y], [botao_sair.x + botao_sair.width,
                                                          botao_sair.y + botao_sair.height]):
        botao_hover.set_position(botao_sair.x, botao_sair.y)
        botao_hover.draw()

        if mouse.is_button_pressed(1):
            janela.close()
    else:
        botao_sair.draw()


    janela.draw_text("Goblin Slayer",janela.width/2 - botao_jogar.width/2, 110, size=36,
                          color="white", font_name="Times New Roman", bold=True, italic=False)
    janela.update()
