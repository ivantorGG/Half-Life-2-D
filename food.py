# TODO: add grenade to player's inventory
import pygame
from player import Player


class FoodBottery(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.sound = pygame.mixer.Sound('sounds/battery_pickup.mp3')
        self.image = pygame.image.load('images/food/bottery.png')
        self.image = pygame.transform.scale(self.image, (20, 44))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites),
                      FoodBottery) and self.obj.suit_health <= 90:
            self.sound.play()
            self.obj.suit_health += 10
            print('picked up bottery')
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites),
                        FoodBottery) and self.obj.suit_health <= 100:
            self.sound.play()
            self.obj.suit_health = 100
            print('picked up bottery')
            self.kill()

    def set_obj(self, obj):
        self.obj = obj


class FoodGrenade(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/ammo_pickup.mp3')
        self.image = pygame.image.load('images/food/grenade.png')
        self.image = pygame.transform.scale(self.image, (23, 57))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites), FoodGrenade):
            self.sound.play()
            print('picked up grenade')
            self.kill()

    def set_obj(self, obj):
        self.obj = obj


class FoodMedkitSmall(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('images/food/medkit-small.png')
        self.image = pygame.transform.scale(self.image, (44, 56))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites),
                      FoodMedkitSmall) and self.obj.player_health <= 85:
            self.obj.player_health += 15
            self.sound.play()
            print('picked up small medkit')
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites),
                        FoodMedkitSmall) and self.obj.player_health <= 100:
            self.obj.player_health = 100
            self.sound.play()
            print('picked up small medkit')
            self.kill()

    def set_obj(self, obj):
        self.obj = obj


class FoodMedkitBig(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)

        self.sound = pygame.mixer.Sound('sounds/smallmedkit1.mp3')
        self.image = pygame.image.load('images/food/medkit_big.png')
        self.image = pygame.transform.scale(self.image, (38, 35))
        self.rect = self.image.get_rect()
        self.rect = self.rect.move(x - self.rect.x, y - self.rect.y)

    def update(self, *args, **kwargs):
        if isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites),
                      FoodMedkitBig) and self.obj.player_health <= 70:
            self.obj.player_health += 30
            self.sound.play()
            print('picked up big medkit')
            self.kill()
        elif isinstance(pygame.sprite.spritecollideany(self.obj, all_sprites),
                        FoodMedkitBig) and self.obj.player_health <= 100:
            self.obj.player_health = 100
            self.sound.play()
            print('picked up big medkit')
            self.kill()

    def set_obj(self, obj):
        self.obj = obj


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 850, 750
    screen = pygame.display.set_mode(size)

    FPS = 60
    running = True
    cloak = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    bottery1 = FoodBottery(70, 300, all_sprites)
    grenade1 = FoodGrenade(170, 300, all_sprites)
    small_medkit = FoodMedkitSmall(270, 300, all_sprites)
    big_medkit = FoodMedkitBig(370, 300, all_sprites)
    player = Player(150, 200, all_sprites)

    bottery1.set_obj(player)
    grenade1.set_obj(player)
    small_medkit.set_obj(player)
    big_medkit.set_obj(player)

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

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        cloak.tick(FPS)

    pygame.quit()
