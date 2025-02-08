from random import randrange

import pygame

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
        self.obj = obj
        self.damage = 40
        self.direction = None
        self.k_size = k_size

    def move_crab(self, plus_x, plus_y):
        self.rect.centerx += plus_x * self.k_size[0]
        self.rect.centery += plus_y * self.k_size[0]

    def update(self, *args, **kwargs):
        if not pygame.sprite.spritecollideany(self, args[1]):
            self.move_crab(0, 20)

        if pygame.sprite.spritecollideany(self, args[1]):
            stop_animating = False
            self.check_direction()

            if self.obj.rect.centerx > self.rect.centerx:
                self.move_crab(self.speed, 0)
                if not pygame.sprite.spritecollideany(self, args[1]):
                    self.move_crab(-self.speed, 0)
                    stop_animating = True
            else:
                self.move_crab(-self.speed, 0)
                if not pygame.sprite.spritecollideany(self, args[1]):
                    self.move_crab(self.speed, 0)
                    stop_animating = True

            if self.for_slower % 5 == 0 and not stop_animating:
                self.phase = (self.phase + 1) % 7
                if not self.phase:
                    self.phase += 1
                self.image = pygame.image.load(f'images/enemies/Crab/{self.direction}/{self.phase}.png')
                self.image = pygame.transform.scale(self.image, (
                    round(self.image.get_width() * 2 * self.k_size[0]), round(self.image.get_height() * 2 * self.k_size[1])))
                self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))

            self.for_slower += 1

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

            sound = pygame.mixer.Sound(f'sounds/crab_eats{randrange(1, 5)}.mp3')
            sound.play()

    def check_direction(self):
        # if isinstance(pygame.sprite.spritecollideany(self.obj, *self.groups()), Crab):
        #     self.direction = 'attack_left' if self.direction == 'left' else 'attack_right'

        if self.obj.rect.x > self.rect.x:
            self.direction = 'right'

        elif self.obj.rect.x < self.rect.x:
            self.direction = 'left'
