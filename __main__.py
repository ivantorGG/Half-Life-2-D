import pygame


pygame.init()
size = width, height = 1500, 800

screen = pygame.display.set_mode(size)

FPS = 60
running = True
cloak = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()
    cloak.tick(FPS)

pygame.quit()
