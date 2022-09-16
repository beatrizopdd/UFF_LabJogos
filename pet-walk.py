from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.collision import*
from PPlay.keyboard import*

import random

janela = Window(400,300)
janela.set_title("ATIRA NA MARMOTA")

fundo = Sprite("png/fundo.png",1)
fundo.set_position(0, janela.height - fundo.height)

controle = janela.get_keyboard()

indy = Sprite("png/indy2.png", 8)
indy.x = 0
indy.y = janela.height - indy.height - 50

indy.set_sequence(0,4)
indy.set_total_duration(2000)

nave = Sprite("png/nave.png", 1)
cacto = Sprite("png/cacto.png", 1)
monty = Sprite("png/monty.png", 1)

#isso vai criar uma lista de 'monstrinhos' pra serem selecionados pelo randint
opcoes = (nave,cacto,monty)

escolhido = random.randint(0,2)
alvo = opcoes[escolhido]
alvo.set_position(indy.x + alvo.width * 3 ,janela.height - alvo.height - 45)

teclaOK = False

while (True):

	fundo.draw()

	#esse bloco cria a correspondência  entre a tecla apertada e o objeto que aparece
	if (alvo == nave):
		if (controle.key_pressed("up")):
			teclaOK = True
	if (alvo == cacto):
		if (controle.key_pressed("right")):
			teclaOK = True
	if (alvo == monty):
		if (controle.key_pressed("down")):
			teclaOK = True	

	#muda o objeto se você conseguiu eliminar o anterior
	if (teclaOK == True):
		escolhido = random.randint(0,2)
		alvo = opcoes[escolhido]
		alvo.set_position(indy.x + alvo.width * 3 ,janela.height - alvo.height - 45)

		teclaOK = False


	alvo.draw()

	indy.draw()
	indy.update()

	janela.update()

    
