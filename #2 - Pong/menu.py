from PPlay.window import*
from PPlay.sprite import*

from jogo_um import*
from jogo_dois import*
from atalhos import*

janela = Window(720,400)
janela.set_title("Pong")
janela.set_background_color((219, 210, 81))

mouse = janela.get_mouse()

menu = Sprite("png/menu.png", 1)
menu_1 = Sprite("png/menu1.png", 1)
menu_2 = Sprite("png/menu2.png", 1)

while (True):

	janela.set_background_color((219, 210, 81))

	if mouse.is_over_area([276,186], [495,235]): 
		menu_1.draw()
		if (mouse.is_button_pressed(1)):
			jogo_uj()
			
	elif mouse.is_over_area([276,250], [540,298]):
		menu_2.draw()
		if (mouse.is_button_pressed(1)):
			jogo_dj()
	
	else:
		menu.draw()
		

	janela.update()
