from PPlay.window import *

#nome-que-voce-quer-atribuir-a-janela = Window(largura,altura)
janela = Window(200,200)

#nome-atribuido.set_title("Nome que vai ficar na borda da janela")
janela.set_title("Janela")

#nome-atribuido.set_background_color((R,G,B))
janela.set_background_color((252, 248, 177))

while True:

	#janela.draw_text("TEXTO", posição-horizontal, posição-vertical, tamanho, cor-em-RGB, "FONTE", negrito, itálico)
	janela.draw_text("Abc123#",0, janela.height / 2 - 45, 30, (0,0,0), "Arial", True, False)
	janela.draw_text("Abc123#",0, janela.height / 2 - 15, 30, (0,0,0), "Arial", False, False)
	janela.draw_text("Abc123#",0, janela.height / 2 + 15, 30, (0,0,0), "Arial", False, True)

    #swap de buffers (sei lá só sei que tava no kahoot)
	janela.update()
