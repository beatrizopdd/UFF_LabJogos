from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.collision import*
from PPlay.keyboard import*

janela = Window(800,600)
janela.set_title("Break Bricks")
janela.set_background_color((255,255,255))

controle = janela.get_keyboard()

bola = Sprite("bola.png",1)
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 4 - bola.height / 2
skate = Sprite("skate.png",1)
skate.x = janela.width / 2 - skate.width / 2
skate.y = janela.height - skate.height - 10

bvelX = 4.5
bvelY = 4.5
svelX = 5
svelY = 5

acertos = 0
erros = 0

while True:
	
	bola.x = bola.x + bvelX
	bola.y = bola.y + bvelY

	#declara como controlar o skate
	if (controle.key_pressed("left")):
		skate.x -= svelX
	elif (controle.key_pressed("right")):
		skate.x += svelX

	#limita o movimento da bola ao tamanho da janela
	if (bola.x + bola.width >= janela.width) or (bola.x <= 0):
		bvelX *= (-1) 
	if (bola.y <= 0):
		bvelY *= (-1) 

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

	#declara o significado de acerto
	if (bola.collided(skate)):
		bvelY *= (-1) 
		acertos += 1

	janela.set_background_color((255,255,255))
	#se o texto vier antes da atualização do fundo ele não aaprece
	janela.draw_text("{} acertos".format(acertos), 50, 50, size=20, color=(0,0,0), font_name="Arial", bold=False, italic=False)
	janela.draw_text("{} erros".format(erros), 50, 85, size=20, color=(0,0,0), font_name="Arial", bold=False, italic=False)

	bola.draw()
	skate.draw()
	janela.update()

    
