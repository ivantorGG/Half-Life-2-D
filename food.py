# TODO: add grenade to player's inventory
import random

import pygame
from player import Player
from chips import create_chips


class FoodBottery(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups):
        super().__init__(*groups)
        self.sound = pygame.mixer.Sound('sounds/battery_pickup.mp3')
        self.image = pygame.image.load('images/food/bottery.png')
        self.image = pygame.transform.scale(self.image, (20 * k_size[0], 44 * k_size[1]))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.obj = obj
        self.walls = walls

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                      Player) and self.obj.suit_health <= 90:
            self.sound.play()
            self.obj.suit_health += 10
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                        Player) and self.obj.suit_health < 100:
            self.sound.play()
            self.obj.suit_health = 100
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10


class FoodGrenade(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/ammo_pickup.mp3')
        self.image = pygame.image.load('images/food/grenade.png')
        self.image = pygame.transform.scale(self.image, (round(23 * k_size[0]), round(57 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.obj = obj

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player):
            self.sound.play()
            self.kill()


class FoodMedkitSmall(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('images/food/medkit-small.png')
        self.image = pygame.transform.scale(self.image, (44 * k_size[0], 56 * k_size[1]))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.obj = obj
        self.walls = walls

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                      Player) and self.obj.health <= 85:
            self.obj.health += 15
            self.sound.play()
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                        Player) and self.obj.health < 100:
            self.obj.health = 100
            self.sound.play()
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10


class FoodMedkitBig(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('images/food/medkit_big.png')
        self.image = pygame.transform.scale(self.image, (38 * k_size[0], 35 * k_size[1]))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.obj = obj
        self.walls = walls

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                      Player) and self.obj.health <= 70:
            self.obj.health += 30
            self.sound.play()
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                        Player) and self.obj.health < 100:
            self.obj.health = 100
            self.sound.play()
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10


class FoodBox(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, food, walls, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/lucky_box_crushing.mp3')
        self.image = pygame.image.load('images/food/box.png')
        self.image = pygame.transform.scale(self.image, (round(111 * k_size[0]), round(84 * k_size[1])))
        self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        self.food = food
        self.obj = obj
        self.k_size = k_size
        self.is_crushed = False
        self.walls = walls

    def crush(self):
        self.sound.play()
        img = random.choice(['images/food/crushed_box.png', 'images/food/crushed_box1.png'])
        self.image = pygame.transform.scale(pygame.image.load(img), (self.rect.width, self.rect.height))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        self.food(self.k_size, round((self.rect.centerx - 4) / self.k_size[0]),
                  round((self.rect.centery - 12) / self.k_size[1]), self.obj, self.walls, *self.groups())
        self.is_crushed = True
        create_chips((self.rect.centerx, self.rect.centery - 30), 'FoodBox', self.groups())

    def update(self, *args, **kwargs):
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player) and not self.is_crushed:
            self.crush()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 850, 750
    screen = pygame.display.set_mode(size)

    FPS = 60
    running = True
    cloak = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    box = FoodBox(500, 500, None, FoodGrenade, all_sprites)

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                print(event.pos)

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_q:
                    box.crush()

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        cloak.tick(FPS)

    pygame.quit()
