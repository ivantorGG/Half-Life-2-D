import random

import pygame
from Game.player import Player
from Game.chips import create_chips


class FoodBattery(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups, do_move=True):
        super().__init__(*groups)
        self.sound = pygame.mixer.Sound('Game/sounds/battery_pickup.mp3')
        self.image = pygame.image.load('Game/images/food/bottery.png')
        self.image = pygame.transform.scale(self.image, (20 * k_size[0], 44 * k_size[1]))
        if do_move:
            self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        else:
            self.rect = self.image.get_rect(center=(x, y))
        self.obj = obj
        self.walls = walls
        self.k_size = k_size

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                      Player) and self.obj.suit_health <= 90:
            self.obj.stats['batteries ate'] += 1
            self.sound.play()
            self.obj.suit_health += 10
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                        Player) and self.obj.suit_health < 100:
            self.obj.stats['batteries ate'] += 1
            self.sound.play()
            self.obj.suit_health = 100
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10 * self.k_size[0]
        if abs(self.rect.x - self.obj.rect.x) > 3000 or abs(self.rect.y - self.obj.rect.y) > 2000:
            self.kill()


class FoodBullets(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups, do_move=True):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('Game/sounds/ammo_pickup.mp3')
        self.image = pygame.image.load('Game/images/food/grenade.png')
        self.image = pygame.transform.scale(self.image, (round(23 * k_size[0]), round(57 * k_size[1])))
        if do_move:
            self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        else:
            self.rect = self.image.get_rect(center=(x, y))
        self.obj = obj
        self.k_size = k_size
        self.walls = walls

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player):
            self.obj.stats['bullets ate'] += 1
            self.sound.play()
            self.obj.bullets += 5
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10 * self.k_size[0]
        if abs(self.rect.x - self.obj.rect.x) > 3000 or abs(self.rect.y - self.obj.rect.y) > 2000:
            self.kill()


class FoodMedkitSmall(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups, do_move=True):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('Game/sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('Game/images/food/medkit-small.png')
        self.image = pygame.transform.scale(self.image, (44 * k_size[0], 56 * k_size[1]))
        if do_move:
            self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        else:
            self.rect = self.image.get_rect(center=(x, y))
        self.obj = obj
        self.walls = walls
        self.k_size = k_size

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                      Player) and self.obj.health <= 85:
            self.obj.stats['medkits ate'] += 1
            self.obj.health += 15
            self.sound.play()
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                        Player) and self.obj.health < 100:
            self.obj.stats['medkits ate'] += 1
            self.obj.health = 100
            self.sound.play()
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10 * self.k_size[0]
        if abs(self.rect.x - self.obj.rect.x) > 3000 or abs(self.rect.y - self.obj.rect.y) > 2000:
            self.kill()


class FoodMedkitBig(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, walls, *groups, do_move=True):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('Game/sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('Game/images/food/medkit_big.png')
        self.image = pygame.transform.scale(self.image, (38 * k_size[0], 35 * k_size[1]))
        if do_move:
            self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        else:
            self.rect = self.image.get_rect(center=(x, y))
        self.obj = obj
        self.walls = walls
        self.k_size = k_size

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                      Player) and self.obj.health <= 70:
            self.obj.stats['medkits ate'] += 1
            self.obj.health += 30
            self.sound.play()
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, *self.groups()),
                        Player) and self.obj.health < 100:
            self.obj.stats['medkits ate'] += 1
            self.obj.health = 100
            self.sound.play()
            self.kill()
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10 * self.k_size[0]
        if abs(self.rect.x - self.obj.rect.x) > 3000 or abs(self.rect.y - self.obj.rect.y) > 2000:
            self.kill()


class FoodBox(pygame.sprite.Sprite):
    def __init__(self, k_size, x, y, obj, food, walls, *groups, do_move=True):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('Game/sounds/lucky_box_crushing.mp3')
        self.image = pygame.image.load('Game/images/food/box.png')
        self.image = pygame.transform.scale(self.image, (round(111 * k_size[0]), round(84 * k_size[1])))
        if do_move:
            self.rect = self.image.get_rect(center=(x * k_size[0], y * k_size[1]))
        else:
            self.rect = self.image.get_rect(center=(x, y))
        self.food = food
        self.obj = obj
        self.k_size = k_size
        self.is_crushed = False
        self.walls = walls
        self.k_size = k_size

    def crush(self):
        self.obj.stats['boxes crushed'] += 1
        self.sound.play()
        img = random.choice(['Game/images/food/crushed_box.png', 'Game/images/food/crushed_box1.png'])
        self.image = pygame.transform.scale(pygame.image.load(img), (self.rect.width, self.rect.height))
        self.rect = self.image.get_rect(center=(self.rect.centerx, self.rect.centery))
        self.food(self.k_size, round((self.rect.centerx - 4) / self.k_size[0]),
                  round((self.rect.centery - 12) / self.k_size[1]), self.obj, self.walls, *self.groups())
        self.is_crushed = True
        create_chips(self.k_size, (self.rect.centerx, self.rect.centery - 30), 'FoodBox', self.groups())

    def update(self, *args, **kwargs):
        if not pygame.sprite.spritecollideany(self, self.walls):
            self.rect.y += 10 * self.k_size[0]
        if isinstance(pygame.sprite.spritecollideany(self, *self.groups()), Player) and not self.is_crushed:
            self.crush()
        if abs(self.rect.x - self.obj.rect.x) > 3000 or abs(self.rect.y - self.obj.rect.y) > 2000:
            self.kill()


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 850, 750
    screen = pygame.display.set_mode(size)

    FPS = 60
    running = True
    cloak = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    box = FoodBox(500, 500, None, FoodBullets, all_sprites)

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
