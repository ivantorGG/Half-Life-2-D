from random import randrange, choice
import pygame

from chips import create_chips
from player import Player


class Crab(pygame.sprite.Sprite):
    def __init__(self, k_size, obj, x, y, *groups, do_move=True):
        super().__init__(*groups)

        self.image = pygame.image.load('images/enemies/Crab/right/1.png')
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_height() * 2 * k_size[0]), round(self.image.get_width() * 2 * k_size[1])))
        if do_move:
            self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        else:
            self.rect = self.image.get_rect(center=(x, y))

        self.phase = 0
        self.for_slower = 0

        self.speed = 6
        self.health = 15
        self.obj = obj
        self.damage = 40
        self.direction = None
        self.killed = False
        self.k_size = k_size
        self.obj.set_enemies(self)

    def move_crab(self, plus_x, plus_y):
        self.rect.centerx += plus_x * self.k_size[0]
        self.rect.centery += plus_y * self.k_size[0]

    def update(self, *args, **kwargs):
        self.for_slower += 1
        if not self.killed:
            if not pygame.sprite.spritecollideany(self, args[0]):
                self.move_crab(0, 20)

            if pygame.sprite.spritecollideany(self, args[0]):
                stop_animating = False
                self.check_direction()

                if self.obj.rect.centerx > self.rect.centerx:
                    self.move_crab(self.speed, 0)
                    if not pygame.sprite.spritecollideany(self, args[0]):
                        self.move_crab(-self.speed, 0)
                        stop_animating = True
                else:
                    self.move_crab(-self.speed, 0)
                    if not pygame.sprite.spritecollideany(self, args[0]):
                        self.move_crab(self.speed, 0)
                        stop_animating = True

                if self.for_slower % 5 == 0 and not stop_animating:
                    self.phase = (self.phase + 1) % 7
                    if not self.phase:
                        self.phase += 1
                    self.image = pygame.image.load(f'images/enemies/Crab/{self.direction}/{self.phase}.png')
                    self.image = pygame.transform.scale(self.image, (
                        round(self.image.get_width() * 2 * self.k_size[0]),
                        round(self.image.get_height() * 2 * self.k_size[1])))
                    self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player) and self.for_slower % 45 == 0:
                if self.obj.suit_health >= self.damage:
                    self.obj.suit_health -= self.damage
                elif self.obj.suit_health > 0:
                    damage_to_player = self.damage - self.obj.suit_health
                    self.obj.suit_health = 0
                    self.obj.health -= damage_to_player
                else:
                    self.obj.health -= self.damage
                    if self.obj.health < 0:
                        self.obj.health = 0

                self.obj.stats['damage took'] += self.damage
                sound = pygame.mixer.Sound(f'sounds/crab_eats{randrange(1, 5)}.mp3')
                sound.play()
            self.check_health()
            if abs(self.obj.rect.y - self.rect.y) > 2000:
                self.killed = True
        else:
            self.move_crab(0, 20)

    def check_direction(self):
        if self.obj.rect.x > self.rect.x:
            self.direction = 'right'

        elif self.obj.rect.x < self.rect.x:
            self.direction = 'left'

    def check_health(self):
        if self.health <= 0:
            create_chips(self.k_size, (self.rect.centerx, self.rect.centery), 'Crab', self.groups())
            self.killed = True
            self.obj.stats['crabs killed'] += 1


class DirectCrab(Crab):
    def __init__(self, k_size, obj, x, y, speed, *groups):
        super().__init__(k_size, obj, x, y, *groups)
        self.direction = 'right' if speed > 0 else 'left'
        self.eating_count = 0
        self.speed = speed
        self.damage = 15
        self.health = 5

    def update(self, *args, **kwargs):
        if not self.killed:
            if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player) and self.for_slower % 3 == 0 and \
                    self.eating_count < 3:
                self.eating_count += 1
                if self.obj.suit_health >= self.damage:
                    self.obj.suit_health -= self.damage
                elif self.obj.suit_health > 0:
                    damage_to_player = self.damage - self.obj.suit_health
                    self.obj.suit_health = 0
                    self.obj.health -= damage_to_player
                else:
                    self.obj.health -= self.damage
                    if self.obj.health < 0:
                        self.obj.health = 0

                self.obj.stats['damage took'] += self.damage
                sound = pygame.mixer.Sound(f'sounds/crab_eats{randrange(1, 5)}.mp3')
                sound.play()

            if self.for_slower % 5 == 0:
                self.phase = (self.phase + 1) % 7
                if not self.phase:
                    self.phase += 1
                self.image = pygame.image.load(f'images/enemies/Crab/{self.direction}/{self.phase}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 2 * self.k_size[0]),
                    round(self.image.get_height() * 2 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            self.move_crab(self.speed, 0)
            self.check_health()
            if abs(self.obj.rect.x - self.rect.x) > 3000 or abs(self.obj.rect.y - self.rect.y) > 2000:
                self.killed = True
        else:
            self.move_crab(0, 20)

        self.for_slower += 1


class TermenatorCrab(Crab):
    def __init__(self, k_size, obj, x, y, speed, *groups):
        super().__init__(k_size, obj, x, y, *groups)
        self.image = pygame.image.load('images/enemies/Crab/right/1.png')
        self.image = pygame.transform.scale(self.image, (
            round(self.image.get_height() * 48 * k_size[0]), round(self.image.get_width() * 48 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.direction = 'right' if speed > 0 else 'left'
        self.speed = speed
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args, **kwargs):
        if pygame.sprite.collide_mask(self, self.obj):
            self.obj.suit_health = 0
            self.obj.health = 0
            sound = pygame.mixer.Sound(f'sounds/crab_eats5.mp3')
            sound.play()

        if self.for_slower % 20 == 0:
            self.phase = (self.phase + 1) % 7
            if not self.phase:
                self.phase += 1
            self.image = pygame.image.load(f'images/enemies/Crab/{self.direction}/{self.phase}.png')
            self.image = pygame.transform.scale(self.image, (
                round(self.image.get_width() * 58 * self.k_size[0]),
                round(self.image.get_height() * 58 * self.k_size[1])))
            self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
            self.mask = pygame.mask.from_surface(self.image)

        self.for_slower += 1
        self.move_crab(self.speed, 0)


class DumbCrab(Crab):
    def __init__(self, k_size, obj, x, y, *groups):
        super().__init__(k_size, obj, x, y, *groups)
        self.direction = choice(('left', 'right'))
        self.speed = -6 if self.direction == 'left' else 6
        self.length = randrange(150)
        self.damage = 10

    def update(self, *args, **kwargs):
        self.for_slower += 1
        if not self.killed:
            if not pygame.sprite.spritecollideany(self, args[0]):
                self.move_crab(0, 20)

            if pygame.sprite.spritecollideany(self, args[0]):
                self.move_crab(self.speed, 0)
                if not pygame.sprite.spritecollideany(self, args[0]) and choice((True, False, False)):
                    if self.direction == 'left':
                        self.move_crab(0, -100)
                        self.move_crab(-self.speed * 4, 0)
                        self.direction = 'right'
                        self.speed = 6
                        self.length = 300
                    else:
                        self.move_crab(0, -100)
                        self.move_crab(-self.speed * 4, 0)
                        self.direction = 'left'
                        self.speed = -6
                        self.length = 300

                if self.for_slower % 5 == 0:
                    self.phase = (self.phase + 1) % 7
                    if not self.phase:
                        self.phase += 1
                    self.image = pygame.image.load(f'images/enemies/Crab/{self.direction}/{self.phase}.png')
                    self.image = pygame.transform.scale(self.image, (
                        round(self.image.get_width() * 2 * self.k_size[0]),
                        round(self.image.get_height() * 2 * self.k_size[1])))
                    self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            else:
                self.length = randrange(500)
                self.direction = choice(('left', 'right'))

            if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player) and self.for_slower % 10 == 0:
                if self.obj.suit_health >= self.damage:
                    self.obj.suit_health -= self.damage
                elif self.obj.suit_health > 0:
                    damage_to_player = self.damage - self.obj.suit_health
                    self.obj.suit_health = 0
                    self.obj.health -= damage_to_player
                else:
                    self.obj.health -= self.damage
                    if self.obj.health < 0:
                        self.obj.health = 0

                self.obj.stats['damage took'] += self.damage
                sound = pygame.mixer.Sound(f'sounds/crab_eats{randrange(1, 5)}.mp3')
                sound.play()

            self.check_health()
            self.length -= 5
            if self.length <= 0:
                self.length = randrange(150)
                self.speed = -6 if self.direction == 'left' else 6
                self.direction = choice(('left', 'right'))

            if abs(self.obj.rect.y - self.rect.y) > 2000 or abs(self.obj.rect.x - self.rect.x) > 2000:
                self.killed = True
        else:
            self.move_crab(0, 20)


class SummonerCrab(DumbCrab):
    def __init__(self, k_size, obj, x, y, *groups):
        super().__init__(k_size, obj, x, y, *groups)
        self.speed = -1 if self.direction == 'left' else 1

    def update(self, *args, **kwargs):
        if not self.killed:
            if not pygame.sprite.spritecollideany(self, args[0]):
                self.move_crab(0, 20)

            if pygame.sprite.spritecollideany(self, args[0]):
                self.move_crab(self.speed, 0)
                if not pygame.sprite.spritecollideany(self, args[0]):
                    if self.direction == 'left':
                        self.move_crab(0, -100)
                        self.move_crab(-self.speed * 4, 0)
                        self.direction = 'right'
                        self.speed = 1
                        self.length = 500
                    else:
                        self.move_crab(0, -100)
                        self.move_crab(-self.speed * 4, 0)
                        self.direction = 'left'
                        self.speed = -1
                        self.length = 500

                if self.for_slower % 5 == 0:
                    self.phase = (self.phase + 1) % 7
                    if not self.phase:
                        self.phase += 1
                    self.image = pygame.image.load(f'images/enemies/Crab/{self.direction}/{self.phase}.png')
                    self.image = pygame.transform.scale(self.image, (
                        round(self.image.get_width() * 2 * self.k_size[0]),
                        round(self.image.get_height() * 2 * self.k_size[1])))
                    self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            else:
                self.length = randrange(500)
                self.direction = choice(('left', 'right'))

            self.check_health()
            self.length -= 5
            if self.length <= 0:
                self.length = randrange(150)
                self.speed = -1 if self.direction == 'left' else 1
                self.direction = choice(('left', 'right'))
                if choice((True, False, False, False, False)):
                    enemy = choice(('Crab', 'DirectCrab', 'DumbCrab'))
                    match enemy:
                        case 'Crab':
                            FlyingEnemy(self.k_size, self.rect.centerx, self.rect.centery, enemy, self.obj, *self.groups())
                        case 'DirectCrab':
                            speed = 20 if self.speed < 0 else -20
                            FlyingEnemy(self.k_size, self.rect.centerx, self.rect.centery, enemy, self.obj, *self.groups(), speed=speed)
                        case 'DumbCrab':
                            FlyingEnemy(self.k_size, self.rect.centerx, self.rect.centery, enemy, self.obj, *self.groups())
        else:
            self.move_crab(0, 20)


class FlyingEnemy(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, enemy, obj, *groups, speed=None):
        super().__init__(*groups)
        self.image = pygame.image.load('images/enemies/SummonerCrab/attack.png')
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.enemy = enemy
        self.length_x = randrange(-250, 250, 10)
        self.speed_x = 5 if self.length_x > 0 else -5
        self.length_y = randrange(20, 160, 10)
        self.speed_y = 5
        self.for_slower = 0
        self.k_size = k_size
        self.obj = obj
        self.enemy_speed = speed

    def update(self, *args, **kwargs):
        self.for_slower += 1
        if self.for_slower % 5 == 0:
            if self.length_x != 0:
                self.length_x -= self.speed_x
                self.rect.x += self.speed_x
            if self.length_y != 0:
                self.length_y -= self.speed_y
                self.rect.y -= self.speed_y
            if self.length_x == 0 and self.length_y == 0:
                match self.enemy:
                    case 'Crab':
                        enemy = Crab(self.k_size, self.obj, self.rect.x, self.rect.y, *self.groups())
                    case 'DirectCrab':
                        enemy = DirectCrab(self.k_size, self.obj, self.rect.x, self.rect.y, self.enemy_speed, *self.groups())
                    case 'DumbCrab':
                        enemy = DumbCrab(self.k_size, self.obj, self.rect.x, self.rect.y, *self.groups())
                self.obj.enemies.append(enemy)
                self.kill()
