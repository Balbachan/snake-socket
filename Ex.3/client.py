"""
Universidade Prebisteriana Mackenzie
Faculdade de Computacao e Informatica (FCI)
Ciência da Computação
Redes de Computadores
Prof. Bruno Rodrigues

Batalha de Snakes
Turma 05G
Alunos:
    - Laura C. Balbachan dos Santos (32173008)
    - Matheus Farias de Oliveira Matsumoto (32138271)
"""
from cobrinhaClass import Cobrinha
from comidaClass import Comida
from network import Network
import arquivoDef
import pygame
import socket


# Ler a posicao da cobrinha.
def read_pos(str):
    str = str.split(",")
    return int(str[0]), int(str[1])


# Definir a posicao da cobrinha.
def make_pos(tup):
    return str(tup[0]) + "," + str(tup[1])


def main():
    # Definicao da janela.
    JANELA_HEIGHT: int = 600
    JANELA_WIDTH: int = 800
    JOGO_HEIGHT: int = 300
    JOGO_WIDTH: int = 500
    TAM_BLOCO: int = 20

    # Definicao das cores.
    PRETO = (0, 0, 0)
    BRANCO = (250, 250, 250)
    CVERDE = (120, 156, 103)
    EVERDE = (155, 176, 142)
    CINZA = (34, 37, 46)
    VERMELHO = (182, 45, 87)
    COBRA1 = (67, 82, 61)
    COBRA2 = (199, 240, 216)

    pygame.init()

    n = Network()
    startPos = read_pos(n.getPos())
    janela = pygame.display.set_mode([JANELA_WIDTH, JANELA_HEIGHT])  # Criar tela.
    player = Cobrinha(startPos[0], startPos[1], True, 0, TAM_BLOCO, True)  # Criar player 1. startPos[0], startPos[1]
    opponent = Cobrinha(500, 480, True, 0, TAM_BLOCO, False)  # Criar player 2.
    comida = Comida(0, 0)  # Cria comidinha
    comida.escolherPos()  # Randomiza a localização da comidinha
    clientNumber = 0  # Numero de Clientes

    # Loop de execucao.
    executando = True
    while executando:

        pygame.time.delay(80)  # simula FPS
        opponent2Pos = read_pos(n.send(make_pos((player.body[0][0], player.body[0][1]))))

        # Capturar eventos.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                executando = False

        # Definir configuracoes de tela.
        janela.fill(EVERDE)
        fonte = pygame.font.Font("nokiafc22.ttf", 20)
        texto_title = fonte.render("Batalha das Snakes", True, CINZA)
        janela.blit(texto_title, (290, 110))
        arquivoDef.grid(TAM_BLOCO, JOGO_HEIGHT, JOGO_WIDTH, janela, CVERDE)
        contorno = pygame.draw.rect(janela, CINZA, (146, 196, 508, 308), 4)

        # Desenhar jogadores.
        player.updatePlayer(janela, COBRA1, comida)
        opponent.updateOpponent(janela, COBRA2, opponent2Pos[0], opponent2Pos[1])
        player.bateCobra(opponent)

        # Desenhar comida
        comida.drawComida(janela, VERMELHO)

        # Atualizar tela.
        pygame.display.update()

    pygame.quit()


main()
