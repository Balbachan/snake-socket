"""
Faculdade Prebisteriana Mackenzie
Ciência da Computação (FCI)
Redes
Prof. Bruno Rodrigues

Batalha de Snake
Turma 05G
Alunos:
    - Laura C. Balbachan dos Santos (32173008)
    - Matheus Farias ()
"""
from cobrinhaClass import Cobrinha
import arquivoDef
import pygame
import socket

JANELA_HEIGHT: int = 600
JANELA_WIDTH: int = 800
JOGO_HEIGHT: int = 300
JOGO_WIDTH: int = 500
TAM_BLOCO: int = 20

PRETO = (0, 0, 0)
BRANCO = (250, 250, 250)
CVERDE = (120, 156, 103)
EVERDE = (155, 176, 142)
CINZA = (34, 37, 46)

pygame.init()

janela = pygame.display.set_mode([JANELA_WIDTH, JANELA_HEIGHT])
player = Cobrinha(150, 200, [[150, 200]], 1, 1, 20)

executando = True
while executando:
    pygame.time.delay(100)  # simula FPS
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            executando = False

    janela.fill(EVERDE)

    fonte = pygame.font.Font("nokiafc22.ttf", 20)
    texto_title = fonte.render("Batalha das Snake", True, CINZA)
    janela.blit(texto_title, (290, 110))

    arquivoDef.grid(TAM_BLOCO, JOGO_HEIGHT, JOGO_WIDTH, janela, CVERDE)
    contorno = pygame.draw.rect(janela, CINZA, (146, 196, 508, 308), 4)

    player.updatePlayer(janela, BRANCO)

    pygame.display.update()

pygame.quit()
