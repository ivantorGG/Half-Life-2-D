import pygame
import random


width, height = 1000, 800
screen_rect = (0, 0, width, height)
screen = pygame.display.set_mode((width, height))


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, dx, dy, images, *groups):
        super().__init__(*groups)
        img = pygame.image.load(random.choice(images))
        self.image = pygame.transform.scale(img, (32, 52))
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = 1
        self.pos = pos

    def update(self, *args, **kwargs):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if self.rect.y - self.pos[1] > 80:
            self.kill()


def create_chips(position, type_of_object, *groups):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-5, 6)

    if type_of_object == 'FoodBox':
        for _ in range(particle_count):
            Particle(position, random.choice(numbers), random.choice(numbers),
                     ['images/food/box_chip1.png',
                      'images/food/box_chip2.png',
                      'images/food/box_chip1.png',
                      'images/food/box_chip4.png',
                      'images/food/box_chip5.png',
                      ], *groups)


if __name__ == '__main__':
    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                # создаём частицы по щелчку мыши
                create_chips(pygame.mouse.get_pos(), 'FoodBox', all_sprites)

        all_sprites.update()
        screen.fill((0, 0, 0))
        all_sprites.draw(screen)
        pygame.display.flip()
        clock.tick(50)

    pygame.quit()
