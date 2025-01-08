# !!! MAIN CLASSES: HEVCharger, HealthCharger !!!

from time import time
from player import Player
import pygame


class HEVChargerBox(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        """При инициализации указывать координаты и группы спрайтов"""
        super().__init__(*groups)

        self.image = pygame.image.load('images/hev_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (117, 245))
        self.rect = self.image.get_rect()

        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)  # двигаю тело зарядника по x и y


class HEVChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self, chargerx, chargery, *groups):
        """При инициализации указывать координаты тела зарядника и группы спрайтов"""
        super().__init__(*groups)

        self.chargerx = chargerx  # х тела
        self.chargery = chargery  # у тела

        self.sound = pygame.mixer.Sound('sounds/hev_charger.mp3')  # звук
        self.time_start_hev_charger_sound = None  # время начала проигрывания звука

        self.image = pygame.image.load('images/hev_charger/for_animation.png')
        self.image = pygame.transform.scale(self.image, (13, 14))

        self.go = False  # проигрывать анимацию?
        self.for_slover = 0  # это чтобы она была медленнее
        self.move_direction = 'down'  # двигается вниз

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(chargerx + 30, chargery + 86)  # перемещаю относительно тела

        self.charge_points = 100  # столько в заряднике припасов
        self.object = None  # объект, которому давать припасы

    def update(self, *args, **kwargs):
        if self.time_start_hev_charger_sound is not None and (
                time() - self.time_start_hev_charger_sound > 8 or self.object.suit_health == 100 or
                self.charge_points == 0) and self.go:
            print(f"hev-charger points: {self.charge_points}")
            print(f"object's suit health: {self.object.suit_health}")
            self.go = False
            self.sound.stop()

        self.for_slover += 1
        if self.go and self.for_slover % 2 == 0:
            if self.move_direction == 'down':
                self.rect = self.rect.move(0, 2)
                if self.rect.y >= self.chargery + 125:
                    self.move_direction = 'up'
            else:
                self.rect = self.rect.move(0, -2)
                if self.rect.y <= self.chargery + 90:
                    self.move_direction = 'down'
            if self.for_slover % 4 == 0:
                self.charge_points -= 1
                self.object.suit_health += 1

    def start_animation(self, obj) -> None:
        """Начать анимацию зарядника костюма"""
        if not self.go:
            self.sound.play()
            self.go = True
            self.time_start_hev_charger_sound = time()
            self.object = obj


class HealthChargerBox(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/health_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (416 // 3, 687 // 3))
        self.rect = self.image.get_rect().move(200, 300)
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)


class HealthChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self, chargerx, chargery, sound, *groups):
        super().__init__(*groups)

        self.charge_points = 100
        self.time_start_health_charger_sound = None
        self.sound = sound
        self.chargerx = chargerx
        self.chargery = chargery
        self.go = False
        self.object = None
        self.animation_i = 0
        self.for_slover = 0
        self.images = [
            'images/health_charger/for_animation.png',
            'images/health_charger/for_animation1.png',
            'images/health_charger/for_animation (1).png',
            'images/health_charger/for_animation (2).png',
            'images/health_charger/for_animation (3).png',
            'images/health_charger/for_animation (4).png',
            'images/health_charger/for_animation (5).png',
        ]
        self.image = pygame.image.load(self.images[self.animation_i])
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect().move(self.chargerx + 60, self.chargery + 75)

    def update(self, *args, **kwargs):
        if self.time_start_health_charger_sound is not None and (
                time() - self.time_start_health_charger_sound > 14 or self.object.player_health == 100 or
                self.charge_points == 0) and self.go:
            print(f"health-charger points: {self.charge_points}")
            print(f"object health: {self.object.player_health}")
            self.go = False
            self.sound.stop()

        self.for_slover += 1
        if self.go and self.for_slover % 2 == 0:
            self.animation_i = (self.animation_i + 1) % 6
            self.image = pygame.image.load(self.images[self.animation_i])
            self.image = pygame.transform.scale(self.image, (40, 40))
            self.rect = self.image.get_rect().move(self.chargerx + 60, self.chargery + 75)
            if self.for_slover % 4 == 0:
                self.charge_points -= 1
                self.object.player_health += 1

    def start_animation(self, obj) -> None:
        """Начать анимацию зарядника здоровья"""
        if not self.go:
            self.sound.play()
            self.go = True
            self.time_start_health_charger_sound = time()
            self.object = obj


class HEVCharger:
    def __init__(self, x, y, *groups):
        self.hev_charger = HEVChargerBox(x, y, *groups)
        self.hev_charger_animaton_block = HEVChargerAnimationBlock(self.hev_charger.rect.x, self.hev_charger.rect.y,
                                                                   *groups)

    def start_animation(self, obj):
        self.hev_charger_animaton_block.start_animation(obj)


class HealthCharger:
    def __init__(self, x, y, *groups):
        self.health_charger = HealthChargerBox(x, y, *groups)
        self.health_charger_animaton_block = HealthChargerAnimationBlock(self.health_charger.rect.x,
                                                                         self.health_charger.rect.y,
                                                                         pygame.mixer.Sound(
                                                                             'sounds/health_charger.mp3'),
                                                                         *groups)

    def start_animation(self, obj):
        self.health_charger_animaton_block.start_animation(obj)


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 850, 750
    screen = pygame.display.set_mode(size)

    FPS = 60
    running = True
    cloak = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    HEV_charger = HEVCharger(50, 300, all_sprites)
    health_charger = HealthCharger(250, 300, all_sprites)
    player = Player(150, 300, all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.move_player(25, 0)

                if event.key == pygame.K_a:
                    player.move_player(-25, 0)

                if event.key == pygame.K_w:
                    player.move_player(0, -25)

                if event.key == pygame.K_s:
                    player.move_player(0, 25)

                if event.key == pygame.K_e:
                    if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HEVChargerBox):
                        HEV_charger.start_animation(player)
                    if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HealthChargerBox):
                        health_charger.start_animation(player)

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        cloak.tick(FPS)

    pygame.quit()
