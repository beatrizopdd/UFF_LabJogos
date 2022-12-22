from PPlay.window import*
from PPlay.sprite import*

from atalho import* 

def input_ranking(pontos):

	janela = Window(537,457)
	janela.set_title("Game Over")
	
	ranking = open("ranking_lista.txt", "a")
	nome_player = "Nenhum"
	
	while (nome_player == "Nenhum"):

		nome_player = str(input("Digite seu nome: "))
		ranking.write("{:.0f} {} \n".format(int(pontos), nome_player))
		ranking.close()
		
		if (nome_player != "Nenhum"):
			return None
		
		janela.update()

def ordena_ranking():

	ranking = open("ranking_lista.txt", "r")
	lista_ranking = ranking.readlines()

	valores = []
	for dados in lista_ranking:

		pontos = dados.split(" ")
		pontos.pop(2)
		valores.append(" ".join(pontos))

	valores.sort()
	
	top5 = []
	for i in range(len(valores) - 1, len(valores) - 6, -1):
		top5.append(valores[i])
	
	return top5
	

def mostrar_ranking():

	janela = Window(537,457)
	janela.set_title("Ranking")

	fundo = Sprite("png/ranking_lista.png", 1)
	fundo.x = 0
	fundo.y = 0

	tecla = janela.get_keyboard()
	m_ficar = True
	
	top5 = ordena_ranking()
	
	while (m_ficar == True):

		m_ficar = sair()

		fundo.draw()

		janela.draw_text("#1 {}".format(top5[0]), 125, 150, 35, (15,235,36), "Arial")
		janela.draw_text("#2 {}".format(top5[1]), 125, 200, 35, (15,235,36), "Arial")
		janela.draw_text("#3 {}".format(top5[2]), 125, 250, 35, (15,235,36), "Arial")
		janela.draw_text("#4 {}".format(top5[3]), 125, 300, 35, (15,235,36), "Arial")
		janela.draw_text("#5 {}".format(top5[4]), 125, 350, 35, (15,235,36), "Arial")
		
		janela.update()
