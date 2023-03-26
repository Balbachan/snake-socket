import pygame

class Cobrinha:
    
    def __init__(self, headX, headY, vivo, pontos, velocidade, direcao):
        self.body = [[headX, headY], [headX+20, headY], [headX+40, headY]]
        self.vivo = vivo
        self.pontos = pontos
        self.velocidade = velocidade
        self.direcao = direcao

    def updatePlayer(self, janela, cor):
        self.lerTeclado()
        self.drawPlayer(janela, cor)

    def drawPlayer(self, janela, cor):
        for n in range(len(self.body)):
            pygame.draw.rect(janela, cor, (self.body[n][0], self.body[n][1], 20, 20), 0)

    def lerTeclado(self):
        seta = pygame.key.get_pressed()
        posXAnt: int = 0
        posYAnt: int = 0
        
        if seta[pygame.K_LEFT]:
            if self.limitarPos(self.body[0][0] - self.velocidade, self.body[0][1]) == True:
                for n in range(len(self.body)-1, 0, -1):
                    posXAnt = self.body[n-1][0]
                    posYAnt = self.body[n-1][1]
                    self.body[n][0] = posXAnt
                    self.body[n][1] = posYAnt
                self.body[0][0] -= self.velocidade
        
        if seta[pygame.K_RIGHT]:
            if self.limitarPos(self.body[0][0] + self.velocidade, self.body[0][1]) == True:
                for n in range(len(self.body)-1, 0, -1):
                    posXAnt = self.body[n-1][0]
                    posYAnt = self.body[n-1][1]
                    self.body[n][0] = posXAnt
                    self.body[n][1] = posYAnt
                self.body[0][0] += self.velocidade
        
        if seta[pygame.K_UP]:
            if self.limitarPos(self.body[0][0], self.body[0][1] - self.velocidade) == True:
                for n in range(len(self.body)-1, 0, -1):
                    posXAnt = self.body[n-1][0]
                    posYAnt = self.body[n-1][1]
                    self.body[n][0] = posXAnt
                    self.body[n][1] = posYAnt
                self.body[0][1] -= self.velocidade
        
        if seta[pygame.K_DOWN]:
            if self.limitarPos(self.body[0][0], self.body[0][1] + self.velocidade) == True:
                for n in range(len(self.body)-1, 0, -1):
                    posXAnt = self.body[n-1][0]
                    posYAnt = self.body[n-1][1]
                    self.body[n][0] = posXAnt
                    self.body[n][1] = posYAnt
                self.body[0][1] += self.velocidade


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
    def comer(self):
        
        ultimoMembro = self.body[-1]
        
        if self.direcao == "UP":
            ultimoMembro[1] += self.velocidade
            self.body.append(ultimoMembro)
    
    # def crescer
