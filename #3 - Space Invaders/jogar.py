from PPlay.window import*
from PPlay.sprite import*

from atalho import* 
from ranking import*
import random

def jogo(nivel):

#SEÇÃO DA TELA
	janela = Window(537,457)
	janela.set_title("Jogo")

	fundo = Sprite("png/fundo.png", 1)
	fundo.x = 0
	fundo.y = 0

	tecla = janela.get_keyboard()
	
	vida = Sprite("png/vida.png", 6)
	vida.x = janela.width - vida.width
	vida.y = vida.height

#SEÇÃO DE CRIAÇÃO DA NAVE
	nave = Sprite("png/ship.png", 2)
	nave.x = (janela.width - nave.width) / 2
	nave.y = janela.height - nave.height
	nave.set_sequence_time(0, 2, 200, True)

	velN = 200
	
#SEÇÃO DE CRIAÇÃO DO DISPARO
	disparos = [] 
	recarga = 1
	velD = 100

#SEÇÃO DE CRIAÇÃO DOS MONSTROS
	#ocupa 2/3 de largura e de altura e o espaçamento entre monstros deve ser de meio monstro
	matriz_aliens = []
	
	linhas = 3
	colunas = 3
	
	velX = 50
	velY = 15
	
	boss_vida = 0
	boss_X = 1
	boss_Y = 1
	
#SEÇÃO DE CRIAÇÃO DO DISPARO dos monstros
	disparos_m = [] 
	recarga_m = 0
	velDM = 70
	
#VARIAVEIS
	#vai ser alterada ao pressionar o botão ESC
	m_ficar = True

	fr_fps = 0
	fr_timer = 0
	fr_frames = 0
	
	cronometro = 0
	
	#if status == True: jogo continua, status == False: gameover
	status = True
	
	invisibilidade = False 
	invisibilidade_timer = 0
	
	vidas = 0
	
	pontos = 0
	
	piscando = False
	
#COMEÇO DO JOGO
	while (m_ficar == True):

		m_ficar = sair()

		fundo.draw()
		
		cronometro += janela.delta_time()
		
		 
	#SEÇÃO DA NAVE
		#controle da nave
		if (tecla.key_pressed("left")):
			nave.x -= velN * janela.delta_time()
		if (tecla.key_pressed("right")):
			nave.x += velN * janela.delta_time()
			
		#limite da nave na tela
		if (nave.x <=  0):
			nave.x = 0
		if (nave.x >= janela.width - nave.width):
			nave.x = janela.width - nave.width
				

	#SEÇÃO DO DISPARO do player
		recarga += janela.delta_time()
		
		#ativa o tiro do jogador ao pressionar espaço e respeitando o tempo de recarga
		if (tecla.key_pressed("space")) and (recarga >= nivel / 5):
			disparos = novo_tiro(nave, disparos)
			recarga = 0

		#desenha, controla e limita o disparo 
		if (disparos != []):
			for d in disparos:
				d.draw()
				d.y -= velD * janela.delta_time()	
				d = limitando_tiro(d, disparos)	


	#SEÇÃO DO DISPARO do monstro
		recarga_m += janela.delta_time()
		
		#ativa o disparo do monstro respeitando o tempo de recarga
		if (recarga_m >= 1 * nivel and status == True):
			x = random.randint(0, len(matriz_aliens) - 1)
			y = random.randint(0, len(matriz_aliens[x]) - 1)
			disparos_m = novo_tiro_inimigo(matriz_aliens[x][y], disparos_m)
			recarga_m = 0

		#desenha, controla e limita o disparo 
		if (disparos_m != [] and status == True):
			for d in disparos_m:
				d.draw()
				d.y += velDM * janela.delta_time()	
				d = limitando_tiro_inimigo(d, disparos_m)	
		
		if (invisibilidade == False):
			vidas, invisibilidade = acerto_tiro_inimigo(disparos_m, nave, vidas)
			
		else:
			invisibilidade_timer += janela.delta_time()
	
			if (invisibilidade_timer < 2): #nave piscando
				nave.update()
			
			if (invisibilidade_timer >= 2):
				invisibilidade_timer = 0
				nave.curr_frame = 0
				invisibilidade = False
							
				
	#SEÇÃO PARA CRIAR MATRIZ DE MONSTROS
		#cria a matriz se ela estiver vazia
		if (matriz_aliens == [] and status == True):
			nivel += 1
			linhas = random.randint(3,4)
			colunas = random.randint(3,4)
			boss_Y = linhas - 1
			boss_X = random.randint(0,colunas - 1)
			
			matriz_aliens = nova_matriz(matriz_aliens, linhas, colunas, boss_X, boss_Y)
			
		#faz a matriz andar // função responsável pelo acerto do tiro
		if (matriz_aliens != [] and status == True):
			matriz_aliens, velX, status = movimento_matriz(matriz_aliens, velX, velY, nave, janela)

			if (disparos != []):
				pontos, boss_vida = acerto_tiro(disparos, matriz_aliens, cronometro, pontos, boss_vida)

			#desenha os aliens
			for linha in matriz_aliens:
				for coluna in linha:
					coluna.draw()

		#Game Over
		if (vidas >= 4):
			status = False

		if (status == False):
			return pontos


	#SEÇÃO PARA ESCREVER A PONTUAÇÃO
		janela.draw_text("PONTUAÇÃO {:.0f}".format(pontos), 5, vida.height, 15, (255,255,255), "Arial")


	#SEÇÃO PARA ESCREVER O FRAME RATE
		fr_frames += 1
		fr_timer += janela.delta_time()
		janela.draw_text("FPS: {:.1f}".format(fr_fps), 5, janela.height - 10, 10, (255,255,255), "Arial")

		if (fr_timer >= 1):
			fr_fps = fr_frames
			fr_timer = 0
			fr_frames = 0


	#SEÇÃO DE ATUALIZAÇÕES
		nave.draw()
		 
		vida.curr_frame = vidas
		vida.draw()
		
		janela.update()
