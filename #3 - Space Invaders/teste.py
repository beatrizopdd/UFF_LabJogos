ranking = open("ranking_lista.txt", "r")
lista_ranking = ranking.readlines()

valores = []
for dados in lista_ranking:

	pontos = dados.split(" ")
	pontos.pop(2)
	valores.append(" ".join(pontos))

valores.sort()
print("valores: ", valores)
