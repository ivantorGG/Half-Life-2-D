from player import Player
from chargers import HEVCharger, HealthCharger, HEVChargerBox, HealthChargerBox
import pygame


if __name__ == '__main__':
    pygame.init()
    pygame.mixer.init()
    size = width, height = 850, 750
    screen = pygame.display.set_mode(size)

    FPS = 60
    running = True
    cloak = pygame.time.Clock()

    all_sprites = pygame.sprite.Group()

    HEV_charger1 = HEVCharger(50, 300, all_sprites)
    health_charger = HealthCharger(450, 300, all_sprites)
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
                        HEV_charger1.start_animation()
                    if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HealthChargerBox):
                        health_charger.start_animation()

        screen.fill((0, 0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        cloak.tick(FPS)

    pygame.quit()
