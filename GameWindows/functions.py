from random import randint
from GameObjects.goblin import Goblin
from GameObjects.goblin_bomba import Goblin_bomba
from GameObjects.goblin_tnt import Goblin_tnt
from PPlay.sprite import Sprite

#------------------------------ Código com Funções Alternativas -------------------------------


def chave_y(objeto):
    return objeto.y

def format_tempo(segundos):
    horas = int(segundos // 3600)
    minutos = int((segundos % 3600) // 60)
    segundos = int(segundos % 60)

    return f"{horas:02}:{minutos:02}:{segundos:02}"


#------------------------ Função que forma Horda de Goblins -----------------------------------
def preenche_lista_goblins(dificuldade, onda, w_width, w_height, vel):
    lista_goblins = []
    for i in range(onda + dificuldade):
        goblin = Goblin(w_width, w_height, vel)
        goblin.x += randint(0, 13) * 64
        goblin.y += randint(0, 3) * 64
        lista_goblins.append(goblin)
    if onda + dificuldade - 2 > 0:
        for i in range(onda + dificuldade - 2):
            goblin_bomba = Goblin_bomba(w_width, w_height, vel)
            goblin_bomba.x += randint(0, 13) * 64
            goblin_bomba.y += randint(0, 3) * 64
            lista_goblins.append(goblin_bomba)
    if onda + dificuldade - 5 > 0:
        for i in range(onda + dificuldade - 5):
            goblin_tnt = Goblin_tnt(w_width, w_height, vel)
            goblin_tnt.x += randint(0, 13) * 64
            goblin_tnt.y += randint(0, 3) * 64
            lista_goblins.append(goblin_tnt)
    return lista_goblins


#------------------------ Função para ler dados de Arquivo Texto das Configurações ----------------------------
def pega_config():
    configs = None
    with open("configs/config.txt", "r") as c:
        configs = c.readlines()
        c.close()
    for i in range(3):
        aux = configs[i].split(sep="=")
        configs[i] = int(aux[1])
    return configs

def alterar_config(antigo, novo):
    # ----------------------- Alteração no arquivo ---------------------
    # Lê o conteúdo do arquivo
    with open("configs/config.txt", 'r', encoding='utf-8') as r:
        conteudo = r.read()

    # Substitui o caractere antigo pelo novo
    conteudo_modificado = conteudo.replace(antigo, novo)

    # Escreve o conteúdo modificado de volta ao arquivo
    with open("configs/config.txt", 'w', encoding='utf-8') as f:
        f.write(conteudo_modificado)


#-------------------------- Função com tela de Objetivos ----------------------------
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
                from GameWindows.jogo import jogo
                jogo(janela, mouse)

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


#---------------------------- Função com Tela de Game Over -----------------------------
def game_over(janela, mouse, num_mortos, tempo):

    # Atualizando Recordes
    recorde_num_mortos = 0
    recorde_tempo = 0

    if num_mortos > recorde_num_mortos:
        recorde_num_mortos = num_mortos
    if recorde_tempo < tempo:
        recorde_tempo = tempo
    # Elementos estéticos da Tela de Game Over
    cenario_menu = Sprite("Assets Resized/Fundo-GS-Menu_1500x800.png", 1)
    cartaz_game_over = Sprite("Assets Resized/Ribbon_Red_Mod.600x90.png", 1)
    banner_buttons = Sprite("Assets Resized/Banner_Horizontal_Mod.1600x900.png", 1)
    tela_buttons = Sprite("Tiny Swords (Update 010)/UI/Banners/Carved_9Slides.png", 1)

    # Botões da Tela de Game Over
    botao_jogar = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png", 1)
    botao_menu = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides.png", 1)

    # Botão selecionado
    botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover_3Slides.png", 1)

    #------------------ Atribuição de coordenadas aos Elementos do Game Over -----------------------------
    cartaz_game_over.x = janela.width/2 - cartaz_game_over.width/2
    cartaz_game_over.y = 100

    banner_buttons.x = janela.width/2 - banner_buttons.width/2
    banner_buttons.y = -10

    tela_buttons.x = janela.width/2 + tela_buttons.width/2
    tela_buttons.y = banner_buttons.y + 400

    botao_jogar.x = tela_buttons.x
    botao_jogar.y = tela_buttons.y + 30

    botao_menu.x = tela_buttons.x
    botao_menu.y = tela_buttons.y + 100

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
                from jogo import jogo
                jogo(janela, mouse)

        # Menu
        if mouse.is_over_object(botao_menu):
            botao_hover.set_position(botao_menu.x, botao_menu.y)
            botao_hover.draw()
            if mouse.is_button_pressed(1):
                from GameWindows.menu import menu
                menu(janela, mouse)


    # ----------------------- Escrevendo Textos na Tela de Configurações ------------------------------
        # Título ( Game Over )
        janela.draw_text("Game Over", janela.width / 2 - botao_jogar.width / 2, 110, size=36,
                         color="white", font_name="Times New Roman", bold=True, italic=False)

        # Jogar de novo
        janela.draw_text("Tentar de novo", botao_jogar.x + botao_jogar.width / 2 - 70, botao_jogar.y + 10, size=24,
                         color="black", font_name="Arial", bold=True, italic=False)

        # Voltar ao Menu
        janela.draw_text("Menu", botao_menu.x + botao_menu.width / 2 - 30, botao_menu.y + 10, size=24,
                         color="black", font_name="Arial", bold=True, italic=False)

        # Estatísticas
        janela.draw_text("Estatísticas:", banner_buttons.x + 500, banner_buttons.y  + 270,
                         size=36, color="black", font_name="Arial", bold=True, italic=False)

        # Goblins Derrotados
        janela.draw_text(f"- Goblins Derrotados: {num_mortos}", banner_buttons.x + 500, banner_buttons.y + 320,
                         size=24, color="black", font_name="Arial", bold=True, italic=False)

        # Tempo de Jogo
        janela.draw_text(f"- Tempo de Jogo: {format_tempo(tempo)}", banner_buttons.x + 500, banner_buttons.y + 350,
                         size=24, color="black", font_name="Arial", bold=True, italic=False)

        # Recordes
        janela.draw_text("Recordes:", banner_buttons.x + 500, banner_buttons.y + 450,
                         size=36, color="blue", font_name="Arial", bold=True, italic=False)

        # Goblins Derrotados (recorde)
        janela.draw_text(f"- Goblins Derrotados: {recorde_num_mortos}",
                         banner_buttons.x + 500, banner_buttons.y + 500,
                         size=24, color="red", font_name="Arial", bold=True, italic=False)

        # Tempo de Jogo (recorde)
        janela.draw_text(f"- Tempo de Jogo: {format_tempo(tempo)}", banner_buttons.x + 500, banner_buttons.y + 530,
                         size=24, color="red", font_name="Arial", bold=True, italic=False)


        # Escondendo Cursor do Mouse padrão
        mouse.hide()

        # Atribuição de Novo Mouse dentro da Janela
        if mouse.is_over_area([0, 0], [janela.width, janela.height]):
            cords_mouse = mouse.get_position()
            a = Sprite("Tiny Swords (Update 010)/UI/Pointers/01.png", 1)
            a.set_position(cords_mouse[0] - 30, cords_mouse[1] - 25)
            a.draw()

        janela.update()

def melhoria(janela, mouse, player):
    # ---------------------------- Elementos estéticos da Tela de Melhoria -------------------------------------
    banner_buttons = Sprite("Assets Resized/Banner_Vertical_Mod.1000x650.png", 1)
    tela_buttons = Sprite("Assets Resized/Carved_9Slides_Mod.350x280.png", 1)

    botao_vida = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Red_3Slides.png", 1)
    botao_attack = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Blue_3Slides.png", 1)
    botao_hover = Sprite("Tiny Swords (Update 010)/UI/Buttons/Button_Hover_3Slides.png", 1)

    # ------------------ Atribuição de coordenadas aos Elementos da Tela de Melhoria -----------------------------
    botao_vida.x = janela.width / 2 - botao_vida.width / 2
    botao_vida.y = tela_buttons.y + 20 + botao_vida.height + 20

    botao_attack.x = janela.width / 2 - botao_vida.width / 2
    botao_attack.y = botao_vida.y + botao_vida.height + 20

    while True:
        # ----------------------- Escrevendo Textos na Tela de Melhoria ------------------------------
        banner_buttons.draw()
        tela_buttons.draw()
        botao_vida.draw()
        botao_attack.draw()

        # Interação com o Botão de Recuperar Vida
        if mouse.is_over_object(botao_vida):
            botao_hover.set_position(botao_vida.x, botao_vida.y)
            botao_hover.draw()

            if mouse.is_button_pressed(1):
                if player.vida < 5:
                    player.vida += 1
                    break

        # Interação com o Botão de Aumentar Attack Speed
        if mouse.is_over_object(botao_attack):
            botao_hover.set_position(botao_attack.x, botao_attack.y)
            botao_hover.draw()

            if mouse.is_button_pressed(1):
                if player.cooldown_forte > 1:
                    player.cooldown_atq_forte -= 0.2
                    break

        # ----------------------- Escrevendo Textos na Tela de Melhoria ------------------------------

            # Para a próxima Horda:
            janela.draw_text("Para a próxima Horda:", tela_buttons.x + tela_buttons.width / 2 - 50,
                             tela_buttons.y + 30, size=24, color="black", font_name="Arial", bold=True, italic=False)
            # Recuperar 1 de Vida
            janela.draw_text("Recuperar 1 de Vida", botao_vida.x + botao_vida.width / 2 - 70, botao_vida.y + 10,
                             size=24, color="black", font_name="Arial", bold=True, italic=False)
            # +1 Attack Speed
            janela.draw_text("+1 Vel. Ataque", botao_attack.x + botao_attack.width / 2 - 15, botao_attack.y + 10,
                             size=24, color="black", font_name="Arial", bold=True, italic=False)

            # Escondendo Cursor do Mouse padrão
            mouse.hide()

            # Atribuição de Novo Mouse dentro da Janela
            if mouse.is_over_area([0, 0], [janela.width, janela.height]):
                cords_mouse = mouse.get_position()
                a = Sprite("Tiny Swords (Update 010)/UI/Pointers/01.png", 1)
                a.set_position(cords_mouse[0] - 30, cords_mouse[1] - 25)
                a.draw()

            janela.update()