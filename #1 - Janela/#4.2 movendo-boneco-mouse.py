from PPlay.window import *
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.mouse import*

janela = Window(300,300)
janela.set_title("Janela")

#nome-atribuido-ao-mouse = nome-atribuido-a-tela.GET_MOUSE()
controle = janela.get_mouse()

boneco = Sprite("png/boneco.png",1)
boneco.x = janela.width / 2 - boneco.width / 2
boneco.y = janela.height / 2 - boneco.height / 2

while True:

	#pega a posição do mouse se ele estiver na tela (uma lista [X,Y]) e atribui esses valores a variáveis
	if (controle.is_on_screen):
		p_mouse = controle.get_position()
		mouseX = p_mouse[0]
		mouseY = p_mouse[1]

	#converte a posição do mouse para posição do boneco 
	boneco.x = mouseX
	boneco.y = mouseY

	if (boneco.x <= 0):
		boneco.x = 0
	if (boneco.x + boneco.width >= janela.width):
		boneco.x = janela.width - boneco.width
	if (boneco.y <= 0):
		boneco.y = 0
	if (boneco.y >= janela.height - boneco.height):
		boneco.y = janela.height - boneco.height

	janela.set_background_color((252, 248, 177))

	janela.draw_text("USE O MOUSE",15, 15, 20, (0,0,0), "Arial", False, False)

	boneco.draw()

	janela.update()
