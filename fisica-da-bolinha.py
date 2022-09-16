from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*

janela = Window(600,600)
janela.set_title("Bolinha")
janela.set_background_color((210,210,210))

#nome-atribuido-ao-objeto = Sprite("nome-do-arquivo.formato", qtd-de-frames) 
bola = Sprite("png/bola.png",1)

#nome-atribuido.x/y = posição inicial do objeto
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

#valores que representam de quantos em quantos "pixels por loop" o objeto se locomove
velX = 2
velY = 2

while True:
	
	#movimento automático do objeto
	bola.x = bola.x + velX
	bola.y = bola.y + velY
	
	#limita o movimento do objeto ao tamanho da janela
	if (bola.x + bola.width >= janela.width) or (bola.x <= 0):
		velX *= (-1) 
	if (bola.y + bola.height >= janela.height)or (bola.y <= 0):
		velY *= (-1) 
	
	#pinta a janela da cor que você quer// apaga os rastros do movimento do objeto 
	janela.set_background_color((210,210,210))
	
	#a bola tem que ser desenhada antes da atualização da janela
	bola.draw()
	janela.update()

    
