import pygame
import time

pygame.init()
window = pygame.display.set_mode((500, 500))
window.fill((255, 125, 125))
game = True
clock = pygame.time.Clock()
while game:
    clock.tick(60)
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            game = False
    pygame.display.update()
