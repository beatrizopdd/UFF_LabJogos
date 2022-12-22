<h2 align="center"> :desktop_computer: JANELA :desktop_computer: </h2>

- `(Aula 2) criando-janela.py:` Aqui você aprende o básico do básico: criar-janela-verde.aula2;

- `:bomb: texto-na-janela.py:` Como colocar um texto na janela (sério não precisava de legenda);
OBS.: Aparentemente esse querido arrasa com o fps do seu jogo então use com moderação.

- `:bomb: criando-boneco.py:` Criando e posicionando um boneco na tela;

- `:bomb: movendo-boneco-teclado.py:` Movimentando o boneco pela tela com o teclado e respeitando os limites da moldura;

- `:bomb: movendo-boneco-mouse.py:` Movimentando o boneco pela tela com o mouse e respeitando os limites da moldura;


<h2 align="center"> :ping_pong: PONG :ping_pong: </h2>

- `(Aula 3) fisica-da-bolinha.py:` Como criar uma bolinha que anda sozinha pela janela e respeita os limites da moldura;
OBS.: Vou começar a usar Sprite("png/bola.png",1) e esse 'png/' é a pasta que armazena a foto. Quer menos complicação? Deixa o png no mesmo lugar que o arquivo.

- `(Aula 4) fisica-da-bolinha-2.py:` Vou ser bem honesta: não faço ideia do por quê desse troço de delta_time mas consegui fazer e é isso que importa;

- `(Aula 4) pong-dois-jogadores.py:` Um pong de dois jogadores. PORÉM consegui arrumar o bug do pad possuído;

- `(Aula 5) pong-com-ia.py:` Agora o usuário pode jogar sozinho e ainda ter um adversário;

- `(Aula 5) pong-com-duas-bolas.py:` Esse é o exercício surpresa. Quando a bola bate 3 vezes num pad aparece uma nova bola;

Cada exercício de aula ta num arquivo separado como um jogo independente, PORÉM eu fiz um arquivo com menu e etc, dividido em módulos etc, pra rodar é só abrir o "menu.py".


<h2 align="center"> :space_invader: SPACE-INVADERS :space_invader: </h2>

- `(Aula 6) menu.py:` Um menu com botões clicáveis de JOGAR, DIFICULDADE, RANKING, SAIR e implementação do "esc pra sair";

- `(Aula 7) player:` Nave anda de um lado pro outro e solta um tiro quando o espaço ta pressionado (o tiro sobe pela tela e é limitado a um por vez);

- `(Aula 8) monstros pt1:` Criação de vários tiros em uma lista (e remoção) e desenhar uma matriz estática de monstros;

- `(Aula 9) monstros pt2:` Movimentação dos monstros ainda sem dano pelo tiro;

- `(Aula 10) monstros pt3:` Monstros danificados pelo tiro do player;

- `(Aula 11) monstros pt4:` Monstros aleatórios atirando no player, danos a nave e gameover;

- `(Aula 12) ranking:` Cria uma nova horda de aliens quando a antiga acaba e, caso gameover, pede o nome do usuário para salvar a pontuação;

- `(Aula 13) exercício surpresa:` Vai ter um infiltrado no meio da horda que aguenta 3 tiros até voltar a ser um alien normal. A sprite tem que ser diferente.
OBS.: O jogo ta cheio de bug? Claro que sim, mas o jeito que eu consegui diferenciar o boss dos aliens normais pra mim foi genial.

#### atalho.py (linha)

- :bomb: Posicionar os botôes do menu (8);
- :bomb: Esc pra sair (16);
- :bomb: Cria nova horda (25);
- :bomb: Limita a horda (46);
- :bomb: Movimenta a horda (61);
- :bomb: Cria um disparo da nave (75);
- :bomb: Limita o disparo da nave (89);
- :bomb: Descobre o tamanho da matriz no espaço (99);
- :bomb: Acerto do disparo da nave na matriz (119);
- :bomb: Cria um disparo do alien (158);
- :bomb: Limita o disparo do alien (172);
- :bomb: Acerto do disparo do alien na nave (183);

#### dificuldade.py

É um menu pro usuário escolher o "ritmo" do jogo.

#### ranking.py

Isso aqui ta radioativo mas se você quiser um exemplo do que NÃO fazer...

- :bomb: input_ranking ta funcionando direitinho, pode usar;
- :bomb: ordena_ranking NÃO;
- :bomb: mostrar_ranking ta esse aqui também ta funcionando bonitinho;

OBS: Uma turma tinha que ordenar as 5  melhores pontuações e a outra só precisava dos últimos 5 jogadores. De qual turma a otária aqui era? Pois é...

#### jogar.py

Ta tudo comentadinho, se vira aí. 

## :radioactive: Se você encontrar um computador com pygame, meus parabéns!

Mas você não vai.

- `INSTALAR PYGAME:` python3 -m pip install -U pygame --user
- `PPLAY:` http://www2.ic.uff.br/pplay/download/
- `RODAR O JOGO:` Abre a pasta do jogo -> Botão direito "abrir terminal aqui" -> Digita "python3 nome-do-arquivo.py"



| Emoji | Legenda |
| :---: | :---: |
| :bomb: | fiz por conta própria |

