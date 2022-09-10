from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.collision import*
from PPlay.keyboard import*

janela = Window(300,440)
janela.set_title("Sky Jump")
janela.set_background_color((210,210,210))

controle = janela.get_keyboard()

indy = Sprite("indy.png", 8)
indy.x = janela.width / 2 - indy.width / 2
indy.y = janela.width - indy.width / 2 - 50

#importante pra que a sprite mude de frame parte 1
indy.set_sequence(0,8)
indy.set_total_duration(1600)

velX = 1
velY = 1


while True:

	indy.y += velY

	#declara como controlar o boneco
	if (controle.key_pressed("left")):
		indy.x -= velX
	elif (controle.key_pressed("right")):
		indy.x += velX

	#limita o movimento do boneco ao tamanho da janela
	if (indy.x <= 0):
		indy.x = 0
	if (indy.x + indy.width >= janela.width):
		indy.x = janela.width - indy.width

	#limita o movimento do boneco a area escolhida
	if (indy.y == janela.height / 2 - indy.height) or (indy.y + indy.height == janela.height):
		velY *= -1

	janela.set_background_color((210,210,210))
	
	#importante pra que a sprite mude de frame parte 2
	indy.draw()
	indy.update()

	janela.update()

    
