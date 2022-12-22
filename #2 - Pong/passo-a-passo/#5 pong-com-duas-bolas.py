from PPlay.window import*
from PPlay.sprite import*
from PPlay.collision import*
from PPlay.keyboard import*

janela = Window(720,500)
janela.set_title("Ping-Pong de IA")

controle = janela.get_keyboard()

#criação dos pads esquerdo e da ia respectivamente
pad = Sprite("png/raquete.png",1)
pad.x = pad.width + 50
pad.y = janela.height / 2 - pad.height / 2

pad2 = Sprite("png/raquete.png",1)
pad2.x = janela.width - pad.width - 50
pad2.y = janela.height / 2 - pad2.height / 2

velP = 300
velIA = 350

#criação das bolas
bola = Sprite("png/bola.png",1)
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

bola2 = Sprite("png/bola2.png",1)

bX = 300
bY = 400
bXX = -300
bYY = 400

#pontuação de cada pad
esquerda = 0
direita = 0
rebatida = 0

while True:
        
        bola.x += bX * janela.delta_time()
        bola.y += bY * janela.delta_time()
        
        if (controle.key_pressed("up")):
                pad.y -= velP * janela.delta_time()
        if (controle.key_pressed("down")):
                pad.y += velP * janela.delta_time()                
  
        #o movimento da ia tve que entrar no if pra controlar qual bola ela vai seguir
				       
        if (pad.y <= 0):
                pad.y = 0
        if (pad.y + pad.height >= janela.height):
                pad.y = janela.height - pad.height
        if (pad2.y <= 0):
                pad2.y = 0
        if (pad2.y + pad2.height >= janela.height):
                pad2.y = janela.height - pad2.height
                
        if (bola.y <= 0):
                bola.y = 0
                bY *= (-1) 
        if (bola.y + bola.height >= janela.height):
                bola.y = janela.height - bola.height
                bY *= (-1)
		
        #define a pontuação do jogador 
        if (bola.x + bola.width >= janela.width):
                esquerda += 1
                bX *= -1
                bola.x = janela.width / 2 - bola.width / 2
                bola.y = janela.height / 2 - bola.height / 2
        if (bola.x <= 0):
                direita += 1
                bX *= -1
                bola.x = janela.width / 2 - bola.width / 2
                bola.y = janela.height / 2 - bola.height / 2
	
        #reação da bola ao entrar em contato com os pads
        if (pad.collided(bola)):
                bX *= (-1)
                bola.x = pad.x + pad.width
                rebatida += 1
        if (pad2.collided(bola)):
                bX *= (-1)
                bola.x = pad2.x - bola.width
                rebatida += 1

        #acréscimo de bola
        if (rebatida < 3):
                bola2.x = -bola2.width
                bola2.y = 0
		#movimento da ia
                if (bola.x >= janela.width / 2 and bola.y >= janela.height / 2 and bY > 0):
                        pad2.y += velIA * janela.delta_time()
                if (bola.x >= janela.width / 2 and bola.y <= janela.height / 2 and bY < 0):
                        pad2.y -= velIA * janela.delta_time()

        if (rebatida == 3):
                bola2.x = janela.width / 2 - bola.width / 2
                bola2.y = janela.height / 2 - bola.height / 2
                rebatida += 1

        if (rebatida >= 3):
                bola2.x += bXX * janela.delta_time()
                bola2.y += bYY * janela.delta_time()

                #bola extra não sai da tela no eixo Y
                if (bola2.y <= 0):
                        bola2.y = 0
                        bYY *= (-1)
                if (bola2.y + bola2.height >= janela.height):
                        bola2.y = janela.height - bola2.height
                        bYY *= (-1)
                                
                #bola extra some depois de sair no eixo X + pontuação
                if (bola2.x + bola2.width >= janela.width):
                        esquerda += 1
                        rebatida = 0
                if (bola2.x <= 0):
                        direita += 1
                        rebatida = 0

                #reação da bola ao entrar em contato com os pads
                if (pad.collided(bola2)):
                        bXX *= (-1)
                        bola2.x = pad.x + pad.width
                if (pad2.collided(bola2)):
                        bXX *= (-1)
                        bola2.x = pad2.x - bola2.width

                #movimento da ia (dando um desconto por ser muito trabalho) posso deixar ela mais espertinha
                if (bola.x >= bola2.x):
                        if (bola.x >= janela.width / 2 and bY > 0):
                                pad2.y += velIA * janela.delta_time()
                        if (bola.x >= janela.width / 2 and bY < 0):
                                pad2.y -= velIA * janela.delta_time()
                if (bola.x < bola2.x):
                        if (bola2.x >= janela.width / 2 and bYY > 0):
                                pad2.y += velIA * janela.delta_time()
                        if (bola2.x >= janela.width / 2 and bYY < 0):
                                pad2.y -= velIA * janela.delta_time()

        #fim dos comandos aqui é só atualização
        janela.set_background_color((219, 210, 81))

        janela.draw_text("{} você x {} computador".format(esquerda,direita), janela.width / 2 - 100, 30, 20, (94, 44, 14), "Arial", True, False)

        pad.draw()
        pad2.draw()
        bola.draw()
        if (rebatida >= 3):
                bola2.draw()

        janela.update()
