import pygame


class CrushedCarChained(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, length, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/objects/crushed_car.png')
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * 2 * k_size[0]), round(self.image.get_height() * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.mask = pygame.mask.from_surface(self.image)

        self.go = False
        self.animation_done = False
        self.k_size = k_size
        self.length = length * k_size[0]
        self.car = None

    def update(self, *args, **kwargs):
        if self.go and self.length > 0:
            self.length -= 10
            self.rect.y += 10
        if self.length <= 0 and self.go:
            self.animation_done = True
            self.go = False
        if self.animation_done:
            self.car = CrushedCar(self.k_size, self.rect.centerx,
                                  self.rect.centery + 573 * self.k_size[1], *self.groups())
            self.animation_done = False
            self.mask = None


class CrushedCar(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/objects/crushed_car2.png')
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * 2 * k_size[0]), round(self.image.get_height() * k_size[1])))
        self.rect = self.image.get_rect(
            center=(x, y))
        self.mask = pygame.mask.from_surface(self.image)


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 850, 750
    screen = pygame.display.set_mode(size)
    k_size = (1, 1)

    FPS = 60
    running = True
    cloak = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()
    crushed_car = CrushedCarChained(k_size, 200, 200, all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        cloak.tick(FPS)
        pygame.display.flip()
