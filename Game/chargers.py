# !!! MAIN CLASSES: HEVCharger, HealthCharger !!!

import pygame


class HEVChargerBox(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, *groups):
        """При инициализации указывать координаты и группы спрайтов"""
        super().__init__(*groups)

        self.image = pygame.image.load('Game/images/hev_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (round(117 * k_size[0]), round(245 * k_size[1])))
        self.rect = self.image.get_rect(center=(round(x * k_size[0]), round(y * k_size[1])))


class HEVChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self, k_size, charger, charge_points, *groups):
        """При инициализации указывать координаты тела зарядника и группы спрайтов"""
        super().__init__(*groups)

        self.charger = charger

        self.sound = pygame.mixer.Sound('Game/sounds/hev_charger.mp3')  # звук
        self.err_sound = pygame.mixer.Sound('Game/sounds/hev_charger-error.mp3')

        self.image = pygame.image.load('Game/images/hev_charger/for_animation.png')
        self.image = pygame.transform.scale(self.image, (round(13 * k_size[0]), round(14 * k_size[1])))

        self.go = False  # проигрывать анимацию?
        self.for_slover = 0  # это чтобы она была медленнее
        self.move_direction = 'down'  # двигается вниз

        self.rect = self.image.get_rect()
        self.rect = self.rect.move(charger.rect.x + 30 * k_size[0],
                                   charger.rect.y + 86 * k_size[1])  # перемещаю относительно тела

        self.charge_points = charge_points  # столько в заряднике припасов
        self.object = None  # объект, которому давать припасы

        self.k_size = k_size

    def update(self, *args, **kwargs):
        if self.object is not None and (
                (self.object.suit_health == 100 or self.charge_points == 0) and self.go or not isinstance(
                pygame.sprite.spritecollideany(self.object, *self.groups()), HEVChargerBox)):
            self.go = False
            self.sound.stop()

        self.for_slover += 1
        if self.go and self.for_slover % 2 == 0:
            if self.move_direction == 'down':
                self.rect = self.rect.move(0, round(2 * self.k_size[1]))
                if self.rect.y >= self.charger.rect.y + 125 * self.k_size[1]:
                    self.move_direction = 'up'
            else:
                self.rect = self.rect.move(0, round(-2 * self.k_size[1]))
                if self.rect.y <= self.charger.rect.y + 90 * self.k_size[1]:
                    self.move_direction = 'down'
            if self.for_slover % 4 == 0:
                self.charge_points -= 1
                self.object.suit_health += 1
                self.object.stats['HEVCharger used'] += 1

    def start_animation(self, obj) -> None:
        """Начать анимацию зарядника костюма"""
        if not self.go:
            if self.charge_points == 0 or obj.suit_health == 100:
                self.err_sound.play()
            else:
                self.sound.play()
                self.go = True
                self.object = obj


class HealthChargerBox(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('Game/images/health_charger/charger.png')
        self.image = pygame.transform.scale(self.image, (round(416 // 3 * k_size[0]), round(687 // 3 * k_size[1])))
        self.rect = self.image.get_rect(center=(round(x * k_size[0]), round(y * k_size[1])))


class HealthChargerAnimationBlock(pygame.sprite.Sprite):
    def __init__(self, k_size, charger, charge_points, *groups):
        super().__init__(*groups)

        self.charge_points = charge_points

        self.sound = pygame.mixer.Sound('Game/sounds/health_charger.mp3')
        self.err_sound = pygame.mixer.Sound('Game/sounds/health_charger-error.mp3')

        self.charger = charger
        self.go = False
        self.object = None
        self.animation_i = 0
        self.for_slover = 0
        self.images = [
            'Game/images/health_charger/for_animation.png',
            'Game/images/health_charger/for_animation1.png',
            'Game/images/health_charger/for_animation (1).png',
            'Game/images/health_charger/for_animation (2).png',
            'Game/images/health_charger/for_animation (3).png',
            'Game/images/health_charger/for_animation (4).png',
            'Game/images/health_charger/for_animation (5).png',
        ]

        self.image = pygame.image.load(self.images[self.animation_i])
        self.image = pygame.transform.scale(self.image, (round(40 * k_size[0]), round(40 * k_size[1])))
        self.rect = self.image.get_rect().move(self.charger.rect.x + 60 * k_size[0],
                                               self.charger.rect.y + 75 * k_size[1])

        self.k_size = k_size

    def update(self, *args, **kwargs):
        if self.object is not None and (((self.object.health == 100 or
                                          self.charge_points == 0) and self.go) or not isinstance(
                pygame.sprite.spritecollideany(self.object, *self.groups()), HealthChargerBox)):
            self.go = False
            self.sound.stop()

        self.for_slover += 1
        if self.go and self.for_slover % 2 == 0:
            self.animation_i = (self.animation_i + 1) % 6
            self.image = pygame.image.load(self.images[self.animation_i])
            self.image = pygame.transform.scale(self.image, (round(40 * self.k_size[0]), round(40 * self.k_size[1])))
            self.rect = self.image.get_rect().move(self.charger.rect.x + 60 * self.k_size[0],
                                                   self.charger.rect.y + 75 * self.k_size[1])
            if self.for_slover % 4 == 0:
                self.charge_points -= 1
                self.object.health += 1
                self.object.stats['HealthCharger used'] += 1

    def start_animation(self, obj) -> None:
        """Начать анимацию зарядника здоровья"""
        if not self.go:
            if self.charge_points == 0 or obj.health == 100:
                self.err_sound.play()
            else:
                self.sound.play()
                self.go = True
                self.object = obj


class HEVCharger:
    def __init__(self, k_size, x, y, charge_points, *groups):
        self.hev_charger = HEVChargerBox(k_size, x, y, *groups)
        self.hev_charger_animaton_block = HEVChargerAnimationBlock(k_size, self.hev_charger, charge_points,
                                                                   *groups)

    def start_animation(self, obj):
        self.hev_charger_animaton_block.start_animation(obj)


class HealthCharger:
    def __init__(self, k_size, x, y, charge_points, *groups):
        self.health_charger = HealthChargerBox(k_size, x, y, *groups)
        self.health_charger_animaton_block = HealthChargerAnimationBlock(k_size, self.health_charger, charge_points,
                                                                         *groups)

    def start_animation(self, obj):
        self.health_charger_animaton_block.start_animation(obj)

