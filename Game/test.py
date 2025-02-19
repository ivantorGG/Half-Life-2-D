import pygame


def draw_circle(screen, xy, radius):
    screen.fill((0, 0, 255))
    pygame.draw.circle(screen, (255, 255, 0), xy, radius)


pygame.init()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
radius = 0
circle_start_grow = False
curr_pos = None
FPS = 10
running = True
cloak = pygame.time.Clock()

while running:


    pygame.display.flip()
    cloak.tick(FPS)


pygame.quit()
