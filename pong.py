from PPlay.window import*
from PPlay.sprite import*
from PPlay.animation import*
from PPlay.collision import*
from PPlay.keyboard import*

janela = Window(720,300)
janela.set_title("Ping-Pong")
janela.set_background_color((210,210,210))

controle = janela.get_keyboard()

bola = Sprite("png/bola.png",1)
bola.x = janela.width / 2 - bola.width / 2
bola.y = janela.height / 2 - bola.height / 2

pad = Sprite("png/raquete.png",1)
pad.x = 20
pad.y = janela.height / 2 - pad.height / 2

ia = Sprite("png/raquete.png",1)
ia.x = janela.width - 40
ia.y = janela.height / 2 - ia.height / 2

velIA = 5
velP = 4
bX = 3
bY = 3

erros = 0
acertos = 0

while True:
        
        bola.x += bX
        bola.y += bY

        if (controle.key_pressed("up")):
                pad.y -= velP
        elif (controle.key_pressed("down")):
                pad.y += velP

        #fisica da ia
        if (bola.x >= janela.width / 2) and (bY > 0):
                ia.y -= velIA
        if (bola.x >= janela.width / 2) and (bY < 0):
                ia.y += velIA
        if (bola.x <= janela.width / 2):
                ia.y += velIA
                #impede a ia de sair da tela
                if (ia.y <= 0) or (ia.y + ia.height >= janela.height):
                        velIA *= -1
                        
        #impede que o pad e a ia saiam da tela
        if (pad.y <= 0):
                pad.y = 0
        if (pad.y + pad.height >= janela.height):
                pad.y = janela.height - pad.height

        #impede que o pad saia da tela
        if (ia.y <= 0):
                ia.y = 0
        if (ia.y + ia.height >= janela.height):
                ia.y = janela.height - ia.height

        #impede que a bola saia da tela       
        if (bola.y + bola.height >= janela.height) or (bola.y <= 0):
                bY *= (-1)

        #define erros e acertos e devolve a bola pro jogo 
        if (bola.x + bola.width >= janela.width):
                acertos += 1
                bX *= -1
                bola.x = janela.width / 2 - bola.width / 2
                bola.y = janela.height / 2 - bola.height / 2
        if (bola.x <= 0):
                erros += 1
                bX *= -1
                bola.x = janela.width / 2 - bola.width / 2
                bola.y = janela.height / 2 - bola.height / 2

        #reação da bola ao entrar em contato com o pad
        if (bola.collided(pad)):
                bX *= (-1)
        if (bola.collided(ia)):
                bX *= (-1)

        janela.set_background_color((210,210,210))

        janela.draw_text("{} acertos".format(acertos), bola.width / 2, 25, 20, (0,0,0), "Arial", True, False)
        janela.draw_text("{} erros".format(erros),bola.width / 2, 50, 20, (0,0,0), "Arial", True, False)
        
        pad.draw()
        ia.draw()
        bola.draw()
        janela.update()
