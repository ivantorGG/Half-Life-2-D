from player import Player
from chargers import HEVCharger, HealthCharger
from food import FoodBox, FoodBottery, FoodBullets, FoodMedkitBig, FoodMedkitSmall
from enemies import Crab
from connecting_objects import Level, InvisibleWall
from objects import Bridge, GameLevel
import stats
import controls
from camera import Camera

from screeninfo import get_monitors
import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
pygame.display.set_caption("HALF-LIFE: 2D")
size = width, height = get_monitors()[0].width * 1, get_monitors()[0].height * 1
k_size = width / 1600, height / 900

FPS = 60
cloak = pygame.time.Clock()
screen.fill((255, 255, 255))


def login():
    running = True


def pre_screen():
    running = True
    first_motion = True
    last_place = None
    image, all_sprites, draw_btn, draw_btn2, btn_x1, btn_y1, btn_x2, btn_y2, btn2_x1, btn2_y1, btn2_x2, btn2_y2 = stats.print_pre_screen(
        screen, width, height)
    while running:
        image, first_motion, last_place, running = controls.pre_screen_check_events(image, first_motion, last_place,
                                                                                    width, height, btn_x1, btn_y1,
                                                                                    btn_x2, btn_y2, btn2_x1, btn2_y1,
                                                                                    btn2_x2, btn2_y2)

        pygame.display.flip()
        cloak.tick(FPS)
        all_sprites.draw(screen)
        all_sprites.update()
        draw_btn()
        draw_btn2()
        if running is None:
            running = True


def first_level(player_health, player_suit_health):
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()
    box_walls = pygame.sprite.Group()

    walls_are_visible = True
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', (-300, -200, 'purple'), (880, 0, 'purple'), [all_sprites],
                          level_sprites)

    InvisibleWall(k_size, -854, -290, 1200, -290, level_sprites, box_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, -410, -180, -410, 200, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 950, -180, 950, 200, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, -450, 180, 210, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 220, 260, 350, 260, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 210, 200, 210, 240, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 350, 200, 350, 240, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 350, 180, 445, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 445, 200, 445, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 570, 200, 570, 230, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, 570, 180, 950, 180, level_sprites, invisible_horizontal_walls, is_visible=walls_are_visible)
    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/1.png', (-300, -200, 'purple'), (880, 0, 'purple'), all_sprites,
                          level_sprites)

    control_level = Level(k_size, None, 700, 148, all_sprites)
    player = Player(k_size, screen, -300, -200, player_health, player_suit_health, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    while True:
        do_break = controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                                     invisible_vertical_walls, level=control_level)

        if do_break:
            return True

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(None, invisible_horizontal_walls, invisible_vertical_walls, box_walls)
        all_sprites.draw(screen)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if player.go_again:
            player_health, player_suit_health = first_level(player_health, player_suit_health)
            return player_health, player_suit_health
        camera.update(player)

        if level.completed:
            return player.health, player.suit_health

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)

        pygame.display.flip()
        cloak.tick(FPS)


def second_level(player_health, player_suit_health):
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()
    box_walls = pygame.sprite.Group()

    walls_are_visible = True
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/2.png', (-650, -500, 'purple'), (550, -250, 'purple'), [all_sprites],
                          level_sprites)

    InvisibleWall(k_size, -854, -600, 1200, -600, level_sprites, box_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, -750, -97, -355, 240, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -235, -97, 258, 240, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 380, -97, 670, 240, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -730, -750, -730, -97, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 680, -750, 680, -97, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -354, -80, -354, -5, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, -232, -80, -232, -6, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 258, -96, 258, -5, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)
    InvisibleWall(k_size, 380, -96, 380, -6, level_sprites, invisible_vertical_walls, is_visible=walls_are_visible)

    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/2.png', (-650, -500, 'purple'),
                          (550, -250, 'green'), all_sprites, level_sprites)

    player = Player(k_size, screen, -650, -300, player_health, player_suit_health, all_sprites)
    Crab(k_size, player, 100, -500, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    while True:
        do_break = controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                                     invisible_vertical_walls)

        if do_break:
            return True

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(None, invisible_horizontal_walls, invisible_vertical_walls, box_walls)
        all_sprites.draw(screen)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if level.completed:
            return player.health, player.suit_health

        if player.go_again:
            player_health, player_suit_health = second_level(player_health, player_suit_health)
            return player_health, player_suit_health

        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)
        pygame.display.flip()
        cloak.tick(FPS)


def third_level(player_health, player_suit_health):
    all_sprites = pygame.sprite.Group()
    level_sprites = pygame.sprite.Group()
    invisible_horizontal_walls = pygame.sprite.Group()
    invisible_vertical_walls = pygame.sprite.Group()
    box_walls = pygame.sprite.Group()

    walls_are_visible = True
    if walls_are_visible:
        level = GameLevel(k_size, 'images/levels/3.png', (-3050, -600, 'purple'), (4850, -330, 'purple'), [all_sprites],
                          level_sprites)

    InvisibleWall(k_size, -4000, -1000, 7000, -1000, level_sprites, box_walls, is_visible=walls_are_visible)

    InvisibleWall(k_size, -4200, -155, -2835, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2730, -155, -2640, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2540, -155, -2450, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2355, -155, -2258, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2228, -200, -2137, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1670, -400, -1380, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1990, -310, -1889, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2127, -250, -2030, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1825, -340, -1730, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1160, -400, -1075, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -980, -400, -788, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -510, -270, -320, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -60, -155, 400, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, 1285, -155, 8000, 0, level_sprites, invisible_horizontal_walls,
                  is_visible=walls_are_visible)



    InvisibleWall(k_size, -3155, -777, -3155, -160, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -2835, -150, -2835, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2730, -150, -2730, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2640, -150, -2640, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2540, -150, -2540, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2450, -150, -2450, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2355, -150, -2355, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -2258, -150, -2258, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1670, -400, -1670, -300, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1380, -400, -1380, -300, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -1160, -400, -1160, -300, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -1075, -400, -1075, -300, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -980, -400, -980, -300, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -788, -400, -788, -300, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    InvisibleWall(k_size, -510, -260, -510, -150, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -320, -260, -320, -150, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, -60, -150, -60, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 400, -150, 400, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)
    InvisibleWall(k_size, 1285, -150, 1285, 0, level_sprites, invisible_vertical_walls,
                  is_visible=walls_are_visible)

    if not walls_are_visible:
        level = GameLevel(k_size, 'images/levels/3.png', (-3050, -600, 'purple'),
                          (4850, -330, 'green'), all_sprites, level_sprites)

    player = Player(k_size, screen, -3050, -280, player_health, player_suit_health, all_sprites)
    camera = Camera(width, height)
    camera.update(player)

    while True:
        do_break = controls.first_level_check_events(k_size, player, level, all_sprites, invisible_horizontal_walls,
                                                     invisible_vertical_walls)

        if do_break:
            return True

        screen.fill((0, 0, 0))
        level_sprites.update()
        level_sprites.draw(screen)
        all_sprites.update(invisible_horizontal_walls, invisible_vertical_walls, box_walls)
        all_sprites.draw(screen)

        if not player.died:
            stats.print_stats(screen, k_size, player)

        if level.completed:
            return player.health, player.suit_health

        if player.go_again:
            player_health, player_suit_health = third_level(player_health, player_suit_health)
            return player_health, player_suit_health

        camera.update(player)

        for sprite in all_sprites:
            camera.apply(sprite)
        for sprite in level_sprites:
            camera.apply(sprite)
        pygame.display.flip()
        cloak.tick(FPS)


def main():
    pygame.mouse.set_visible(True)
    # pre_screen()
    pygame.mouse.set_visible(False)
    music = pygame.mixer.Sound('sounds/main_music1.mp3')
    music.play()
    player_health, player_suit_health = 30, 0
    try:
        # player_health, player_suit_health = first_level(player_health, player_suit_health)
        # player_health, player_suit_health = second_level(player_health, player_suit_health)
        player_health, player_suit_health = third_level(player_health, player_suit_health)
        music.stop()
    except TypeError:
        return None


if __name__ == '__main__':
    while True:
        main()
