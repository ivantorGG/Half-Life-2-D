import pygame
import sys

from chargers import HEVChargerBox, HealthChargerBox
from connecting_objects import Level
from enemies import Crab
from food import *


def pre_screen_check_events(image, first_motion, last_place, width, height, btn_x1, btn_y1, btn_x2, btn_y2, btn2_x1,
                            btn2_y1, btn2_x2, btn2_y2):
    """Проверка событий pygame"""
    running = None
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            if first_motion:
                last_place = event.pos
                first_motion = False
            else:
                curr_place = event.pos
                if last_place[0] > curr_place[0] and image.rect.x < 0:
                    image.rect.x += 1
                elif last_place[0] < curr_place[0] and image.rect.x > -(width * 1.2 - width):
                    image.rect.x -= 1
                if last_place[1] > curr_place[1] and image.rect.y < 0:
                    image.rect.y += 1
                elif last_place[1] < curr_place[1] and image.rect.y > -(height * 1.2 - height):
                    image.rect.y -= 1
                last_place = curr_place

        if event.type == pygame.MOUSEBUTTONDOWN:
            # в кнопке "старт"
            if event.pos[0] in range(btn_x1, btn_x2) and \
                    event.pos[1] in range(btn_y1, btn_y2):
                running = False
            # в кнопке "выход"
            if event.pos[0] in range(btn2_x1, btn2_x2) and \
                    event.pos[1] in range(btn2_y1, btn2_y2):
                pygame.quit()
                sys.exit()

    return image, first_motion, last_place, running


def first_level_check_events(k_size, player, game_level, all_sprites, invisible_horizontal_walls,
                             invisible_vertical_walls,
                             HEV_charger=None, health_charger=None, level=None):
    """Проверка событий pygame"""
    E_sound = pygame.mixer.Sound('sounds/E_button-pressed.mp3')
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            player.shoot()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                player.move_right = True

            if event.key == pygame.K_a:
                player.move_left = True

            if event.key == pygame.K_w or event.key == pygame.K_SPACE:

                if pygame.sprite.spritecollideany(player, invisible_horizontal_walls):
                    player.jumping = True
                    player.is_now_jumping = True

            if event.key == pygame.K_s or event.key == pygame.K_LCTRL:
                player.crouch = True
                player.crouched = False

            if event.key == pygame.K_LSHIFT:
                player.speed = 20

            if event.key == pygame.K_e:
                no_action = True
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HEVChargerBox):
                    HEV_charger.start_animation(player)
                    no_action = False
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), HealthChargerBox):
                    health_charger.start_animation(player)
                    no_action = False
                if isinstance(pygame.sprite.spritecollideany(player, all_sprites), Level):
                    if level.switch():
                        no_action = False
                        FoodBottery(k_size, game_level.rect.centerx + 210 * k_size[0], -200 * k_size[0], player,
                                    invisible_horizontal_walls, all_sprites, do_move=False)
                        FoodBottery(k_size, game_level.rect.centerx + 210 * k_size[0], -600 * k_size[0], player,
                                    invisible_horizontal_walls, all_sprites, do_move=False)
                        FoodMedkitBig(k_size, game_level.rect.centerx + 210 * k_size[0], -800 * k_size[0], player,
                                      invisible_horizontal_walls, all_sprites, do_move=False)
                        FoodBox(k_size, game_level.rect.centerx + 210 * k_size[0], -1200 * k_size[0], player,
                                FoodBottery, invisible_horizontal_walls, all_sprites, do_move=False)
                        FoodMedkitSmall(k_size, game_level.rect.centerx + 210 * k_size[0], -400 * k_size[0], player,
                                        invisible_horizontal_walls, all_sprites, do_move=False)

                        Crab(k_size, player, game_level.rect.centerx + 310 * k_size[0], -12500 * k_size[0], all_sprites,
                             do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + 210 * k_size[0], -12500 * k_size[0], all_sprites,
                             do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + 110 * k_size[0], -12500 * k_size[0], all_sprites,
                             do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + 10 * k_size[0], -12500 * k_size[0], all_sprites,
                             do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -110 * k_size[0], -12500 * k_size[0],
                             all_sprites, do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -210 * k_size[0], -12500 * k_size[0],
                             all_sprites, do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -310 * k_size[0], -12500 * k_size[0],
                             all_sprites, do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -310 * k_size[0], -10500 * k_size[0],
                             all_sprites, do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -410 * k_size[0], -13500 * k_size[0],
                             all_sprites, do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -110 * k_size[0], -13500 * k_size[0],
                             all_sprites, do_move=False)
                        Crab(k_size, player, game_level.rect.centerx + -510 * k_size[0], -13500 * k_size[0],
                             all_sprites, do_move=False)
                if no_action:
                    E_sound.play()

            if event.key == pygame.K_p:
                player.print_stats()

            if event.key == pygame.K_ESCAPE:
                return True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_d:
                player.move_right = False

            if event.key == pygame.K_a:
                player.move_left = False

            if event.key == pygame.K_s or event.key == pygame.K_LCTRL:
                player.crouch = False
                player.crouched = True

            if event.key == pygame.K_w or event.key == pygame.K_SPACE:
                player.jumping = False

            if event.key == pygame.K_LSHIFT:
                player.speed = 10
