from PPlay.window import *
from jogo import *

def tutorial(janela):
    mouse = Window.get_mouse()

    x = Sprite("Tiny Swords (Update 010)/UI/Icons/Regular_01.png")
    bordas = Sprite("Tiny Swords (Update 010)/UI/Pointers/02.png")
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Vertical_Mod.1000x650.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.350x280.png", 1)


    banner_buttons.x = janela.width / 2 - banner_buttons.width / 2
    banner_buttons.y = 100

    tela_buttons.x = janela.width / 2 - tela_buttons.width / 2
    tela_buttons.y = banner_buttons.y + 160

    x.x = banner_buttons.x + banner_buttons.width - 419
    x.y = banner_buttons.y + banner_buttons.height - 283

    bordas.x = banner_buttons.x + banner_buttons.width - 420
    bordas.y = banner_buttons.y + banner_buttons.height - 290


    while True:

        cenario_menu.draw()
        banner_buttons.draw()
        tela_buttons.draw()
        x.draw()
        bordas.draw()

        if mouse.is_over_area([bordas.x, bordas.y], [bordas.x + bordas.width, bordas.y + bordas.height]):

            if mouse.is_button_pressed(1):
                jogo(janela)



        janela.draw_text("- W, S, D, A para se mover", janela.width/2 - 150, janela.height/2 - 100, 28, color="black",
                         font_name="Times New Roman", bold=True, italic=False)

        janela.draw_text("- E para atacar", janela.width / 2 - 150, janela.height / 2 - 50, 28,
                         color="black", font_name="Times New Roman", bold=True, italic=False)

        janela.update()
