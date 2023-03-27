from math import dist
from comidaClass import Comida
import pygame


class Cobrinha:

    def __init__(self, headX, headY, vivo, pontos, velocidade, possuiControle):
        self.body = [[headX, headY]]
        self.vivo = vivo
        self.pontos = pontos
        self.velocidade = velocidade
        self.possuiControle = possuiControle

    def updatePlayer(self, janela, cor, Comida):
        self.lerTeclado()
        self.drawPlayer(janela, cor)
        self.comer(Comida)

    def updateOpponent(self, janela, cor, nextX, nextY):  # dúvida
        pass

    def drawPlayer(self, janela, cor):
        for n in range(len(self.body)):
            pygame.draw.rect(janela, cor, (self.body[n][0], self.body[n][1], 20, 20), 0)

    def lerTeclado(self):
        if self.possuiControle == True:
            seta = pygame.key.get_pressed()
            print(seta)
            posXAnt: int = 0
            posYAnt: int = 0

            if seta[pygame.K_LEFT]:
                if self.limitarPos(self.body[0][0] - self.velocidade, self.body[0][1]) == True:
                    self.updateTail()
                    self.body[0][0] -= 20

            if seta[pygame.K_RIGHT]:
                if self.limitarPos(self.body[0][0] + self.velocidade, self.body[0][1]) == True:
                    self.updateTail()
                    self.body[0][0] += 20

            if seta[pygame.K_UP]:
                if self.limitarPos(self.body[0][0], self.body[0][1] - self.velocidade) == True:
                    self.updateTail()
                    self.body[0][1] -= 20

            if seta[pygame.K_DOWN]:
                if self.limitarPos(self.body[0][0], self.body[0][1] + self.velocidade) == True:
                    self.updateTail()
                    self.body[0][1] += 20

    def updateTail(self):
        for n in range(len(self.body) - 1, 0, -1):
            posXAnt = self.body[n - 1][0]
            posYAnt = self.body[n - 1][1]
            self.body[n][0] = posXAnt
            self.body[n][1] = posYAnt

    def limitarPos(self, posX, posY):
        if posY < 200:
            return False
        if posY > 480:
            return False
        if posX < 150:
            return False
        if posX > 630:
            return False

        return True

    # Aumenta o corpo quando come um alimento.
    def crescer(self):
        posHead = self.body[0]
        self.body.append([posHead[0] + len(self.body) * 20, posHead[1]])

    def comer(self, Comida):
        colide = dist(self.body[0], Comida.posComida[0])
        if colide < 0.1:
            self.crescer()
            Comida.escolherPos()

