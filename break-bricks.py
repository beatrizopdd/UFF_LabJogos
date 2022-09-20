from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.collision import*
from PPlay.keyboard import*

janela = Window(500,500)
janela.set_title("Break Bricks")
janela.set_background_color((255,255,255))

controle = janela.get_keyboard()

bola = Sprite("png/bola.png",1)
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 4 - bola.height / 2

velX = 450
velY = 450

skate = Sprite("png/skate.png",1)
skate.x = janela.width / 2 - skate.width / 2
skate.y = janela.height - skate.height - 30

svelX = 5
svelY = 5

acertos = 0
erros = 0

while True:
	
	#convertendo a velocidade no tempo do jogo (não me pergunte pq)
	bola.x += velX * janela.delta_time()
	bola.y += velY * janela.delta_time()

	#impedindo a bola sair da tela // resolvendo o bug da bola sair escoregando na parede
	if (bola.x <= 0):
		bola.x = 0
		velX *= (-1) 
	if (bola.x + bola.width >= janela.width):
		bola.x = janela.width - bola.width
		velX *= (-1)
	if (bola.y <= 0):
		bola.y = 0
		velY *= (-1) 
		
	#declara como controlar o skate
	if (controle.key_pressed("left")):
		skate.x -= svelX
	elif (controle.key_pressed("right")):
		skate.x += svelX

	#limita o movimento do skate ao tamanho da janela
	if (skate.x <= 0):
		skate.x = 0
	if (skate.x + skate.width >= janela.width):
		skate.x = janela.width - skate.width

	#declara o significado de erro ao jogo
	if (bola.y + bola.height >= janela.height):
		erros += 1
		bola.x = janela.width / 2 - bola.width / 2
		bola.y = janela.height / 4 - bola.height / 2

	#reação da bola ao entrar em contato com o skate // correção da bolinha passando por dentro do pad
	if (bola.collided(skate)):
		acertos += 1
		bola.y = skate.y - skate.height - (bola.height / 2)
		velY *= (-1)

	janela.set_background_color((255,255,255))

	#se o texto vier antes da atualização do fundo ele não aparece
	janela.draw_text("{} pontos".format(acertos), 50, 50, size=20, color=(0,0,0), font_name="Arial", bold=False, italic=False)
	janela.draw_text("{} erros".format(erros), 50, 85, size=20, color=(0,0,0), font_name="Arial", bold=False, italic=False)

	bola.draw()
	skate.draw()
	janela.update()

    
