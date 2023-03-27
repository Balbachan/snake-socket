import pygame
from random import randrange


class Comida:

    def __init__(self, posX, posY):
        self.posComida = [[posX, posY]]

    def escolherPos(self):
        coluna = randrange(200, 480, 20)
        linha = randrange(150, 630, 20)

        self.posComida[0][0] = linha
        self.posComida[0][1] = coluna

    def drawComida(self, janela, cor):
        pygame.draw.rect(janela, cor, (self.posComida[0][0], self.posComida[0][1], 20, 20), 0)

