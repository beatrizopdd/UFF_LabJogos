from PPlay.window import*
from PPlay.sprite import*
#from PPlay.keyboard import*
#from PPlay.collision import*

def sair(teclado):
	
	if (teclado.key_pressed("esc")):
		return False
	else:
		return True

def controle_pad(player, pad, vel, teclado, janela):

	if (player == "e"):
		if (teclado.key_pressed("w")):
			pad.y -= vel * janela.delta_time()
		elif (teclado.key_pressed("s")):
			pad.y += vel * janela.delta_time()

	if (player == "d"):
		if (teclado.key_pressed("up")):
			pad.y -= vel * janela.delta_time()
		elif (teclado.key_pressed("down")):
			pad.y += vel * janela.delta_time()
                
	if (pad.y <= 0):
		pad.y = 0
	if (pad.y + pad.height >= janela.height):
		pad.y = janela.height - pad.height


def controle_ia(bola, velBY, pad, velP, janela):

	#movimento da ia induzindo ao erro (não muito lerda pra não parecer burra, nem muito esperta pra não parecer roubada...)
	#se a bola tiver passado do meio em direção a IA + estiver na metade inferior + descendo 
	#se a bola tiver passado do meio em direção a IA + estiver na metade superior + subindo
	if (bola.x >= janela.width / 2 and bola.y >= janela.height / 2 and velBY > 0):
		pad.y += velP * janela.delta_time()
	if (bola.x >= janela.width / 2 and bola.y <= janela.height / 2 and velBY < 0):
		pad.y -= velP * janela.delta_time()
                
	if (pad.y <= 0):
		pad.y = 0
	if (pad.y + pad.height >= janela.height):
		pad.y = janela.height - pad.height


def controle_bola(bola, velBX, velBY, rebatidas, pad1, pad2, janela):
	
	bola.x += velBX * janela.delta_time()
	bola.y += velBY * janela.delta_time()

	if (pad1.collided(bola)):
		velBX *= (-1)
		rebatidas += 1
		bola.x = pad1.x + pad1.width
		
	if (pad2.collided(bola)):
		velBX *= (-1)
		rebatidas += 1
		bola.x = pad2.x - bola.width
		
	#bola não sai da tela no eixo Y
	if (bola.y <= 0):
		bola.y = 0
		velBY *= (-1)
		
	if (bola.y + bola.height >= janela.height):
		bola.y = janela.height - bola.height
		velBY *= (-1)
		

	return velBX, velBY, rebatidas


def pontuacao(bola, velBX, pad1, pad2, p1p, p2p, janela, rebatidas, extra=False):

	if (bola.x + bola.width >= janela.width or bola.x <= 0):
		if (bola.x + bola.width >= janela.width):
			p1p += 1
		if (bola.x <= 0):
			p2p += 1
		
		if (extra == True):
			bola.x = -bola.width
			rebatidas = 0
		else:
			bola.x = (janela.width - bola.width) / 2
		
		bola.y = (janela.height - bola.height) / 2
		velBX *= -1

	return p1p, p2p, velBX, rebatidas



