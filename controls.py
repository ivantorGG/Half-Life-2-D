import pygame
import sys

from chargers import HEVChargerBox, HealthChargerBox


def pre_screen_check_events(image, first_motion, last_place):
    """Проверка событий pygame"""
    running = None
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEMOTION:
            if first_motion:
                last_place = event.pos
                first_motion = False
            else:
                curr_place = event.pos
                if last_place[0] > curr_place[0]:
                    image.rect.x += 1
                elif last_place[0] < curr_place[0]:
                    image.rect.x -= 1
                if last_place[1] > curr_place[1]:
                    image.rect.y += 1
                elif last_place[1] < curr_place[1]:
                    image.rect.y -= 1
                last_place = curr_place

        if event.type == pygame.MOUSEBUTTONDOWN and event.pos[0] in range(57, 528) and \
                event.pos[1] in range(408, 441):
            running = False

    return image, first_motion, last_place, running


def main_game_check_events(player, all_sprites, HEV_charger=None, health_charger=None):
    """Проверка событий pygame"""
    E_sound = pygame.mixer.Sound('sounds/E_button-pressed.mp3')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right = True

            if event.key == pygame.K_a:
                player.move_left = True

            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                player.jumping = True
                player.is_now_jumping = True

            if event.key == pygame.K_s:
                player.crouch = True

            if event.key == pygame.K_e:
                no_action = True
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HEVChargerBox):
                    HEV_charger.start_animation(player)
                    no_action = False
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HealthChargerBox):
                    health_charger.start_animation(player)
                    no_action = False
                if no_action:
                    E_sound.play()

            if event.key == pygame.K_p:
                player.print_stats()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_right = False

            if event.key == pygame.K_a:
                player.move_left = False

            if event.key == pygame.K_s:
                player.crouch = False

            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                player.jumping = False

