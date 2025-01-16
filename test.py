import pygame
import random

pygame.init()

size = width, height = (700, 700)
screen = pygame.display.set_mode(size)
all_sprites = pygame.sprite.Group()

screen_rect = (0, 0, width, height)


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [pygame.image.load("images/gordon/animation_run_right1.png")]
    colorkey = fire[0].get_at((0, 0))
    fire[0].set_colorkey(colorkey)
    for scale in (5, 10, 20):
        x = pygame.transform.scale(fire[0], (scale, scale))
        colorkey = x.get_at((0, 0))
        x.set_colorkey(colorkey)
        fire.append(x)

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = random.choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 1

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)
    for _ in range(particle_count):
        Particle(position, random.choice(numbers), random.choice(numbers))


clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            # создаём частицы по щелчку мыши
            create_particles(pygame.mouse.get_pos())

    all_sprites.update()
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(50)

pygame.quit()
