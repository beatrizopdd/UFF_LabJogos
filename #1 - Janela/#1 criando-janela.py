from PPlay.window import *

#nome-que-voce-quer-atribuir-a-janela = Window(largura,altura)
janela = Window(200,200)

#nome-atribuido.set_title("Nome que vai ficar na borda da janela")
janela.set_title("Janela")

#nome-atribuido.set_background_color((R,G,B))
janela.set_background_color((252, 248, 177))

while True:

    #swap de buffers (sei lá só sei que tava no kahoot)
    janela.update()
