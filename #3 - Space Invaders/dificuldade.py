from PPlay.window import*
from PPlay.sprite import*

import atalho

def tela():

	janela = Window(537,457)
	janela.set_title("Dificuldade")

	dificuldade = Sprite("png/tela-difi.png", 1)
	dificuldade.x = 0
	dificuldade.y = 0

	mouse = janela.get_mouse()
	tecla = janela.get_keyboard()

	b_facil = Sprite("png/facil.png", 1)
	b_medio = Sprite("png/medio.png", 1)
	b_dificil = Sprite("png/dificil.png", 1)

	m_ficar = True
	
	sair_difi = False
	escolhida_difi = 5
	
	troca_timer = 0

	while (m_ficar == True):

		dificuldade.draw()

		m_ficar = atalho.sair()

		#os numeros da dificuldade são invertidos 
		#FACIL = 5 unidade de tempo para recarga; 
		#MEDIO = 10 da unidade de tempo para recarga; 
		#DIFICIL = 20 unidade de tempo para recarga;

		if mouse.is_over_area([95,215], [440,255]): 
			atalho.posicao(b_facil, 95, 215)
			if (mouse.is_button_pressed(1)):
				escolhida_difi = 5
				sair_difi = True

		if mouse.is_over_area([95,265], [440,305]):
			atalho.posicao(b_medio, 95, 265)
			if (mouse.is_button_pressed(1)):
				escolhida_difi = 10
				sair_difi = True

		if mouse.is_over_area([95,315], [440,355]):
			atalho.posicao(b_dificil, 95, 315)
			if (mouse.is_button_pressed(1)):
				escolhida_difi = 20
				sair_difi = True
				
		if (sair_difi == True):
			troca_timer += janela.delta_time()
			if (troca_timer >= 1):
				return escolhida_difi



		janela.update()

