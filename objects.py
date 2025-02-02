import pygame

from player import Player


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
                                  self.rect.y + 573 * self.k_size[1], *self.groups())
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
    def __init__(self, k_size, img, portal1, portal2, obj_groups, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load(img)
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * k_size[0]), round(self.image.get_height() * k_size[1])))
        self.rect = self.image.get_rect(center=(300 * k_size[0], -265 * k_size[1]))
        self.start_portal = Portal(k_size, portal1[0], portal1[1], True, portal1[2], *obj_groups, *self.groups())
        self.end_portal = Portal(k_size, portal2[0], portal2[1], False, portal2[2], *obj_groups, *self.groups())

        self.completed = False

    def update(self, *args, **kwargs):
        try:
            if self.start_portal.is_done:
                del self.start_portal
        except AttributeError:
            pass
        try:
            if self.end_portal.is_done:
                del self.end_portal
        except AttributeError:
            self.completed = True


class Portal(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, is_first, color, obj_groups, *groups):
        pass
        super().__init__(*groups)

        if is_first:
            self.phase = 'starting'
        else:
            self.phase = 'waiting'

        self.color = color

        self.is_first = is_first
        self.is_done = False
        self.k_size = k_size
        self.obj_groups = obj_groups

        self.i = 1
        self.counting_i = 0
        self.counting_max = 3
        self.for_slower = 0

        self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_width() * 6 * self.k_size[0]), round(self.image.get_height() * 6 * self.k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        start_snd = pygame.mixer.Sound('sounds/teleport_entering.mp3')
        start_snd.play()

    def update(self, *args, **kwargs):
        self.for_slower += 1
        if self.for_slower % 2 == 0:
            if self.phase == 'starting':
                self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 6 * self.k_size[0]),
                    round(self.image.get_height() * 6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.i += 1
                if self.i == 8:
                    self.i = 1
                    self.phase = 'waiting'

            if self.phase == 'waiting':
                self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 6 * self.k_size[0]),
                    round(self.image.get_height() * 6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.i += 1

                if self.i == 8:
                    self.i = 1
                    if self.is_first:
                        self.counting_i += 1

                if self.counting_i == self.counting_max:
                    self.phase = 'ending'

            if self.phase == 'ending':
                self.image = pygame.image.load(f'images/levels/portal/{self.color}/{self.phase}/{self.i}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 6 * self.k_size[0]),
                    round(self.image.get_height() * 6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.i += 1
                if self.i == 6:
                    self.i = 1
                    self.is_done = True
                    close_snd = pygame.mixer.Sound('sounds/teleport_closing.mp3')
                    close_snd.play()
                    self.kill()
        if self.phase != 'ending' and isinstance(pygame.sprite.spritecollideany(self, self.obj_groups),
                                                 Player) and not self.is_first:
            self.phase = 'ending'
            self.i = 1


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
