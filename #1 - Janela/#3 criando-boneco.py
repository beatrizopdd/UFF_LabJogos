from PPlay.window import *
from PPlay.sprite import*
from PPlay.animation import*

janela = Window(200,200)
janela.set_title("Janela")

#nome-atribuido-ao-objeto = Sprite("nome-do-arquivo.formato", qtd-de-frames) 
boneco = Sprite("png/boneco.png",1)

#nome-atribuido.x/y = posição inicial do objeto
boneco.x = (janela.width - boneco.width) / 2
boneco.y = (janela.height - boneco.height) / 2

while True:

	#tem que vir antes do draw() pra apagar os rastros do boneco a cada desenho (só vai servir quando a gente começar a movimentar boneco)
	janela.set_background_color((252, 248, 177))

	#o boneco tem que ser desenhado antes da atualização da janela
	boneco.draw()

	janela.update()
