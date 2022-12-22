from PPlay.window import*
from PPlay.sprite import*

janela = Window(537,457)
tecla = janela.get_keyboard()

#economiza linhas pra desenhar e posicionar os botões do menu
def posicao(sprite, X, Y):

	sprite.x = X
	sprite.y = Y
	sprite.draw()


#fecha a tela quando pressiona esc
def sair():

	if (tecla.key_pressed("ESC")):
		return False 
	else:
		return True


#criando matriz de monstros
def nova_matriz(matriz, linhas, colunas, boss_X, boss_Y):
	
	for l in range(linhas):
		coluna = []
		for c in range(colunas):
			if (l == boss_Y and c == boss_X):
				alien = Sprite("png/a4.png", 2)
				alien.curr_frame = 0
			else:
				alien = Sprite("png/a3.png", 1)
				
			alien.x = (alien.width + alien.width / 2) * c + 10 #margem de erro
			alien.y = (alien.height + alien.height / 2)  * l
			coluna.append(alien)

		matriz.append(coluna)
	
	return matriz
	
	
#os monstros andando
def colisao_matriz(matriz, velX, nave, janela):
	
	lateral = False
	base = True
	
	for linha in matriz:
		for alien in linha:
			alien.x += velX * janela.delta_time()
			if (alien.x <= 5 or alien.x + alien.width + 5 >= janela.width):
				lateral = True
			if (alien.y + alien.height >= nave.y):
				base = False
	
	return lateral, base

def movimento_matriz(matriz, velX, velY, nave, janela):

	c_lateral, c_base = colisao_matriz(matriz, velX, nave, janela)
			
	if (c_lateral == True):
		velX *= -1
		for linha in matriz:
			for alien in linha: 
				alien.y += velY
	
	return matriz, velX, c_base
		
		
#criação do objeto tiro
def novo_tiro(nave, lista_de_tiros):

	tiro = Sprite("png/laser_m.png", 5)
	tiro.set_sequence_time(0, 4, 300, True)
	
	#posiciona o disparo exatamente em cima e no meio da nave
	tiro.x = nave.x + 2
	tiro.y = nave.y - tiro.height
	
	lista_de_tiros.append(tiro)
	
	return lista_de_tiros
	
	
def limitando_tiro(tiro, lista_de_tiros): 
	#controlando a animação do laser pra acontecer só quando ele estiver quase saindo da tela
	if (tiro.y <= tiro.height * 3):
		tiro.update()
	
	if (tiro.y <= 0):
		lista_de_tiros.remove(tiro)
	
	
#determina o tamanho da matriz de monstros no espaço 
def limites_matriz(lista_de_aliens):

	listaX = []
	listaY = []
	
	for linha in lista_de_aliens: #foi bem aqui que eu destrui a otimização do meu jogo
		for alien in linha:
		
			listaX.append(alien.x)
			listaY.append(alien.y)
	
	minX = min(listaX)
	maxX = max(listaX) + lista_de_aliens[0][0].x
	minY = min(listaY)
	maxY = max(listaY) + lista_de_aliens[0][0].y
	
	return minX, maxX, minY, maxY
		
		
#tiro da nave no monstro
def acerto_tiro(lista_de_tiros, lista_de_aliens, timer, pontos, boss_vida):
	
	minX, maxX, minY, maxY = limites_matriz(lista_de_aliens)
	
	for tiro in lista_de_tiros:
		
		if (tiro.x >= minX and tiro.x <= maxX) and (tiro.y >= minY and tiro.y <= maxY):
			for i in range(len(lista_de_aliens) - 1, -1, -1):
				
				if (lista_de_aliens[i] != []):
					minX, maxX, minY, maxY = limites_matriz(lista_de_aliens)
					
					for alien in lista_de_aliens[i]:
					
						if (tiro.collided(alien) and (tiro in lista_de_tiros)):
							lista_de_tiros.remove(tiro)
							pontos += (100 + 100 / timer)
							
							if (alien.total_frames == 1):
								lista_de_aliens[i].remove(alien)
								
							if (alien.total_frames == 2):
								boss_vida += 1

								if (boss_vida == 2):
									alien.curr_frame = 1
								if (boss_vida == 3):
									lista_de_aliens[i].remove(alien)
								

				if (lista_de_aliens[i] == []):
					lista_de_aliens.pop(i)
					
				

	return pontos, boss_vida
	
	
#criação do objeto tiro inimigo
def novo_tiro_inimigo(alien, lista_de_tiros):

	tiro = Sprite("png/laser.png", 5)
	tiro.set_sequence_time(0, 4, 300, True)
	
	#posiciona o disparo exatamente em cima e no meio da nave
	tiro.x = alien.x + 2
	tiro.y = alien.y + alien.height + tiro.height
	
	lista_de_tiros.append(tiro)
	
	return lista_de_tiros
	
	
def limitando_tiro_inimigo(tiro, lista_de_tiros): 

	#controlando a animação do laser pra acontecer só quando ele estiver quase saindo da tela
	if (tiro.y >= janela.height - tiro.height * 4):
		tiro.update()
	
	if (tiro.y >= janela.height):
		lista_de_tiros.remove(tiro)
		
		
#tiro do monstro na nave
def acerto_tiro_inimigo(lista_de_tiros, nave, vidas):
	
	invisibilidade = False
	
	for tiro in lista_de_tiros:
	
		if (tiro.collided(nave) and (tiro in lista_de_tiros)):
			lista_de_tiros.remove(tiro)				
			vidas += 1
			invisibilidade = True
			nave.x = (janela.width - nave.width) / 2
			
			break

	return vidas, invisibilidade

	
	
	
