import pygame
import sys

from chargers import HEVChargerBox, HealthChargerBox


def pre_screen_check_events():
    """Проверка событий pygame"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(57, 528) and \
                event.pos[1] in range(408, 441):
            return False


def main_game_check_events(player, all_sprites, HEV_charger, health_charger):
    """Проверка событий pygame"""
    E_sound = pygame.mixer.Sound('sounds/E_button-pressed.mp3')
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
                E_sound.play()
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HEVChargerBox):
                    HEV_charger.start_animation(player)
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HealthChargerBox):
                    health_charger.start_animation(player)
