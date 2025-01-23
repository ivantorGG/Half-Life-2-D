import pygame
from objects import CrushedCarChained


class Level(pygame.sprite.Sprite):
    def __init__(self, k_size, obj, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/objects/level1-off.png')
        self.image = pygame.transform.scale(self.image, (round(37 * 2 * k_size[0]), round(29 * 2 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))

        self.state = 'off'
        self.obj = obj
        self.k_size = k_size
        self.sound = pygame.mixer.Sound('sounds/level1-on.mp3')

    def switch(self):
        if self.state == 'off':
            self.sound.play()
            self.image = pygame.image.load('images/objects/level1-on.png')
            self.image = pygame.transform.scale(self.image, (round(32 * 2 * self.k_size[0]), round(26 * 2 * self.k_size[1])))
            self.rect = self.image.get_rect(center=(self.rect.centerx + 18 * self.k_size[0], self.rect.centery))
            self.state = 'on'
            self.obj.go = True
            return True
        return False


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
    level1 = Level(k_size, crushed_car, 300, 300, all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                level1.switch()

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        cloak.tick(FPS)
        pygame.display.flip()
