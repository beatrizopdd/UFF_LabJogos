from PPlay.window import *
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.keyboard import*

janela = Window(300,300)
janela.set_title("Janela")

#nome-atribuido-ao-teclado = nome-atribuido-a-tela.GET_KEYBOARD()
controle = janela.get_keyboard()

boneco = Sprite("png/boneco.png",1)
boneco.x = janela.width / 2 - boneco.width / 2
boneco.y = janela.height / 2 - boneco.height / 2

#valor que representa de quantos em quantos pixels o objeto se locomove
velocidade = 3

while True:

	#controle do boneco
	if (controle.key_pressed("up")):
		boneco.y -= velocidade
	if (controle.key_pressed("right")):
		boneco.x += velocidade
	if (controle.key_pressed("down")):
		boneco.y += velocidade
	if (controle.key_pressed("left")):
		boneco.x -= velocidade

    #impede que o boneco saia da tela
	if (boneco.x <= 0):
		boneco.x = 0
	if (boneco.x + boneco.width >= janela.width):
		boneco.x = janela.width - boneco.width
	if (boneco.y <= 0):
		boneco.y = 0
	if (boneco.y >= janela.height - boneco.height):
		boneco.y = janela.height - boneco.height

	janela.set_background_color((252, 248, 177))

	#textos tem que ser colocados entre a atualização de fundo e a atualização de janela
	janela.draw_text("USE AS SETAS",15, 15, 20, (0,0,0), "Arial", False, False)

	boneco.draw()

	janela.update()
