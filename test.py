from time import time
import pygame


class HEVCharger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.image = pygame.image.load('images/hev_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (117, 245))
        self.rect = self.image.get_rect()


class HEVChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.go = False
        self.j = 0
        self.image = pygame.image.load('images/hev_charger/for_animation.png')
        self.image = pygame.transform.scale(self.image, (13, 14))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(32, 94)
        self.move_direction = 'down'
        self.stop = False

    def update(self, *args, **kwargs):
        try:
            if time() - time_start_hev_charger_sound > 8:
                self.stop = True
        except NameError:
            pass
        self.j += 1
        if self.go and self.j % 2 == 0:
            if self.move_direction == 'down':
                self.rect = self.rect.move(0, 2)
                if self.rect.y == 122:
                    self.move_direction = 'up'
            else:
                self.rect = self.rect.move(0, -2)
                if self.rect.y == 94:
                    if self.stop:
                        self.go = False
                    self.move_direction = 'down'


class HealthCharger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.image = pygame.image.load('images/health_charger/charger.png')
        self.rect = self.image.get_rect().move(400, 20)


class HealthChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.go = False
        self.i = 0
        self.tmp = 0
        self.images = [
            'images/health_charger/for_animation.png',
            'images/health_charger/for_animation1.png',
            'images/health_charger/for_animation (1).png',
            'images/health_charger/for_animation (2).png',
            'images/health_charger/for_animation (3).png',
            'images/health_charger/for_animation (4).png',
            'images/health_charger/for_animation (5).png',
        ]
        self.image = pygame.image.load('images/health_charger/for_animation.png')
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(580, 246)

    def update(self, *args, **kwargs):
        try:
            if time() - time_start_health_charger_sound > 14:
                self.go = False
        except NameError:
            pass

        self.tmp += 1
        if self.go and self.tmp % 2 == 0:
            self.i += 1
            self.i %= 6
            self.image = pygame.image.load(self.images[self.i])
            self.rect = self.image.get_rect().move(580, 246)


pygame.init()
size = width, height = 850, 750
screen = pygame.display.set_mode(size)

FPS = 60
running = True
cloak = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

hev_charger = HEVCharger()
hev_charger_animaton_block = HEVChargerAnimationBlock()
health_charger = HealthCharger()
health_charger_animaton_block = HealthChargerAnimationBlock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(38, 309) and event.pos[1] in range(41, 695):
            pygame.mixer.music.load('sounds/hev_charger.mp3')
            pygame.mixer.music.play()
            hev_charger_animaton_block.go = True
            time_start_hev_charger_sound = time()
            hev_charger_animaton_block.stop = False

        elif event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(417, 791) and event.pos[1] in range(42,
                                                                                                                688):
            pygame.mixer.music.load('sounds/health_charger.mp3')
            pygame.mixer.music.play()
            health_charger_animaton_block.go = True
            time_start_health_charger_sound = time()

    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    cloak.tick(FPS)

pygame.quit()
