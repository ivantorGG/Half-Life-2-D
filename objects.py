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


class GameLevel(pygame.sprite.Sprite):
    def __init__(self, k_size, img, portal1_xy, portal2_xy, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * k_size[0]), round(self.image.get_height() * k_size[1])))
        self.rect = self.image.get_rect(center=(300, -170))
        self.start_portal = Portal(k_size, portal1_xy[0], portal1_xy[1], True, *self.groups())
        self.end_portal = Portal(k_size, portal2_xy[0], portal2_xy[1], True, *self.groups())

        self.completed = False

    def update(self, *args, **kwargs):
        pass
        # try:
        #     if self.start_portal.is_done:
        #         del self.start_portal
        # except NameError:
        #     pass
        # try:
        #     if self.end_portal.is_done:
        #         del self.end_portal
        # except NameError:
        #     self.completed = True


class Portal(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, is_first, *groups):
        pass
        # super().__init__(*groups)
        #
        # if is_first:
        #     self.phase = 'starting'
        #     self.counting_i = 0
        #     self.counting_max = 3
        #     self.color = 'green'
        # else:
        #     self.phase = 'waiting'
        #     self.color = 'purple'
        #
        # self.is_first = is_first
        # self.is_done = False
        #
        # self.starting_images = [...]
        # self.waiting_images = [...]
        # self.closing_images = [...]
        #
        # self.i = 0
        # self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
        # self.image = pygame.transform.scale(self.image, (
        #     round(50 * k_size[0]), round(100 * k_size[1])))
        # self.rect = self.image.get_rect(center=(x, y))

    def update(self, *args, **kwargs):
        pass
        # if self.phase == 'starting':
        #     self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
        #     self.image = pygame.transform.scale(self.image, (
        #         round(50 * k_size[0]), round(100 * k_size[1])))
        #     self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))
        #     self.i += 1
        #     if self.i is ...:
        #         self.i = 0
        #         self.phase = 'waiting'
        #
        # if self.phase == 'waiting':
        #     self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
        #     self.image = pygame.transform.scale(self.image, (
        #         round(50 * k_size[0]), round(100 * k_size[1])))
        #     self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))
        #     self.i += 1
        #
        #     if self.i is ...:
        #         self.i = 0
        #         if self.is_first:
        #             self.counting_i += 1
        #
        #     if self.counting_i == self.counting_max:
        #         self.phase = 'closing'
        #
        # if self.phase == 'closing':
        #     self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
        #     self.image = pygame.transform.scale(self.image, (
        #         round(50 * k_size[0]), round(100 * k_size[1])))
        #     self.rect = self.image.get_rect(center=(self.rect.x, self.rect.y))
        #     self.i += 1
        #     if self.i is ...:
        #         self.i = 0
        #         self.is_done = True
        #         self.kill()


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
