from PPlay.window import *
from menu import *

# Definição da Janela do MENU, seu título e tamanho
janela = Window(1500, 800)
janela.set_title("Goblin Slayer")
janela.set_background_color([0, 0, 0])

# Detecção do Mouse
mouse = Window.get_mouse()

# Chamando Menu e iniciando o jogo
menu(janela, mouse)
