import pygame


class Cobrinha:
    def __init__(self, headX, headY, posHead: list, vida, pontos, velocidade):
        self.headX = headX
        self.headY = headY
        self.posHead = posHead
        self.vida = vida
        self.pontos = pontos
        self.velocidade = velocidade

    def updatePlayer(self, janela, cor):
        self.lerTeclado()
        self.limitarPos()
        self.drawPlayer(janela, cor)

    def drawPlayer(self, janela, cor):
        for n in range(len(self.posHead)):
            pygame.draw.rect(janela, cor, (self.posHead[n][0], self.posHead[n][1], 20, 20), 0)

    def lerTeclado(self):
        seta = pygame.key.get_pressed()
        if seta[pygame.K_LEFT]:
            self.headX -= self.velocidade
            self.posHead[0][0] -= self.velocidade
        if seta[pygame.K_RIGHT]:
            self.headX += self.velocidade
            self.posHead[0][0] += self.velocidade
        if seta[pygame.K_UP]:
            self.headY -= self.velocidade
            self.posHead[0][1] -= self.velocidade
        if seta[pygame.K_DOWN]:
            self.headY += self.velocidade
            self.posHead[0][1] += self.velocidade

    def limitarPos(self):
        if self.posHead[0][1] < 200:
            self.posHead[0][1] = 200
        if self.posHead[0][1] > 480:
            self.posHead[0][1] = 480
        if self.posHead[0][0] < 150:
            self.posHead[0][0] = 150
        if self.posHead[0][0] > 630:
            self.posHead[0][0] = 630

    # def comer

    # def crescer
