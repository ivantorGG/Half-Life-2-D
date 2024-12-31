# меня преследует эта проблема с поворотами ☠️
import pygame


pygame.init()
size = width, height = 201, 201

screen = pygame.display.set_mode(size)

screen2 = pygame.Surface(screen.get_size())
pygame.draw.circle(screen2, (255, 255, 255), (100, 100), 10)
pygame.draw.polygon(screen2, (255, 255, 255), ((100, 100), (82, 30), (118, 30)))
pygame.draw.polygon(screen2, (255, 255, 255), ((100, 100), (171, 121), (150, 150)))
pygame.draw.polygon(screen2, (255, 255, 255), ((100, 100), (31, 121), (52, 150)))
screen.blit(screen2, (0, 0))

FPS = 100
running = True
angle = 0
plus_angle = 0
cloak = pygame.time.Clock()
ROTATEVENTEVENT = pygame.USEREVENT + 1
pygame.time.set_timer(ROTATEVENTEVENT, 50)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                plus_angle += 5
            if event.button == 3:
                plus_angle -= 5
        if event.type == ROTATEVENTEVENT:
            angle += plus_angle
            angle %= 360
            screen.blit(pygame.transform.rotate(screen2, angle), (0, 0))

    pygame.display.flip()
    cloak.tick(FPS)


pygame.quit()
