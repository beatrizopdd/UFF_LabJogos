from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*

janela = Window(500,500)
janela.set_title("Bolinha")

bola = Sprite("png/bola.png",1)
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

velX = 2
velY = 3

while True:
	
	#movimento automático do objeto
	bola.x = bola.x + velX
	bola.y = bola.y + velY
	
	#se a bola bater na moldura da janela a velocidade é invertida e ela faz o movimento contrário
	if (bola.x + bola.width >= janela.width) or (bola.x <= 0):
		velX *= (-1) 
	if (bola.y + bola.height >= janela.height) or (bola.y <= 0):
		velY *= (-1) 
	
	janela.set_background_color((219, 210, 81))
	
	bola.draw()

	janela.update()

    
