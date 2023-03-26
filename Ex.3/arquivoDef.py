import pygame

# Desenhar o grid do jogo em que as cobrinhas se movimentarao.
def grid(tam_bloco, tam_comprimento, tam_altura, janela_utilizada, cor):
    for x in range(0, tam_altura, tam_bloco):
        for y in range(0, tam_comprimento, tam_bloco):
            rect = pygame.Rect((x + 150), (y + 200), tam_bloco, tam_bloco)
            pygame.draw.rect(janela_utilizada, cor, rect, 0)

