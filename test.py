# TODO: Optimise code(hard)
from time import time
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.image = pygame.Surface((30, 50))
        pygame.draw.rect(self.image, (0, 255, 0), (0, 0, 30, 50))
        self.rect = pygame.Rect(300, 300, 30, 50)

    def move_player(self, plus_x, plus_y):
        self.rect = self.rect.move(plus_x, plus_y)


class HEVCharger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.image = pygame.image.load('images/hev_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (117, 245))
        self.rect = self.image.get_rect().move(50, 250)


class HEVChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.go = False
        self.j = 0
        self.image = pygame.image.load('images/hev_charger/for_animation.png')
        self.image = pygame.transform.scale(self.image, (13, 14))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(32 + 50, 94 + 250)
        self.move_direction = 'down'

    def update(self, *args, **kwargs):
        try:
            if time() - time_start_hev_charger_sound > 8:
                self.go = False
        except NameError:
            pass

        self.j += 1
        if self.go and self.j % 2 == 0:
            if self.move_direction == 'down':
                self.rect = self.rect.move(0, 2)
                if self.rect.y >= 376:
                    self.move_direction = 'up'
            else:
                self.rect = self.rect.move(0, -2)
                if self.rect.y <= 344:
                    self.move_direction = 'down'


class HealthCharger(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.add(all_sprites)
        self.image = pygame.image.load('images/health_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (416 // 3, 687 // 3))
        self.rect = self.image.get_rect().move(200, 300)


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
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(260, 374)

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
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect().move(260, 374)


pygame.init()
pygame.mixer.init()
size = width, height = 850, 750
screen = pygame.display.set_mode(size)

FPS = 60
running = True
cloak = pygame.time.Clock()

all_sprites = pygame.sprite.Group()

hev_charger = HEVCharger()
hev_charger_animaton_block = HEVChargerAnimationBlock()
hev_charging_sound = pygame.mixer.Sound('sounds/hev_charger.mp3')

health_charger = HealthCharger()
health_charger_animaton_block = HealthChargerAnimationBlock()
health_charging_sound = pygame.mixer.Sound('sounds/health_charger.mp3')

player = Player()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_player(15, 0)

            if event.key == pygame.K_a:
                player.move_player(-15, 0)

            if event.key == pygame.K_w:
                player.move_player(0, -15)

            if event.key == pygame.K_s:
                player.move_player(0, 15)

            if event.key == pygame.K_e:
                if player.rect.centerx in range(hev_charger.rect.centerx - 80, hev_charger.rect.centerx + 80) and \
                        player.rect.centery in range(hev_charger.rect.centery - 150, hev_charger.rect.centery + 150):
                    if not hev_charger_animaton_block.go:
                        hev_charging_sound.play()
                        hev_charger_animaton_block.go = True
                        time_start_hev_charger_sound = time()

                if player.rect.centerx in range(health_charger.rect.centerx - 80,
                                                health_charger.rect.centerx + 80) and \
                        player.rect.centery in range(health_charger.rect.centery - 120,
                                                     health_charger.rect.centery + 120):
                    if not health_charger_animaton_block.go:
                        health_charging_sound.play()
                        health_charger_animaton_block.go = True
                        time_start_health_charger_sound = time()

    screen.fill((0, 0, 0))
    all_sprites.update()
    all_sprites.draw(screen)
    pygame.display.flip()
    cloak.tick(FPS)

pygame.quit()
