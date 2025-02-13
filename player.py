from random import randrange

import pygame
import stats
from weapons import GlockBullet


class Player(pygame.sprite.Sprite):
    def __init__(self, k_size, screen, x, y, health, suit_health, bullets, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load('images/gordon/right/stand.png')
        self.image = pygame.transform.scale(self.image, (round(83 * k_size[0]), round(208 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.mask = pygame.mask.from_surface(self.image)

        self.move_left = False
        self.move_right = False
        self.jumping = False
        self.is_now_jumping = False
        self.crouch = False
        self.crouched = False
        self.jumping_speed = -60
        self.direction = 'right'

        self.health = health * 999
        self.suit_health = suit_health

        self.bullets = bullets + 50

        self.shooting_count = 0
        self.phase = 0
        self.for_slower = 1
        self.jumped_direction = ''

        self.k_size = k_size

        self.x = x
        self.y = y
        self.speed = 10
        self.base_x = x
        self.base_y = y

        self.i = 0
        self.screen = screen
        self.died = False
        self.go_again = False
        self.enemies = []

    def move_player(self, plus_x, plus_y):
        self.rect.centerx += plus_x * self.k_size[0]
        self.rect.centery += plus_y * self.k_size[0]
        self.x += plus_x
        self.y += plus_y

    def print_stats(self):
        print(f'player_health:{self.health}')
        print(f'suit_health:{self.suit_health}')
        print(f'ko-ords:{(self.x, self.y)}')

    def update(self, *args, **kwargs):
        self.update_animation_phases()

        if not pygame.sprite.spritecollideany(self, args[0]):
            self.move_player(0, 20)

        else:
            self.move_player(0, -20)
            if not pygame.sprite.spritecollideany(self, args[0]):
                self.move_player(0, 20)
            else:
                self.move_player(0, -15)
                if not pygame.sprite.spritecollideany(self, args[0]):
                    self.move_player(0, 15)
                else:
                    self.move_player(0, -10)
                    if not pygame.sprite.spritecollideany(self, args[0]):
                        self.move_player(0, 10)
                    else:
                        self.move_player(0, -5)
                        if not pygame.sprite.spritecollideany(self, args[0]):
                            self.move_player(0, 5)

        if not self.shooting_count:
            if self.jumping and pygame.sprite.spritecollideany(self, args[0]) and not pygame.sprite.spritecollideany(
                    self, args[1]):
                if self.is_now_jumping is False:
                    self.is_now_jumping = True
                    sound = pygame.mixer.Sound(f'sounds/jump_{randrange(1, 4)}.mp3')
                    sound.play()

            if self.move_left:
                self.move_player(-self.speed, 0)
                if pygame.sprite.spritecollideany(self, args[1]):
                    self.move_player(self.speed, 0)

            if self.move_right:
                self.move_player(self.speed, 0)
                if pygame.sprite.spritecollideany(self, args[1]):
                    self.move_player(-self.speed, 0)

            if (self.move_left or self.move_right) and not self.is_now_jumping and self.for_slower % 13 == 0:
                sound = pygame.mixer.Sound(f'sounds/walk_{randrange(1, 3)}.mp3')
                sound.play()

            if (self.move_right or self.move_left) and \
                    self.direction != 'Jump-right' and self.direction != 'Jump-left' and not self.crouch:  # если только бегает
                if self.for_slower % 5 == 0:
                    self.phase = (self.phase + 2) % 8
                    if not self.phase:
                        self.phase += 2
                    self.image = pygame.transform.scale(
                        pygame.image.load(f'images/gordon/{self.direction}/{self.phase}.png'),
                        (round(83 * self.k_size[0]), round(208 * self.k_size[1])))
                    self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            elif self.direction != 'Jump-right' and self.direction != 'Jump-left' and not self.crouch and not self.crouched:
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                    (round(83 * self.k_size[0]), round(208 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            elif (
                    self.direction == 'Jump-right' or self.direction == 'Jump-left') and self.is_now_jumping and not self.crouch:
                self.image = pygame.transform.scale(pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                                                    (round(352 / 2.6 * self.k_size[0]),
                                                     round(500 / 2.6 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                self.move_player(0, self.jumping_speed)
                if pygame.sprite.spritecollideany(self, args[0]):
                    self.move_player(0, -self.jumping_speed)
                self.jumping_speed += 4
                if self.jumping_speed == 20:
                    self.jumping_speed = -60
                    self.is_now_jumping = False
                    self.direction = 'left' if self.direction == 'Jump-left' else 'right'
                    self.image = pygame.transform.scale(pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                                                        (round(83 * self.k_size[0]),
                                                         round(208 * self.k_size[1])))
                    self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            if self.crouch and self.for_slower % 5 == 0:
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/{self.direction}/stand.png'),
                    (round(105 * self.k_size[0]), round(142 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            if self.crouched and not (self.move_right or self.move_left or self.is_now_jumping or self.jumping):
                self.image = pygame.transform.scale(
                    self.image,
                    (round(105 * self.k_size[0]), round(142 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            if (self.move_right or self.move_left) and self.crouch:
                self.phase = (self.phase + 2) % 10
                if not self.phase:
                    self.phase += 2
                if self.for_slower % 5 == 0:
                    self.image = pygame.transform.scale(
                        pygame.image.load(f'images/gordon/{self.direction}/{self.phase}.png'),
                        (round(105 * self.k_size[0]), round(142 * self.k_size[1])))
                    self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        else:
            self.shooting_count -= 1

        if self.move_left or self.move_right or self.is_now_jumping or self.jumping:
            self.crouched = False

        self.mask = pygame.mask.from_surface(self.image)
        self.for_slower += 1
        self.is_in_death_zone()
        self.is_alive()

    def update_animation_phases(self):
        if self.move_left and self.jumping:
            self.direction = 'Jump-left'

        if self.move_right and self.jumping:
            self.direction = 'Jump-right'

        if self.move_left and not self.is_now_jumping:
            self.direction = 'left'

        if self.move_right and not self.is_now_jumping:
            self.direction = 'right'

        if self.jumping and not self.move_right and not self.move_left and \
                self.direction != 'Jump-right' and self.direction != 'Jump-left':
            if self.direction == 'right':
                self.direction = 'Jump-right'
            elif self.direction == 'left':
                self.direction = 'Jump-left'

        if self.move_left and self.crouch:
            self.direction = 'crouch_left'

        if self.move_right and self.crouch:
            self.direction = 'crouch_right'

    def is_alive(self):
        if self.health <= 0:
            self.i += 1
            stats.print_death_screen(self.screen, self.i, self.i == 1)
            self.image = pygame.Surface((0, 0))
            self.rect = pygame.Rect(0, 0, 0, 0)
            self.died = True
            if self.i >= 250:
                self.go_again = True

    def is_in_death_zone(self):
        if self.y > 700:
            self.health = 0

    def shoot(self):
        if self.bullets > 0:
            sound = pygame.mixer.Sound('sounds/shoot1.mp3')
            sound.play()
            self.shooting_count = 15
            self.bullets -= 1
            if self.direction == 'left' or self.direction == 'Jump-left':
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/attack_gun/left.png'),
                    (round(205 * self.k_size[0]), round(217 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                GlockBullet(self.rect.centerx - 80, self.rect.centery - 76, 'left', self.enemies, *self.groups())

            elif self.direction == 'right' or self.direction == 'Jump-right':
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/attack_gun/right.png'),
                    (round(161 * 1.1 * self.k_size[0]), round(193 * 1.1 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                GlockBullet(self.rect.centerx + 64, self.rect.centery - 84, 'right', self.enemies, *self.groups())

            elif self.direction == 'crouch_left':
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/attack_gun/crouch_left.png'),
                    (round(167 * self.k_size[0]), round(150 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                GlockBullet(self.rect.centerx - 54, self.rect.centery - 54, 'left', self.enemies, *self.groups())

            elif self.direction == 'crouch_right':
                self.image = pygame.transform.scale(
                    pygame.image.load(f'images/gordon/attack_gun/crouch_right.png'),
                    (round(167 * self.k_size[0]), round(148 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
                GlockBullet(self.rect.centerx + 48, self.rect.centery - 54, 'right', self.enemies, *self.groups())

    def set_enemies(self, *enemies):
        self.enemies += list(enemies)
