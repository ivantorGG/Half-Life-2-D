import pygame
import sys

from chargers import HEVChargerBox, HealthChargerBox


def check_events(player, all_sprites, HEV_charger, health_charger):
    """Проверка событий pygame"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

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
