from PPlay.window import*
from PPlay.sprite import*
from PPlay.keyboard import*
from PPlay.collision import*

from atalhos import*

def jogo_dj():

        janela = Window(720,400)
        janela.set_title("Ping-Pong")

        controle = janela.get_keyboard()

        #criação dos pads esquerdo e direito respectivamente
        pad = Sprite("png/raquete.png",1)
        pad.x = pad.width * 2
        pad.y = janela.height / 2 - pad.height / 2

        pad2 = Sprite("png/raquete.png",1)
        pad2.x = janela.width - pad.width * 3
        pad2.y = janela.height / 2 - pad2.height / 2

        velP = 200

        bola = Sprite("png/bola.png",1)
        bola.x = janela.width / 2 - bola.width / 2
        bola.y = janela.height / 2 - bola.height / 2
        velBX = 300
        velBY = 300

        bolaE = Sprite("png/bola2.png",1)
        bolaE.x -= bolaE.width
        velBEX = 300
        velBEY = 300

        rebatidas = 0

        #pontuação de cada pad
        esquerda = 0
        direita = 0
	
        ficar = True

        while (ficar == True):

                ficar = sair(controle)

                velBX, velBY, rebatidas = controle_bola(bola, velBX, velBY, rebatidas, pad, pad2, janela)

                controle_pad("e", pad, velP, controle, janela)
                controle_pad("d", pad2, velP, controle, janela)

                #acréscimo de bola
                if (rebatidas < 3):
                        bolaE.x -= bolaE.width
                        esquerda, direita, velBX, rebatidas = pontuacao(bola, velBX, pad, pad2, esquerda, direita, janela, rebatidas)

                if (rebatidas == 3):
                        bolaE.x = (janela.width - bolaE.width) / 2
                        bolaE.y = (janela.height - bolaE.height) / 2
                        rebatidas += 1

                if (rebatidas >= 3):
                
                        velBEX, velBEY, rebatidas = controle_bola(bolaE, velBEX, velBEY, rebatidas, pad, pad2, janela)

                        esquerda, direita, velBX, rebatidas = pontuacao(bola, velBX, pad, pad2, esquerda, direita, janela, rebatidas)
                        esquerda, direita, velBEX, rebatidas = pontuacao(bolaE, velBEX, pad, pad2, esquerda, direita, janela, rebatidas, True)

                janela.set_background_color((219, 210, 81))
                                
                janela.draw_text("{} esquerda x {} direita".format(esquerda, direita), janela.width / 2 - 120, 30, 20, (94, 44, 14), "Arial", True, False)

                pad.draw()
                pad2.draw()

                bola.draw()
                bolaE.draw()

                janela.update()
                
                
