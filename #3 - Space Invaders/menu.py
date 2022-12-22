from PPlay.window import*
from PPlay.sprite import*

import jogar
import dificuldade
import atalho
from ranking import*

janela = Window(537,457)
janela.set_title("Space Invaders")

mouse = janela.get_mouse()

menu = Sprite("png/menu.png", 1)
menu.x = 0
menu.y = 0

#sprites dos botões
b_jogar = Sprite("png/jogar.png", 1)
b_difi = Sprite("png/dificuldade.png", 1)
b_rank = Sprite("png/ranking.png", 1)
b_sair = Sprite("png/sair.png", 1)

#variaveis que vão alterar a tela
ini_jogar = False
ini_difi = False
ini_rank = False
ini_sair = True


troca_timer = 0

#nivel de dificuldade
nivel = 2

pontuacao = None

while (ini_sair == True):

	menu.draw()

	#se o mouse "está sobre o botão", posiciona o botão iluminado // se "botão é pressionado" ativa o inicializador de troca de tela
	if mouse.is_over_area([95,215], [440,255]): 
		atalho.posicao(b_jogar, 95, 215)
		if (mouse.is_button_pressed(1)):
			ini_jogar = True 
			
	if mouse.is_over_area([95,265], [440,305]):
		atalho.posicao(b_difi, 95, 265)
		if (mouse.is_button_pressed(1)):
			ini_difi = True
				
	if mouse.is_over_area([95,315], [440,355]):
		atalho.posicao(b_rank, 95, 315)
		if (mouse.is_button_pressed(1)):
			ini_rank = True
		
	if mouse.is_over_area([95,365], [440,405]):
		atalho.posicao(b_sair, 95, 365)
		if (mouse.is_button_pressed(1)):
			ini_sair = False
			
	#ativa a outra tela		
	if (ini_jogar == True or ini_difi == True or ini_rank == True):
		troca_timer += janela.delta_time()
		
		if (troca_timer >= 1 and ini_jogar == True):
			pontuacao = jogar.jogo(nivel)
			ini_jogar = False
			troca_timer = 0
			
		if (troca_timer >= 1 and ini_difi == True):
			nivel = dificuldade.tela()
			ini_difi = False
			troca_timer = 0
			
		if (troca_timer >= 1 and ini_rank == True):
			mostrar_ranking()
			ini_rank = False
			troca_timer = 0
			
	if (pontuacao != None):
		pontuacao = input_ranking(pontuacao)
		
		

	janela.update()

