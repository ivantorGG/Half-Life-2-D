# TODO: add grenade to player's inventory
import pygame
from player import Player


class FoodBottery(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, *groups):
        super().__init__(*groups)
        self.sound = pygame.mixer.Sound('sounds/battery_pickup.mp3')
        self.image = pygame.image.load('images/food/bottery.png')
        self.image = pygame.transform.scale(self.image, (20, 44))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)
        self.obj = obj

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, all_sprites),
                      Player) and self.obj.suit_health <= 90:
            self.sound.play()
            self.obj.suit_health += 10
            print('picked up bottery')
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, all_sprites),
                        Player) and self.obj.suit_health < 100:
            self.sound.play()
            self.obj.suit_health = 100
            print('picked up bottery')
            self.kill()


class FoodGrenade(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/ammo_pickup.mp3')
        self.image = pygame.image.load('images/food/grenade.png')
        self.image = pygame.transform.scale(self.image, (23, 57))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)
        self.obj = obj

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, all_sprites), Player):
            self.sound.play()
            print('picked up grenade')
            self.kill()


class FoodMedkitSmall(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('images/food/medkit-small.png')
        self.image = pygame.transform.scale(self.image, (44, 56))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)
        self.obj = obj

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, all_sprites),
                      Player) and self.obj.player_health <= 85:
            self.obj.player_health += 15
            self.sound.play()
            print('picked up small medkit')
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, all_sprites),
                        Player) and self.obj.player_health < 100:
            self.obj.player_health = 100
            self.sound.play()
            print('picked up small medkit')
            self.kill()


class FoodMedkitBig(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('images/food/medkit_big.png')
        self.image = pygame.transform.scale(self.image, (38, 35))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)
        self.obj = obj

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self, all_sprites),
                      Player) and self.obj.player_health <= 70:
            self.obj.player_health += 30
            self.sound.play()
            print('picked up big medkit')
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self, all_sprites),
                        Player) and self.obj.player_health < 100:
            self.obj.player_health = 100
            self.sound.play()
            print('picked up big medkit')
            self.kill()


class FoodBox(pygame.sprite.Sprite):
    def __init__(self, x, y, obj, food, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/lucky_box_crushing.mp3')
        self.image = pygame.image.load('images/food/lucky-box.png')
        self.image = pygame.transform.scale(self.image, (111, 84))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)
        self.food = food
        self.obj = obj
        self.groups = groups

    def crush(self):
        self.sound.play()
        self.food(self.rect.centerx, self.rect.centery - 15, self.obj, *self.groups)
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

    player = Player(150, 200, all_sprites)

    for i in range(10):
        FoodMedkitBig(30 * i, 50, player, all_sprites)
        FoodMedkitSmall(30 * i, 150, player, all_sprites)
        FoodBottery(30 * i, 250, player, all_sprites)

    box = FoodBox(500, 500, player, FoodGrenade, all_sprites)

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

                if event.key == pygame.K_p:
                    box.crush()
                    player.print_stats()

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        cloak.tick(FPS)

    pygame.quit()
